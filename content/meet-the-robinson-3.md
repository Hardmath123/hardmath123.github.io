Welcome to today's edition of *Meet the Robinson*.

We left off the [previous article](meet-the-robinson-2.html) wondering if
there's any way to handle an infinite number of propositions with our
resolution-refutation scheme. It turns out that there is---we can "tame the
infinite" using **first-order logic**.

First-order logic is based on two ideas: predicates and quantifiers.

*Predicates* are just what your English teacher said they were, but (like most
things) they make more sense when you think about them in terms of computer
science. Predicates questions you can ask about the subject of a sentence.
They are, in a way, functions that return boolean values.

Here's an example. The predicate of *"Eeyore is feeling blue."* is *"is feeling
blue"*. We can use this to ask the question *"Is Eeyore feeling blue?"*. The
boolean function version is the function that takes an input (such as "Eeyore")
and tells you whether that input is feeling blue or not.

- You try it! What is the predicate in the sentence *"I walk this empty street
on the Boulevard of Broken Dreams."*?
- Use the predicate to ask a question.

The standard notation for predicates is, unfortunately, similar to that for
functions: we would write `isFeelingBlue(Eeyore)` to denote that predicate.
This turns out to cause some confusion, because first-order logic also has
*real* functions (more on that later). In this article, I'm going to use square
brackets for predicates and round ones for functions: `isFeelingBlue[Eeyore]`.
*Nobody else does this,* so don't blame me if this causes you any issues later
on in life. You have been warned.

Predicates are the propositions of first-order logic. So, we can join them just
like we joined propositions earlier: `smart[Alice]` &and; `funny[Alice]`. You
can have "empty" predicates such as `maryHadALittleLamb[]`, which correspond
directly to propositions. Predicates can also have multiple inputs, such as
`killed[Macbeth, Duncan]`.

- Show that everything we have so far can be modeled purely in propositional
logic, and that we can therefore reduce such sentences to CNF.

Predicates can operate on either "concrete" inputs like "Eeyore" (which we call
"constants") or "variable" inputs. Variable inputs are *quantified
generalizations*, which means that when you use a variable, you say that that
variable can be replaced by any constant and the statement would hold.

For example, the sentence "&not; (&forall; `X`) (`gold[X]` &rArr;
`glitters[X]`)" is read as "it is not true that all that is gold must glitter".
The symbol "&forall;" is read as "for all", and it *binds* the variable X. Why
do we need it? Depending on where the binding quantifier is placed, the
sentence can actually have a different meaning.

- Explain how the statement "(&forall; `X`) &not; (`gold[X]` &rArr;
`glitters[X]`)" has a subtly different meaning from what we had above.
- Which of the following is true: "Not all fingers are thumbs." and "All
fingers are not thumbs."?
- Why does the placement of the quantifier matter?
- Write a sentence in first-order logic that means "All fingers are thumbs" and
one that means "Not all thumbs are fingers".

---

The best way to think about quantifiers is not in terms of variables and
substitutions. Think about quantifiers as a way to select a subset of
predicates from an infinite set of predicates, and then apply some operation on
them. For example, "(&forall; `X`) `Foo[X]`" selects all predicates that "look
like" `Foo[_]` and then "ands" them together (we'll revisit the idea of "looks
like" in more detail later).

This isn't a rigorous definition, really, mainly because it's kind of tricky to
talk about "and-ing" together an infinite number of statements (why infinite?).
You also need to introduce the concept of a "domain of discourse", which
basically means "what can I fill into the hole?".

- Explain why the "and-ing" together means the same as "for all".
- What would be the English translation if we "or-ed" them together instead of
"and-ing" them together? We'll revisit this question later.

---

First-order logic also has *functions*, which have a misleading name because
you don't want to think of them as functions. Functions in first-order logic
are really more like prepositional phrases. For instance, `father(Luke)` means
"the father *of Luke*&rdquo;. You don't have to "define" these functions. They
are just ways of transforming data by adding structure.

Functions can be used anywhere variables and concrete values can. Together,
functions, variables, and constants are called *terms*.

- Explain how functions that take no inputs (niladic functions) are the same
as constants.

And example using functions is "(&forall; `X`) `winner[X]` &rArr;
`proud[parents(X)]`."

- Name one statement you can conclude from the above given that
`proud[parents(parents(Amy))]]`.

---

First-order logic is pretty powerful. We can express a great deal in it. To let
it sink in, we're going to quickly describe arithmetic in first-order logic,
using the *Dedekind-Peano axioms*:

