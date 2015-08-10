Bower. RequireJS. JamJS. Browserify. JQuery, Underscore, Lodash, and did I
mention JQuery? Angular, D3, Polymer, Flux, Ember.js, Backbone, React, Dojo,
Mootools, Bootstrap, Foundation, Meteor, Socket.io, Aurelia, Express.

What do all of these have in common?

For one, the fact that even though I've been using JavaScript for several
years, having written thousands of lines of code used by hundreds of people, I
have never used any of them. I don't know any of their APIs. To date, every
website I've written was hand-coded, starting from blank HTML file. And a lot
of people frown upon that.

"Computers are all about automation," you say, "There's no good reason to
impose the drudgery of boilerplate upon yourself. You'll end up writing lots of
duplicate code."

Which is partly true. What you fail to mention is that I'd be writing plenty of
duplicate code *anyway*.
[Consider,](https://github.com/mbostock/d3/wiki/Requests#d3_xhr)
[for](http://api.jquery.com/jquery.ajax/)
[instance,](http://mootools.net/core/docs/1.5.1/Request/Request)
[the](https://github.com/Raynos/xhr)
[XMLHttpRequest](http://dojotoolkit.org/reference-guide/1.10/dojo/xhr.html)
[API](http://www.w3.org/TR/XMLHttpRequest/). Each reimplementation of XHR is
basically the same thing, with slightly different method names or argument
conventions. As a developer, I would rather know the Real API---I can use it
anywhere I want, and I have unrestricted access to the entire API (so I'm not
at the mercy of someone who doesn't think PUT requests are worth implementing).

Each new "web technology" has its own Wiki, API doc and "getting started" page
which you need to somehow absorb ideas from. They have their own strange
installation rituals, their own vocabulary, their own "best practices", and
their own encyclopedia of StackOverflow answers that you must read if you have
any hope of getting stuff done.

Worse, though: they try to influence how you design.

All these "platforms" advertise themselves as "frameworks". They force you to
structure a project so that it conforms with the architecture that they want.
They're monoliths, and they don't like cooperating with other monoliths.

That's a horrible way to do web design. If [PHP
hammers](http://eev.ee/blog/2012/04/09/php-a-fractal-of-bad-design/) have a
claw on each end, then JS hammers are actually disguised combined harvesters
that accept callbacks.

The first part of the problem is pedagogical in nature. To someone who is just
beginning to learn web development, being introduced to a monstrous framework
can lead to all sorts of misconceptions. jQuery is *not* a programming
language.  JavaScript *can* change the color of text on its own.

Students begin to learn from a higher level of abstraction than is necessary.
Filling in the blanks by copy-pasting lots of boilerplate code is not computer
science. You should know why you're using a tool. Experience should come before
abstraction.

The other part of the problem is more practical.

These architectures look shiny in contrived demo situations (name a modern-day
language that does not boast of a beautiful "hello-world" scenario), but in the
real world, their abstractions almost immediately begin leaking. You end up
writing patches to tide over important features marked "TODO" on Github. You
end up writing glue code, which is far worse than "the drudgery of
boilerplate".

Which isn't to say you shouldn't be using---or writing---JavaScript libraries.
But you should be writing small, self-contained modules that provide a clean
interface that is optimized for communicating with other programs. You should
be using conventional vocabulary and idioms everywhere (even if those idioms
smell like the dead fish that is JavaScript semantics). [Don't build a
cathedral](http://www.catb.org/~esr/writings/cathedral-bazaar/) if you can get
things done with a stall at the bazaar.

Your programs should [do one thing, and do it
well](http://en.wikipedia.org/wiki/Unix_philosophy). It could be a small thing
or a big thing. It could be a color picker widget or a library to encode PDF
files. It doesn't matter. It should be self-contained and present itself as a
tool. Programmers should control code; code shouldn't control programmers.

---

How?

**Avoid side effects.** The vast majority of your functions should take inputs
and return an output. Things that change state should be limited as much as
possible, and should *always* do so because the end-user explicitly mandated
it. The moment you start messing about with global prototypes and settings, or
pushing to arrays you didn't create, you're going to end up taking over the
entire application.

**Namespace.** Your library should expose one name. One. `window.something =
{}`.  That's it. Everything you expose should be a property of the
`window.something` object. (No, `window.something` cannot be a function, that's
cute but annoying in practice.) `npm` enforces this, and if you're clever, you
can write code that's a valid `npm` module *and* browser-worthy module. Read
about
[IIFE](http://en.wikipedia.org/wiki/Immediately-invoked_function_expression) if
you're confused.

**Don't force callbacks.** If it doesn't actually do anything asynchronous,
don't add a callback. Just *return* the answer. That's what the return keyword
is for.

**Put thought into your argument convention.** If your functions are generally
monadic or dyadic, just accept positional arguments. Yes, it's ok to write code
like:

    function (a, b) {
        doSomethingWith(a || "default", b || "default");
    }

and yes, it's ok to have users call a function with `function(null, "cow")` to
default a positional argument that isn't the last.

Avoid the `arguments` keyword like the plague. If you need variadicity, accept
an array as an argument. Variadicity causes confusion. And people who get
addicted end up writing functions that do different things depending on how
many arguments were passed. Scary, scary, scary.

It's also perfectly ok to accept just one argument, an object, if you need a
dozen keyword arguments.

**Be quiet.** When your library runs in production, nobody should notice it. No
console messages or "warnings", no twiddling with the DOM to include a little
banner.

**Documentation is not advertisement.** Once I've committed to using your
library, you don't need to continue explaining how it's a revolution in
generative fluid modern flat reactive magical material-inspired skeuomorphic
silky-smooth user interface. Just tell us how to use the primitives. If there
are concepts to be learned before using your library, explain them outside the
API reference.

**If you're strictly on nodejs, prefer the provided Streams to whatever
homegrown thing you're inventing right now.** Streams are tempting to
reinvent-the-wheel, because they're a pretty idea which isn't terribly
difficult to implement with your own shiny interface. Don't do it. This extends
to other things, too: XHR wrappers, querySelector reimplementations, and
event-emitting architectures are just a few of the major offenders.

**Document bugs.** No, I won't lose faith in your module if there's a
one-in-a-million corner case as long as it's documented. I will lose faith if
there's a one-in-a-zillion corner case whose only documentation is a comment
saying "ill fix thiss l8r". Similarly, don't introduce undocumented features.
At the very least, say "this feature is experimental and SHOULD NOT be used in
production".

**Don't force dot-chaining.** Yes, it's useful in some places. Dot-chaining is
great for *transforming* values in a sequence. It makes no sense when there are
sequential actions that have side-effects. JavaScript has built-in support for
that kind of thing: it's called the semicolon (`;`).

Bad:

    element
        .turnRed()
        .then()
        .ifYouFeelLikeIt()
        .and()
        .theStarsAlign()
        .changeSize()
        .do()

Good:

    element.turnRed();
    if (element.youFeelLikeIt && element.theStarsAlign) {
        element.changeSize();
    }

Good:

    data
        .map(transformation)
        .filter(selection)
        .reduce(action)

The problem with dot-chaining is that it locks a lot of important functionality
behind weird objects.

**Stop creating boilerplate creators.** If you're embarking on a new
million-dollar company, you want to start from scratch and do things right,
making sure you understand everything on your website. If you're writing a toy
demo for a 24 hour hackathon, you don't need a full-featured MVC framework. You
need to learn CSS.

Corollary: throwing Bootstrap at a problem doesn't fix it. Bootstrap causes
slow, janky websites. There was a time when it was shiny. Now it's dull and
mundane.  Put some effort into making your website look like "yours". And
remember, there's absolutely nothing wrong with the default OS-provided buttons
that designers at Apple have spent ages perfecting. For that matter, I feel
there's nothing wrong with Times New Roman. It's just that everyone feels the
need to show that they know how to change the font face.

**Don't write generic CSS.** Are you creating a set of pretty text box widgets?
Don't touch anything that doesn't have class `pretty-text-box`. Things that go
around setting global properties (even ones that *should* be set, like
`box-sizing`) are evil. Don't be that guy.

**Write generic CSS.** I might want to change the width of your
syntax-highlighting gutter. Don't make me edit your source code for that to
happen.

**Don't build plugin infrastructures.** Your code should be organized enough
for people to write helpers themselves. You shouldn't need to provide methods
to "register" an "extension". It almost always implies you're building a
cathedral.

---

The TL;DR version of this is that your code should be designed to cooperate
with others. People don't want frameworks to lock up all their hopes and dreams
in. They want small, useful tools so that they don't have to think about too
many details.

UNIX wouldn't work if it wasn't made of hundreds of awesome tiny programs. The
Internet should take a hint from that.
