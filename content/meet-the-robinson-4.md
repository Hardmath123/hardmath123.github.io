Welcome to the final installment of *Meet the Robinson*.

We left off [last time](meet-the-robinson-3.html) with a complete but slow
theorem-proving algorithm for first-order logic, as well as a promise of a
faster algorithm. The faster algorithm depends on a concept called
"unification", so let's talk about that first.

- No, this has nothing to do with Otto von Bismarck. Nevertheless, try to come
up with a good Germany pun here if you can.

---

Propositional resolution involved finding a pair of identical propositions in
opposite polarities (one in "positive" and one in "negated" polarity). In
first-order logic, though, we can do better. We can find pairs that have the
same "shape".

- Explain how `Wrote[X, hamlet()]` and `Wrote[shakespeare(), Y]` are the same
"shape".
- Come up with a rigorous definition of "same shape" which involves replacing
some (universally quantified) variables to make the predicates identical.

The process of substituting variables to make two predicates identical is
called *unification*. If you've worked with Hindley-Milner type inference, you
know what unification is---it's the stage where you figure out what the type
variables you spawned expand to.

The unification algorithm isn't hard to implement at all. It tells you whether
two predicates unify or not, and if they do unify, it comes up with a
substitution for each variable that can be applied to make them identical.
Substitutions replace a variable with either a function or another variable.
People talk about unification in terms of "solving equations" of functions and
variables, if that makes more sense to you.

In particular, unification algorithms come up with the *most general* such
unifier, so variables that don't need to be substituted are left as-is.

 - Which variables are left unsubstituted in the unification of `P[X, Y]` and
 `P[X, f(Z)]`?

