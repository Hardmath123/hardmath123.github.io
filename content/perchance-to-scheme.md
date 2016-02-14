Scheme, they say, is an idea rather than a language. But what does that mean?
Is Java an idea or a language? C?

When you write code in *Java* or *C*, you expect it to work, more or less, even
if you use a different compiler. `gcc` and `clang` are generally compatible.
Similarly, you can run a Java program in Hotspot, JRockit, Kaffe, or J9 and it
should be fine. You can compile the Java program with `javac` or `gcj` and it
should work the same (one might be slower than the other, though).

This is because C and Java have *specifications*. There are long documents
describing *exactly* what the languages should do, and someone writing a
compiler needs to follow those specifications. The implementation details---how
a feature works---is up to them, but not any of the actual language design.

Scheme, on the other hand, is very loosely specified. This is a good thing: the
core language is so small that the entire
[standard](http://www.schemers.org/Documents/Standards/R5RS/r5rs.pdf) fits on
about 50 pages ([Java's
specification](https://docs.oracle.com/javase/specs/jls/se7/jls7.pdf) fits on
644). Additional helpful features are included in "Scheme Requests for
Implementation" or SRFIs, which are not a part of the standard but are useful
for programmers---things like common list operations.

It's not nebulous, it's simply minimalist. This is why Scheme is more of
an idea than a language.

As a result, implementing a Scheme compiler gives you a lot more freedom in how
you want your language to look, while still calling it a "Scheme dialect". You
can choose to make square brackets legal delimiters, or you could choose not
to. You almost always have to supply your own I/O primitives like "prompt for
input" or "open a socket".  Module systems and importing are up to you.

And so Scheme programs are usually *not* compatible across implementations.
With so many hundreds of Scheme dialects out there, it's kind of overwhelming
for a first-time Scheme programmer to pick a dialect and actually get started.

I'm a Scheme dialect nerd. I probably have more Scheme dialects installed than
most people have games on their phone. Here are my opinions on which Scheme
dialect to use. Rather than grouping by use-case, as guides such as [this
one](https://wingolog.org/archives/2013/01/07/an-opinionated-guide-to-scheme-implementations)
do, I grouped by language.

### Racket

[Racket](http://racket-lang.org) is, in a word, academic. It started off as
*PLT Scheme*, which was essentially a research group that happened to produce a
really good pedagogical Scheme dialect which they used for a lot of their
research.

Racket has an impressive standard library and a decent module system. Its POSIX
interface is a bit wanting, though. For example, you can't send a signal to a
process yet (technically, I have a PR open for this
[here](https://github.com/racket/racket/pull/961)). This is partly because
Racket aims to be generally platform-independent, and so doesn't necessarily
want to implement a whole bunch of Unix-specific features in order to appeal to
Windows users. This is either a good thing or a bad thing, depending on your
use-case.

Racket's FFI is iffy. Writing C extensions is kind of tricky.

There are a couple ways to distribute your Racket program: you can have users
install Racket and download the source, or you can use `raco` to compile an
executable that bundles Racket's runtime system with compiled bytecode. Neither
way seems perfect to me, but, well, they work.

Racket comes with a lot of frills. There's a GUI engine, an IDE (which isn't
great, but isn't awful either), and primitives for manipulating images and web
servers and whatnot. It also has copious amounts of documentation, and it ships
with its own documentation tool called Scribble (which is documented in
Scribble). Racket is also a "language lab": it gives you the tools to create
your own programming languages built on top of Racket infrastructure (for
example, Typed Racket, the type-safe dialect of Racket, is written in Racket).

Racket has a nice community and mailing list archives/StackOverflow answers for
help. It's also the recommended Scheme dialect to use if you're learning or
teaching Scheme/SICP.

If you're still lost at the end of this article, stop thinking and go with
Racket and you will be fine.

### Chicken

[Chicken](http://call-cc.org) is sort of the opposite of Racket. It's small
(R5RS only), but it has a fantastic POSIX API. Chicken implements the R5RS
Scheme standard, which stands for the *Revised Revised Revised Revised Revised
Report on the Algorithmic Language Scheme*.

Its website is `call-cc.org` because the Chicken devs are super-proud of how
Chicken handles continuations: it uses the amazingly-named [Cheney on the
MTA](http://www.pipeline.com/~hbaker1/CheneyMTA.html) strategy.

Continuations, by the way, are one of the
[coolest](http://matt.might.net/articles/programming-with-continuations--exceptions-backtracking-search-threads-generators-coroutines/)
Scheme features.

Chicken has a decent number of libraries, and it's really easy to turn a C
module into a Chicken module.

Chicken compiles to C, so to distribute, you can either distribute binaries or
C sources which the user can build without installing Chicken. Super-easy.

### Clojure(Script)

ClojureScript is a compiler from [Clojure](http://clojure.org) to JavaScript
(Clojure originally targeted Java). It is *not* a Scheme dialect, not does it
feel like one. It's a LISP dialect.
[Here](http://c2.com/cgi/wiki?LispSchemeDifferences) are some differences
between LISP and Scheme, if that interests you.

Personally, I don't like it on a matter of principle: I don't like things that
compile to JavaScript. It doesn't seem like anything you really need to write
better code. They say JavaScript is Scheme in C's clothing, anyway, and I do
agree with that to some extent.

Same holds for BiwaScheme, Spock (written by the Chicken developer), the
(unmaintained) WhaleSong Racket-to-JS compiler, and anything on
[this](https://github.com/jashkenas/coffeescript/wiki/List-of-languages-that-compile-to-JS#lisp-scheme)
list.

### Chez Scheme

The [Chez Scheme](http://www.scheme.com) compiler isn't free, and its website
lives on a COM domain. Take from that what you will.

That being said, it's reputed to be ridiculously fast. I have never met a Chez
Scheme user, but maybe I'm in the wrong crowd.

### Guile Scheme

[Guile](http://www.gnu.org/software/guile/) is a GNU project, which means it
has all sorts of ideals and mission statements and declarations that make it
seem like the paragon of freedom.

In short, Guile is the Scheme you want to use in "embedded" form. That is, you
can stick a Guile interpreter in a C application in order to control it without
having to deal with C. One of the canonical examples of this is the [turtle
graphics
example](http://www.gnu.org/software/guile/docs/guile-tut/tutorial.html), in
which you write a graphics display in C, and then let the user control it with
Scheme, which is easier. Similarly, the WeeChat IRC chat client lets you write
extensions in Guile (for example, an extension that automatically URL-shortens
long URLs before you send them).

Guile can both interpret and compile Scheme, it has good documentation, and
it's backed by GNU so you can expect maintained code (Guile is used by other
mature GNU projects such as `gdb`, so they're invested). Also, Guile is written
in Guile, and the LilyPond music formatting program is written in Guile.

### Emacs Lisp

You only use Emacs Lisp if you, well, use Emacs, just like how you only use
VimScript if you use Vim.

### Anything else

Before choosing any other Scheme implementation, it's probably worth your time
to make sure it really does offer something more than the dialects I listed
above. Make sure it has an active community that can help you when you run
into problems, and make sure you can find code written by other people in that
dialect of Scheme. A good quality test is to see if it implements any SRFIs.

Then, hack away.

---

And now, a brief word on the proliferation of Scheme dialects.

Part of the problem is that one you pick a Scheme implementation, you're almost
always "locked in": you can't easily migrate to another. So people tend to just
build their own Scheme environment that they can control.

Another part is that every CS student and their pet dog has probably written
some approximation of a Scheme interpreter (possibly as a course project), so
the Babel effect kicks in and creates a plethora of implementations of choose
from. I'm guilty of this.

It's just so *easy* to write a Scheme implementation. In a way, Scheme is a
virus... but that's the subject of a future post (or you could just read *Snow
Crash* by Neal Stephenson and stick "programming" before every instance of
"language").

An upside of this, though, is that as the Scheme virus infects the programming
language community, it injects the Functional Programming DNA everywhere. Once
you're immune to Scheme (by reading SICP), you'll thrive in any such
environment, be it JavaScript, Scala, Haskell, or Ruby.

Oh, and one last thing. I feel it's obligatory at this point for me to say,
please don't spend too much time researching Scheme dialects. Just pick Racket
and start coding.