1. "`isNaturalNumber[zero()]`&rdquo; says that 0 is a natural number.
2. The next three axioms describe what "equality" means (we will return to this
later):
    - &forall; `X` `Equal[X, X]`
    - &forall; `X` &forall; `Y` &forall; `Z` (`Equal[X, Y]` &and; `Equal[Y, Z]`)
      &rArr; `Equal[X, Z]`
    - &forall; `X` &forall; `Y` `Equal[X, Y]` &rArr; `Equal[Y, X]`
    - (These axioms are "reflexivity", "transitivity", and "symmetry",
      respectively. Techincally, these aren't exactly right because these
      axioms are meant to only hold if each variable `isNaturalNumber`. But
      this version is simpler.)
3. "&forall; `X` `isNaturalNumber[X]` &rArr;
`isNaturalNumber[Successor(X)]`&rdquo; says that the successor of all natural
numbers is also a natural number.
4. "&forall; `X` &forall; `Y` `Equal[X, Y]` &hArr; `Equal[Successor(X),
Successor(Y)]`&rdquo; says that the successor function is injective.
5. "&forall; `X` &not;`Equal[Successor(X), zero()]`&rdquo; says that no natural
number is before zero.

Peano had one more axiom, which represents *induction*.

- Explain why you can't do induction in first-order logic because you can't
quantify *predicates* (there *is* a kind of logic, called second-order logic,
that allows you to quantify over predicates...). The Peano Axioms without
induction are called the "Robinson arithmetic".
- To deal with such axioms, we use *axiom schemas*, which you can think of as
"preprocessors" that generate an axiom for each predicate. If you don't need
any axiom schemas, your logic is *finitely axiomatizable*.
- Axiomatize addition within the Peano axioms.

Perhaps you're unimpressed with this. Another powerful result of first-order
logic is Tarski's axiomatization of plane geometry (elementary Euclidean
geometry). Using a bit of magic (called "quantifier elimination" which does
exactly what you guessed), he showed that there exists an algorithm that can
prove any statement about plane geometry.

This *should* be impressive, because humanity has been tinkering with geometry
for at least two thousand years now. Suddenly being given a magic algorithm to
answer any question you'd like about geometry is amazing.

(What's the catch, you ask? The algorithm is *slow*. Impractically slow. As in,
two-raised-to-two-raised-to-n slow, also known as
will-not-terminate-in-your-lifetime.)

---

If you've read SICP (*The Structure and Interpretation of Computer Programs* by
Abelson and Sussman, [free
online](https://mitpress.mit.edu/sicp/full-text/book/book.html) and often
called the "Wizard Book"), you might be having flashbacks to their section on
logic programming: [section
4.4](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-29.html#%_sec_4.4).
This section describes a *logic* programming language, like Prolog. Prolog-like
languages operate on first-order logic and allow you to ask questions.

Here's an example of a rule in Prolog:

    male(charles).
    parent(charles, martha).
    parent(martha, agnes).
    grandfather(X,Y) :- male(X),
                        parent(X,Somebody),
                        parent(Somebody,Y).

Prolog allows you to then make queries such as `grandfather(charles, X)`, and
Prolog would go along and discovered that `X = agnes` is a valid solution.
This should remind you of database querying and nondeterministic programming
and a whole host of exciting ideas which are fun to explore. 

- Translate the above Prolog program to first-order logic statements (you may
need to read a bit about Prolog syntax).

---

Now that you're a first-order logic expert...

Remember G&ouml;del's Completeness Theorem? It said that all true statements
are provable in propositional logic. Turns out I lied. It's doesn't just hold
for propositional logic; it also holds for first-order logic. The rest of this
post will explain how that works.

"But hang on!" you say, "We just saw some arithmetic modeled in first-order
logic though, and arithmetic implies G&ouml;del's Incompleteness Theorem. How
can the Completeness and Incompleteness theorems live together peacefully?"

Good question. Turns out there are models besides the natural numbers that
satisfy the Peano Axioms, and so there are statements that are undecidable
because their truth value depends on which model is being considered. In other
words, the Completeness theorem applies only to sentences that are
*necessarily* true, while the Incompleteness theorem applies to sentences that
could be either true *or* false. Don't let the related names confuse you.

We haven't talked about proofs in first-order logic yet. For propositional
logic, our proofs had two components: reducing to CNF and resolution. It turns
out that we can extend each of these components to first-order logic.

The conversion of first-order logic sentences to CNF should be simple enough.
The only real complication comes from quantifiers.

- Recall the steps to convert a propositional logic sentence to CNF.
- Explain how quantifiers are only an issue in the part where you move negation
inwards.
- Extend De Morgan's laws to support quantifiers by introducing a new
quantifier:
    - What does &not; &forall; `X` `P[X]` really mean? What does "not
      everybody" went to the dance mean?
    - Explain how &not; &forall; `X` `P[X]` is equivalent to saying that there
      exists an `X` such that &not; `P[X]`.
    - We write "there exists and `X` such that `P[X]` holds" as "(&exist; `X`)
      `P[X]`&rdquo; Think back to above when we thought of &forall; as
      "and-ing" together everything that matches a pattern. Explain how &exist;
      is like "or-ing" them together.
    - What is &not;(&exist; `X`) `P[X]` in terms of De Morgan's Laws?
- Show that after the De Morgan's law step, you can safely pull all the
quantifiers to the very outside of the sentence. That is, "`A[]` &and;
(&forall; `X`) `B[X]`&rdquo; is equivalent to "(&forall; `X`) `A[]` &and;
`B[X]`&rdquo;.
- Show that you need to be careful if you have naming conflicts if the same
variable is quantified in different places in the same sentence.

There's a nice little trick that lets us get rid of all the existential
quantifiers (&exist;). Once the quantifiers have been moved outside, you can
replace all instances of existentially quantified variables with a constant!

- Show that "&exist;`X` `P[X]`&rdquo; is equivalent to "`P[x()]`&rdquo;,
assuming the function `x()` isn't used anywhere else.
- What if you have "&forall;`X` &exist;`Y` `P[Y]`&rdquo;? Show that the right
thing to do is "&forall;`X` `P[y(X)]`&rdquo; instead of "&forall;`X`
`P[y()]`&rdquo;.  What is the difference between these two sentences?

This process is called *Skolemization* (or, sometimes, *Skolemnization*). The
functions are called *Skolem functions* (some textbooks also say "Skolem
constants", but we know that constants are just special functions!).

- Explain where in the CNF conversion procedure Skolemization is most
appropriate.
- Write Skolemization as a rule of inference using the "fraction" notation.
- Explain how we can drop the universal quantifiers (&forall;) after
Skolemization and implicitly have all variables be universally quantified. From
here on out, all variables will be implicitly universally quantified. All
constants will be written as niladic functions. So `P[X, f()]` is a predicate
applied to a universally-quantified variable `X` and a constant `f`.

Sentences in this final form are said to be in *prenex form*.

---

Let's talk about *Herbrand's Theorem*, which states that a sentence is
unsatisfiable in first-order logic if and only if there is a finite subset of
ground instances that is unsatisfiable in propositional logic.

A *ground instance* is simply a version of a sentence where all variables have
been substituted so there are no variables left. For example, `P[a()]` is a
ground instance of `P[X]`.

- What is a ground instance of `P[a(), b(X, Y), Z]`?
- Show that a ground instance is "basically a proposition" in propositional
logic.

In other words, if you replace all variables with valid substitutions ("valid"
as in `X` has the same substitution everywhere) and a finite subset of the
resulting propositional logic statements are unsatisfiable, then the
first-order logic statements are unsatisfiable as well. This is perhaps
unsurprising, but, more excitingly, Herbrand's theorem guarantees that the same
holds in reverse: if it's unsatisfiable, then you must be able to find such a
finite set of substitutions. This shouldn't sound *too* trivial, since there
are an infinite number of substitutions and so guaranteeing that one exists is
something "interesting".

- What substitution makes an unsatisfiable ground instance of `P[X]` &and;
&not; `P[Y]`? Use this substitution to show that the first-order sentence is
unsatisfiable.
- Clearly, `P[X, Y]` &and; &not;`P[X, Z]` is unsatisfiable. Herbrand's theorem
guarantees an unsatisfiable ground instance. Find such a ground instance.

One way of thinking about why this is true is by looking at the "saturation" of
the sentences, which is what you get when you take all predicates and apply all
possible concrete inputs to them. Each predicate in the saturation is
practically a proposition because it has no quantified variables (as we
discussed above), and is a logical consequence of the first-order sentences
that were saturated (why?).

- Explain how the (infinite) set of sentences you get when saturating the
first-order sentences "mean" the same thing.

The argument then goes something like this:

Suppose the sentences of the saturation were satisfiable. Then we can assign a
truth value to each predicate in the first-order world by finding the truth
value of the corresponding ground instances. For example, if we had a model for
the saturation where `P[a()]` was true and `P[b()]` was false, then in the
first-order case, `P[X]` is true if `X`=`a()` and false if `X`=`b()`.

- Convince yourself that this makes sense. We didn't really talk about models
for first-order sentences.

It turns out that this is the contrapositive of the "unobvious" direction of
Herbrand's theorem, that is, that if the first-order sentences are
unsatisfiable then the saturation is unsatisfiable in propositional logic.
A satisfiable saturation in propositional logic implies, almost "by
definition", that the first-order sentences are satisfiable.

- Why is the other direction "obvious"? The other direction states that if the
saturation is unsatisfiable, then the first-order sentences are unsatisfiable
as well.

The "finiteness" guarantee that Herbrand's theorem makes comes from a theorem
called the *compactness theorem*.

- Why is this important? Explain how without this guarantee, we might have
infinitely long proofs. Must all proofs be finite?

The compactness theorem says that in propositional logic, if all finite subsets
of sentences are satisfiable, then the entire set of sentences is also
satisfiable. Equivalently, if a (potentially infinite) set of sentences is
unsatisfiable, then there must be a finite unsatisfiable subset.

Just for fun, here's a proof sketch:

Suppose you have a finitely satisfiable set of sentences. First, you extract
all of the propositions and list them out. Number all your propositions from 1
onwards (axiom of choice alert!). Now, we do an inductive proof, where at each
step we assign the next proposition a truth-value. By showing that each
assignment preserves the "finitely satisfiable" property, we basically describe
an algorithm that gives you the truth-value of any particular proposition,
which is practically a model. Since we can find a model, the set of sentences
must be satisfiable.

The base case of the inductive proof is to show that if you assign no
propositions any truth-values, then the set of sentences is finitely
satisfiable. This was the assumption of the theorem, so we're good.

For the inductive step, assume that you have truth-values of the first *k*
propositions, and the sentences are finitely satisfiable under these
truth-values.

- What does "finitely satisfiable under these truth values" mean? Come up with
two definitions: one involving replacing propositions with truth-values, and
the other involving introducing a fixed set of new sentences to each
satisfiable subset and asserting that they are *still* satisfiable.

Now, let's look at the *(k+1)*th proposition. If the set of sentences is
finitely satisfiable when that proposition is *false*, then simply assign that
sentence to false and move on. Otherwise, we will show that you *must* be able
to assign that proposition *true* and maintain the finite-satisfiability of the
set of sentences.

If you are forced to assign the *(k+1)*th proposition *true*, then there must
be a subset of sentences that is unsatisfiable if the *(k+1)*th proposition is
*false* (and all the previous *k* propositions are assigned their respective
truth-values as well!). Let's call this set of sentences *A*. Now, we will show
that *any* finite subset of sentences *B* is satisfiable if the *(k+1)*th
proposition is *true*. Thus, the set of sentences is still finitely satisfiable
and we can move on.

The idea is to look at the union of *A* and *B*. Since a union of two finite
sets is still finite, the union is also finite, and so it is satisfiable. Thus,
the *(k+1)*th proposition is either *true* or *false*. If it is *false*, then
set *A* of sentences will be unsatisfiable, and so the union of *A* and *B*
will also be unsatisfiable (why?). Thus, the *(k+1)*th has to be *true*. Since
this holds for all subsets *B*, setting that proposition to *true* maintains
finite satisfiability.

This completes the inductive proof of the compactness theorem.

- Explain why you can switch *true* and *false* in the above proof.

Another proof of Herbrand's theorem relies on so-called *semantic trees*, which
are trees where each node is a ground instance of a predicate and the left and
right branches represent the world if that predicate were true or false,
respectively. You end up making some simple arguments related to whether or not
you can find an infinitely long path by traversing the tree.

---

With Herbrand's theorem, we can construct a first-order theorem-proving
algorithm! This algorithm does resolution by generating *all* ground instances
of the first-order sentences (i.e. the "saturation"). Ground instances are
"recursively enumerable", which means you can list them out one by one and
eventually list each one (the real numbers, for example, are *not* recursively
enumerable because you can't list them because they have a higher cardinality
than the rationals).

- Come up with an algorithm to generate ground instances given a list of
functions and arities (*arity* means how many inputs that function takes). Use
a breadth-first search and explain why a depth-first search is incorrect, even
though neither algorithm will terminate.

Since each ground instance in the list is a propositional logic formula, you
can simply resolution-refutation on it. So, the algorithm is:

1. Convert your sentences to prenex form (Skolemized CNF).
2. For each ground instance...
    - Do resolution-refutation. If it finds a proof, terminate and report the
      proof.

Davis and Putnam came up with this algorithm in 1960... and their work was an
improvement on Gilmore's method which was published even earlier. But we
associate *Robinson* with the magical resolution-refutation stuff. Why?
Robinson was the first one to do it *practically*.

Listing out all the ground instances of the sentences is *slow!* There's a sort
of combinatorial "explosion" where every time you have a new variable it makes
things many times slower, because you need to generate substitutions for that
variable as well. While the algorithm works, it's too slow to be practical.

To talk about Robinson's optimization, we need to discuss a whole new kind of
algorithm. But more about that in the [next
installment](meet-the-robinson-4.html) of this, uh, ex-trilogy.  For now,
rejoice in the knowledge of a complete---albeit slow---theorem-proving
algorithm that "tames the infinite".

- Should a four-part series be called a tetralogy?
- Look up the origin of the phrase "taming the infinite" and read something by
my favorite popular math author.
