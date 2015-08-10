A lot of script kiddies, myself included, take a lot of pride in loathing
statically typed languages and being "purists". But I've been doing some
reading about static typing (after realizing that many of the hackers I
respect are type-safety-fanatics) and I've realized that a lot of the reasons
that we have for hating type-safe languages aren't truly valid.

Not that I'm converted. I'm still a firm believer that types belong to objects,
not to variables. But for the benefit of people who are still making a choice,
here are some of my misconceptions about type safety.

This post isn't meant to persuade you one way or the other, because if you're
going to join the Dark Side, it's probably too late already.

### Misconception 1. Type-safe means hardcore imperative OOP.

This probably stems from the huge popularity of Java, which has linked static
typing to aggressively object-oriented imperative programming. When I took AP
Computer Science, the distinction between Types and Objects was not made
clearly enough.

You can have OOP without static typing. There's Pythonic duck typing:

> In other words, don't check whether it IS-a duck: check whether it
> QUACKS-like-a duck, WALKS-like-a duck, etc, etc, depending on exactly what
> subset of duck-like behaviour you need to play your language-games with.
>
>   (Alex Martelli, [source](https://groups.google.com/forum/?hl=en#!msg/comp.lang.python/CCs2oJdyuzc/NYjla5HKMOIJ))

There's Self's prototypical inheritance, where all you have are objects (which
are pretty close to JavaScript Objects and Lua Tables when it comes to
implementing an OOPey system). There's even Scheme OOP, with impure dispatch
functions as described in SICP.

But you can also have type-safe functional languages without an OOP framework
around it. The best examples of these are Haskell and ML, though I'm sure there
exist others. Haskell is as functional as it gets (arguable more so than
Scheme, because it [absolutely prohibits side-effects](http://xkcd.com/1312/),
i.e.  doesn't have `set-car!`).

So you don't need to give up functional code to embrace type safety.

### Misconception 2. Type-safety causes extreme abstraction and code inflation

Another one that I [attribute to
Java](http://geek-and-poke.com/geekandpoke/2014/1/2/games-for-the-real-geeks-part-2).
Though it's [completely
possible](https://github.com/EnterpriseQualityCoding/FizzBuzzEnterpriseEdition)
to be obnoxious about your types, for the most part it's also completely
possible to write reasonable-looking flat-is-better-than-nested code. Just like
you can write C programs, for loops and all, in Scheme, and they'll work, but
that's a blatant abuse of recursion.

Looking at lots of Haskell code, it's pretty clear that the levels of
abstraction you choose to implement are not directly correlated with the way
you use or misuse the type system.

### Misconception 3. Type-safety is a hack added onto languages to discipline programmers. It's just another lint.

We're generally told that aside from some some cases where runtime typechecks
are needed (or C, where types determine memory usage), most of the time
typechecking information is just discarded when you actually compile the code.
In that sense, they seem to add little more value than well-placed, meaningful
comments.

And while that's an acceptable way to look at it, it's certainly worth
realizing that type theory is an established branch of computer science that
comes dangerously close to math. It is nontrivial to come up with a type system
that is "provably correct", that is, a type system that is liberal enough to
accept programs that get stuff done, but conservative enough to reject programs
that do bad stuff (like access fields that don't exist).

For example, consider functions that accept an Animal as input and return a
Truck as output. Is this a superclass of functions that accept Parrots as input
and return Vehicles as output? Or a subclass? How about classifying recursive
tuple types (such as `LinkedList<T>`, which could potentially be of type
`Tuple(T, LinkedList<T>)`)?

Even though type-safety is like a lint, it's a very advanced, deep lint that
occasionally catches subtle bugs. It's a sanity check that prevents you from
coding if it deems you insane.

### And I care because...

...because even though type safety is the enemy, it's important to realize why
it's so popular. In the world of CS, it's important to Hoover up as many new
ideas as you can, even if you don't agree with all of them.

> If you know yourself but not the enemy, for every victory gained you will
> also suffer a defeat.
>
> --- Sun Tzu, *The Art of War*, III-18.
