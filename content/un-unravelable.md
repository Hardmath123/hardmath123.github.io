Say what you will about _The Big Bang Theory_, it has its moments, and this is
one of my favorites (watch it to the end of the clip!):

<iframe width="560" height="315"
src="https://www.youtube-nocookie.com/embed/MsawieizDeE?start=210"
frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope;
picture-in-picture" allowfullscreen></iframe>

Putting aside the wonderful meta-dramatic irony of this moment, the word
"un-unravelable" is the kind of thing you can sit and think about for hours. I
know because I have.

See, you might think that the "un-" prefixes cancel, such that "un-unravelable"
means the same thing as "ravelable." This is kind of like how
"un-unforgettable" probably means "ordinary." And indeed, [Wiktionary
agrees](https://en.wiktionary.org/wiki/un-unravelable) with this assessment,
suggesting instead "ravelable" as the "simpler and more immediately logical
choice."

But clearly that's not what Dr. Cooper meant in this case! "Ravelable" means
_can be raveled_ whereas Dr. Cooper meant _cannot be unraveled_, which are at
least intuitively separate concepts. So what's going on?

First of all, we need to figure out what "ravel" means: it
[means](https://www.websters1913.com/words/Ravel) to entangle. Something that
is "raveled" is entangled and knotted like the HDMI cords behind your cable
box. The sleep that Macbeth murders is the "sleep that knits up the raveled
sleeve of care" (2.2.37). Actually, that's not the full story. "Ravel" _also_
means to _disentangle_, making the word a so-called "Janus word" (read more at
[Merriam-Webster](https://www.merriam-webster.com/words-at-play/words-own-opposites)).
But let's stick with the former definition for the moment.

Okay, so now we can start tacking on prefixes and suffixes. But we have to be
careful!  The dynamics of affixes are tricky --- the order in which we tack
them on matters.

For example, "ravel-able" would mean _can be entangled,_ so spaghetti is
ravelable. Then "un-ravelable" could mean _cannot be entangled,_ so ravioli is
unravelable.

On the other hand, "un-ravel" would mean _to disentangle,_ so Sherlock unravels
mysteries. Then "unravel-able" could mean _disentanglable,_ so the mysteries
Sherlock solves are unravelable (by him, at least).

To summarize:
* un+(ravel+able): there is _no_ way to ravel it
* (un+ravel)+able: there _is_ a way to unravel it

Alas! The associative property has broken down! This means we need to examine
each of the five possible paranthesisifications of "un+un+ravel+able"
separately ([why five?](https://en.wikipedia.org/wiki/Catalan_number)).

Here they are:

1. **(un+un)+(ravel+able)** and
2. **((un+un)+ravel)+able** are easy: neither of them typecheck, because
   "un+un" is meaningless.
3. **un+(un+(ravel+able)):** "ravelable" means _can be entangled,_ so
   "un-ravelable" means _cannot be entangled,_ and thus "un-unravelable"
   means _is not such that it cannot be entangled,_ i.e. _can be
   entangled._ For example, your new favorite organizational scheme might seem
   perfect at first, but after a few weeks you will find that no scheme can
   fend off the entropic tendencies of the universe, and that your files are by
   nature un-un-ravelable.
4. **(un+(un+ravel))+able:** "unravel" means _disentangle,_ so "un-unravel"
   means _re-entangle_ (by analogy to "un-undo" meaning "redo") and thus
   "ununravel-able" means _re-entanglable._ For example, a jigsaw puzzle that
   you mix up again after solving is ununravel-able.
5. **un+((un+ravel)+able):** "unravel" means _disentangle,_ so "unravel-able"
   means _can be disentangled,_ and thus "un-unravelable" means _cannot be
   disentangled._ For example, Dr. Cooper's web of lies is un-unravelable.

So what's really going on here is that the prefix _un-_ has many faces (a Janus
prefix?); it reverses verbs and negates adjectives. Perhaps this is clearer in
the language of first-order logic, where _-able_ introduces an existential
quantifier over _a way to do the thing_ (and thus do(w, x) does w to x).

1. N/A
2. N/A
3. **(un+(un+(ravel+able)))(x)** means &not;&not;&exist;w. raveled(do(w, x))
4. **((un+(un+ravel))+able)(x)** means &exist;w. &not;&not;raveled(do(w, x))
5. **(un+((un+ravel)+able))(x)** means &not;&exist;w. &not;raveled(do(w, x))

Only (5) puts an odd number of negations outside the existential quantifier,
flipping it to a universal quantifier, and expressing that you _cannot_ unravel
whatever needs unraveling.

Why doesn't this effect happen with "un-unforgettable"? It's because "unforget"
isn't a common word, and so we reach for interpretation (3) rather than (5).
Though now that I think about it, "unforget" is an excellent replacement for
"remember."