Unification algorithms are covered in detail in
[SICP](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-29.html#%_sec_4.4.2).
Most people use the algorithm by Martelli and Montanari. Peter Norvig has
published a correction to the algorithm. His paper actually has a very succinct
and clear description of the algorithm, and can be found on his site
[here](http://norvig.com/unify-bug.pdf).

- Explain why `P[X]` and `P[f(X)]` don't unify (why do we need the "occurs
check"?). Come up with a way to relate this to (1) the Y combinator, and (2)
finding the roots of a polynomial.

---

And now back to theorem-proving.

Unification allowed Robinson to prove the *lifting lemma*, which says that if
we have a valid resolution step at the propositional level (with ground
clauses), then we *must* have a valid resolution at the first-order level. For
example, we can unify `P[a(), b()]` and &not;`P[a(), b()]`. Since the former is
a ground instance of `P[X, Y]` and the latter is an instance of &not;`P[a(),
Y]`, we deduce that there must be a resolvent of `P[X, Y]` and &not;`P[a(),
Y]`. One such resolvent is `P[a(), Y]`.

The lifting lemma also guarantees that the resolvent of the ground instances is
an instance of the resolvent of the first-order clauses. In this example, note
that `P[a(), b()]` is an instance of `P[a(), Y]` because if you substitute
`b()` for `Y` in the latter you get the former.

- Use the lifting lemma to show that `P[a(), b(X), Z]` and &not;`P[X, b(Y),
c(X)]` have a resolvent. Find the ground instance and the first-order resolvent
and show that the ground instance is an instance of the first-order resolvent.
- Convince yourself the lifting lemma is true using what you know about
unification.

The lifting lemma lets us "lift" propositional resolution to first-order
resolution. Instead of checking if two terms are equal as in propositional
resolution, we check if they unify, and if they do, we apply the substitution
to the resolvent. Thus, we end up "iteratively" building up the ground instance
at each resolution step. This is much more efficient than the Davis-Putnam
algorithm, which had to guess the ground instance out of the blue.

Here's an example. Suppose we had (`P[a(), Y]` &or; &not; `A[X]`) and (`A[X]`
&or; &not;`P[X, b()]`). First, we note that `P[a(), Y]` and `P[X, b()]` appear
in opposite polarities in the two clauses, and that they unify. The
substitution is `X` becomes `a()` and `Y` becomes `b()`. Applying this
substition yields (`P[a(), b()]` &or; &not; `A[a()]`) and (`A[a()]` &or;
&not;`P[a(), b()]`). Resolving out that term, we have `A[a()]` and
&not;`A[a()]` which clearly resolve to the empty clause, which completes the
proof.

- Use first-order resolution to prove that if (&forall; `X`) `P[X]` then
(&exist; `Y`) `P[Y]`. Then, translate your proof to English.
- If we try to prove something that is false, then the set of sentences
(knowledge base and negated goal) is satisfiable---it is impossible to find a
resolution-style contradiction because there are no contradiction. In this
case, is the resolution-refutation procedure guaranteed to terminate? What
about if we were still using propositional logic?

Hilbert's *Entscheidungsproblem*, posed in 1928, asked whether there was an
algorithm that would tell you whether a first-order set of sentences was valid
or not (he believed that there was!). Alonzo Church used the lambda calculus to
prove that there was not, in fact, such an algorithm. That same year, Turing
used Turing machines to prove the same thing by reducing the halting problem to
the Entscheidungsproblem. That is, they found a way to encode programs as
statements in first-order logic such that asking whether the statements are
provable is the same as asking whether the programs terminate.

- Say "Entscheidungsproblem" out loud three times.
- Very carefully clarify the difference between G&ouml;del's Completeness
Theorem and the Church-Turing Thesis (i.e. answer to Entscheidungsproblem).
- Look up the approximate timeframe of these discoveries. Then, look up when
the first Turing complete computer was built. Peter Landin was one of the first
people to realize that the lambda-calculus was useful in computer
programming---over thirty years after Church first posed the lambda-calculus.
- Give two reasons why a lot of information on these subjects can be found on
online philosophy encyclopedias.

---

A classic logic puzzle goes as follows:

> Anyone who owns a dog is an animal lover. No animal lovers kill cats. Either
> Jack (who owns a dog) or Curiosity killed the cat. Who killed the cat?

This isn't a "proof" as such, it's a question. It turns out that the same
tricks work for answering questions (or "querying").

Suppose we are asking for an `X` such that `Killed[X, cat()]`. If we were
trying to prove something, we would negate our goal and add it to the knowledge
base. Since we're querying, we need to make a small modification. We add this
sentence to the knowledge base: `Answer[X]` &or; &not;`Killed[X, cat()]`. Now,
rather than looking for empty clauses, we look for clauses which only contain
one predicate, which is `Answer[*]`.

Once we extract the `X` from the `Answer[*]` predicate, it's easy to see why
it must be the answer. Simply re-run the theorem prover asking it to prove that
`Killed[X, cat()]` (but substitute in the actual value of `X` you got). Since
the proof is basically the same as above (ignoring the `Answer[*]` predicate),
it must succeed. So, we know that our answer must be "correct" (in the sense
that it is consistent with the knowledge base).

Let's work through a small example. Suppose we have `Wet[water()]` and we want
to query for an `X` such that `Wet[X]`. We construct the answer clause
`Answer[X]` &or; &not;`Wet[X]`. Then, we resolve against `Wet[water()]`,
unifying so that `X` is `water()` to get `Answer[water()]`.

- Could you have multiple "correct" answers? Come up with a knowledge base
where a query has multiple possible correct responses. How do you know which
response the algorithm will output?
- Solve the Curiosity puzzle above using first-order resolution with an answer
predicate.
- Here's another such puzzle:
> Animal lovers love all animals. At least one person loves every animal lover.
> Nobody loves a person who has killed an animal. Either Jack (who loves all
> animals) or Curiosity killed Tuna, who is an animal. Who killed Tuna?
- Reason through it in English and figure out who killed Tuna. Write down your
reasoning somewhere.
- Translate each fact into first-order logic.
- Resolution-refute to find out who killed Tuna.
- Translate your refutation procedure into English.
- Compare this reasoning with the one you did earlier.

---

All texts on resolution theorem proving talk about heuristics, so I guess I
will too. But I won't spend too much time on it. There are a few ways to be
"clever" about how to pick which clauses to try to resolve. The first one is
*unit preference*, which simply says clauses that have a single predicate are
a good choice because if the resolution *does* work, you're done. You probably
use this heuristic without even knowing it: you're likelier to try to resolve
shorter clauses because it "feels" like a reasonable choice.

The second one is the *set of support*, which says that you can divide up your
clauses into the axioms (which are supposed to be consistent within themselves)
and the stuff to be proved (which should have a contradiction with the axioms).
Then, you make sure you always use a sentence from the latter set when you
resolve, because if you use two statements from the set of axioms, you won't
get a contradiction because they're supposed to be consistent among themselves.

In other words, this is the heuristic form of "if you're stuck, check to see if
you have used all the information in the problem". If you're too aggressive
with the set-of-support strategy, you might miss an important resolution and so
the algorithm might become incomplete. Use responsibly at your own peril.

The last is called *subsumption*, which is basically spring cleaning. Every
once in a while, clean out duplicate clauses. Be clever, so if one clause
"subsumes" another (i.e. one is a ground instance of a more general clause)
then delete the more specific one. Fewer clauses means faster resolution, but
subsumption itself can get kind of slow.

- How can you detect if one clause subsumes another? Come up with a specific,
rigorous definition.

And that's it. I don't know why this is such a big deal, but these three things
always show up on every piece of literature on resolution-refutation theorem
proving. Maybe it's because Russell and Norvig covered them in their textbook
and everyone else thought they were really important.

---

One last thing we need to talk about: equality.

> Euclid's first common notion is this: Things which are equal to the same
> things are equal to each other. That's a rule of mathematical reasoning and
> its true because it works - has done and always will do. In his book Euclid
> says this is self evident. You see there it is even in that 2000 year old
> book of mechanical law it is the self evident truth that things which are
> equal to the same things are equal to each other.
> -- *Lincoln* (2012)

Our theorem prover doesn't support equality out-of-the-box. That is, we can't
tell it that `father(father(X))` is the same as `grandfather(X)`, and so those
two functions are interchangeable.

We can, of course, write our own equality axioms (as we did for the Peano
arithmetic above).

The issue is that we then need to also define the "replacement" axiom for every
single predicate: `Equal[A, B]`&and;`P[A]` &rArr; `P[B]`.

- Relate this to why we can't do induction in first-order logic.

The solution is to use the *paramodulation rule*, which is an additional
inference rule just like resolution is. It says that if you have a clause with
a term that contains some subterm `t` and you also have a clause that contains
`T`=`U` where `T` and `t` unify, then you can replace `t` with `U`, apply the
substitution from the unification to *both* clauses, and then join them
together, taking out the equality statement.

For example, given `P[g(f(X))]` &or; `Q[X]` and `f(g(b()))`=`a()` &or;
`R[g(c)]`, we can derive `P[g(a())]` &or; `Q[g(b())]]` &or; `R[g(c())]`.

- What was the unification here? What was the resultant substitution?
- Convince yourself that the paramodulation rule is true.
- Write the paramodulation rule in "fraction form".
- Do we still need the equality axioms (which we talked about when discussing
the Peano axioms)?

In his thesis, Herbrand showed that you don't need equality axioms to prove
theorems if your knowledge base doesn't have any equality statements in it.

---

...and that's it. That's actually all there is. Combining resolution,
unification, and paramodulation let us build the theorem prover that Robinson
used to prove the Robbins conjecture.

So I guess now it's time for me to summarize.

If you've stayed with me on this journey, you've learned the basics of formal
logic, model theory, and proof theory. You've explored several famous theorems
in each field and seen (human-generated!) proofs of them. You've discovered how
math is rigorized. And, finally, you've seen some of the rich history of logic
and how it connects not just to various branches of math, but also to
subjects as abstract as philosophy and as practical as computer science.

- In what "universe" did the proofs covered in this series live? For example,
can the proof of the propositional compactness theorem be encoded in
first-order logic? Is it even legal to talk about a logic within that logic? Or
is it a bad case of "turtles all the way down"? Do we need to take something on
faith at some point, or are there fundamental mathematical truths somewhere?
What does this have to do with *cogito ergo sum*?

---

**Epilogue:** In a way, this isn't about having a machine that can prove
theorems. Like many things in life---marathons, pie-eating contests, and bank
robberies---I think the pleasure is more in knowing that you *can* do it than
in actually doing it.

Why? Because contrary to Rényi, mathematics is not about turning coffee into
theorems. An oracle that just tells you whether or not a statement is true is
useless; the real beauty is in understanding *why* it's true. A world where
math is an endless stream of abstract, intuition-less symbol-shunting is bleak.
Resolution-refutation proofs have no insight or motivation. They are completely
mechanical.

But then again, maybe that's exactly what we were going for.

---

I've admittedly been extremely lazy about citing my sources when writing these
articles. I have, however, diligently kept a list of links to resources I found
helpful. It feels appropriate to give them the last word here, so, in no
particular order, here they are:

- http://www.ki.informatik.uni-frankfurt.de/persons/panitz/paper/russian.ps (on
Haskell, a "Russian Room" analogy)
- http://src.seereason.com/chiou-prover/report.ps (more Haskell)
- http://www.cs.nott.ac.uk/~led/papers/led_bsc_dissertation.pdf (yet more
Haskell)
- http://www.cs.toronto.edu/~sheila/384/w11/Lectures/csc384w11-KR-tutorial.pdf
(on Skolemization and answering queries)
-  http://www.mathcs.duq.edu/simon/Fall04/notes-6-20/node3.html (inductive
proof of completeness of propositional resolution)
- http://www.doc.ic.ac.uk/~sgc/teaching/pre2012/v231/lecture9.html (an inside
look at the people of automated theorem-proving; change the "9" in the URL for
more information on AI)
- http://rmarcus.info/blog/2015/09/02/vulcan.html (Vulcan: the post that
started it all for me)
- http://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-825-techniques-in-artificial-intelligence-sma-5504-fall-2002/lecture-notes/Lecture9Final.pdf (on
paramodulation and semidecidability)
- https://books.google.com/books?id=xwBDylHhJhYC&pg=PA42&lpg=PA42&dq=demodulation+rule&source=bl&ots=WSHLneBzT0&sig=L-EuivNrxiG5GQjRRO40kiARO7o&hl=en&sa=X&ved=0CEYQ6AEwBmoVChMIydKL19K4yAIVCd9jCh1F6A9T#v=onepage&q=demodulation%20rule&f=false (more paramodulation)
- http://www.cs.cmu.edu/~fp/courses/99-atp/lectures/lecture29.html (yet more on
paramodulation)
- http://www.sciencedirect.com/science/book/9780444508133 (a book)
- https://drive.google.com/file/d/0B3DOH8_Gko0GRlRLek9ZZzlyOFk/edit (another
book)
- http://profs.sci.univr.it/~farinelli/courses/ar/slides/paramodulation.pdf
(even more paramodulation)
- http://www.cs.toronto.edu/~toni/Courses/438/Mynotes/page39.pdf (notes on
Herbrand's theorem)
- http://costa.ls.fi.upm.es/~damiano/teaching/emcl/cl_08_09/slides/05herbrand.pdf
(semantic trees and Herbrand's theorem)
- http://people.mpi-inf.mpg.de/~sofronie/lecture-ar-09/slides/lecture-4-june.pdf
(Herbrand's theorem and the lifting lemma)
- https://en.wikibooks.org/wiki/Logic_for_Computer_Scientists/Predicate_Logic/Resolution#Lemma_5_.28Lifting_lemma.29 (on the lifting lemma)
- http://lara.epfl.ch/w/sav08:compactness_theorem (nice proof of propositional
compactness)
- https://terrytao.wordpress.com/2009/04/10/the-completeness-and-compactness-theorems-of-first-order-logic/ (on first-order completeness)
- http://aima.cs.berkeley.edu (Russell and Norvig's textbook *Artificial
Intelligence: A Modern Approach*)
