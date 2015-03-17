As I look back on programs I've written, I almost always notice that the most
successful are the hacks. The ones whose source code is spaghetti, the ones
which consist of patches upon patches, and *not* the ones where I painstakingly
mapped out a beautiful API.

I speak of such monstrosities as `alchemy`, an IRC bot to play [Little
Alchemy](https://littlealchemy.com) collaboratively in IRC. `alchemy.py` is
almost fully contained in a single while loop, and important game functions are
nested so deep that they must be indented more than 80 characters to be valid
Python. `alchemy` might be one of my most successful software projects if
measured by total amount of happiness brought to users.

Speaking of IRC bots, the `jokebot` skeleton code introduced in a previous post
is probably the most-forked of my projects, giving rise to 3 derivative bots
within a week of its first commit. `jokebot` was written with no heed for
efficiency, and so the unpatched `jokebot` was a big fat memory hog.

I also speak of `bouncy`, a screensaver I wrote over the course of a couple of
hours for no good reason, which has been adorning my mom's Mac every 10 minutes
for the past two years. I have no idea what `bouncy`'s source looks like, but
I do recall abusing nested `NSArray`s because Xcode didn't let me create a new
class.

I speak of Snapin8r, which began as a Pythonic mess, was then ported to
JavaScript line-by-line, and then heavily patched as bug reports rolled in.
Most things are handled by one giant if/elif chain in a for loop.  Again,
Snapin8r is used by a disproportionately large number of people considering how
shaky the entire thing is.

And I speak of [miscellaneous](http://scratch.mit.edu/projects/10490996/)
hacked-together Scratch [projects](http://scratch.mit.edu/projects/1322628/)
that have, over the years, accumulated dozens of "remixes" as people ran into
them and used their code for amazing derivative works.

I do *not* speak of things like `nearley`, which despite hundreds of commits by
several authors, has only one legitimate dependency on `npm`. Or, for that
matter, any of my other well-organized projects on Github. 

---

Perhaps there's a reason for this. As logical people, programmers instinctively
build
[cathedrals](http://www.catb.org/~esr/writings/cathedral-bazaar/cathedral-bazaar/cathedral-bazaar.ps),
not bazaars. "If we get it right the first time," we say, "we'll have a good
foundation and won't have any showstopper bugs." And then we spend a few weeks
building up these "foundations" and then release monoliths.

But, as I've observed, that's not how effective software gets created. The
best software gets used as it's being developed. The way it's used affects its
development, so that instead of just a theoretical curiosity designed to be
perfect and modular, the program solves real-world problems from day 1. The
best software begins as a funny IRC bot or hackey Bash script.

And so the lesson I want to teach myself by posting this post is that the most
important thing isn't to pick the perfect APIs, tools, libraries, frameworks,
algorithms, and languages. The most important thing is to just start writing
code.

This is *really* hard.

Even selecting a language for a new project is hard. I want my project to be
fast, but C is too low-level. Scheme would probably be the best choice
algorithmically. Should I use Racket or Chicken? Racket seems more documented,
but it doesn't compile to native code cleanly. Chicken has yucky documentation,
and I don't like Chicken's package manager. Maybe I should do it in Python? But
I hate Python.  Hang on, I've been meaning to learn Haskell for a while, now.
Wait, no, I/O in Haskell is hard, and I'll need a good POSIX interface for this
project.

Speaking of which, how should I accept input? Stdin? File name? In what format?
JSON? YAML? I don't know how to parse JSON in Scala yet. Actually, maybe my
program would be better as a service hosted over HTTP?

How about command-line arguments? Does Rust have a good option parser? Will I
have to write it myself? I probably won't be able to write an option parser
that's as efficient as industry-standards. Parsing is hard. Maybe I should use
JavaScript; I already know how to use nomnom.

But if it's in JavaScript, I can bypass all this and create it as a sleek,
intuitive, and beautiful GUI in the browser. Then again, I want my project to
be fast...

---

I think I've made my point: you can spend as long as you wish trying to choose
the right tool. The truth, of course, is that there is no "right tool". In
fact, whatever tool you pick, you're going to hit a limitation at some point.
It's reality. So instead of spending ages choosing the right tool, just pick
the one that *feels* right and get some code written. Imperfect code is always
more useful than no code. You should think about interfacing and efficiency
*second*.

Ok, fine, I'm going to regret saying that. There's a very good argument to be
made for thinking about the architecture of a project before starting on it. It
leads to clean, maintainable code. It minimizes the amount of refactoring
drudgery.

But I think all those things are secondary to actually having a working
prototype. Yes, you're going to run into painful distribution issues--it's
happened to me, and it was annoying enough to make me give up on the project.
But the open-source world came to the rescue, and someone forked and continued
it. What matters is that I put my idea into code and gave it to the world.

So my promise to myself--as of publishing this post--is to spend less time
debating tools and more time using them. This means forcing myself to
consciously use imperfect tools, which might cause mild internal bleeding.
Let's see how long I survive.
