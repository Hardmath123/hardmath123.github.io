Welcome back.

In the [previous article](meet-the-robinson.html), we learned how **rules of
inference** allow us to prove theorems. We also learned that a rule of
inference is not necessarily **complete**: it might be impossible to prove a
true sentence with a valid rule of inference.

Today's article is about a complete rule of inference.

Before you get excited, though, let's talk about what we really mean by
"complete" in this case.

1. If a statement *must* be true given some axioms, then the rule of inference
can construct a proof for the statment.
2. If a statement is false given some axioms, then the rule of inference will
not construct a proof. It is not guaranteed to even terminate in this case.
3. If a statement could either be true or false given some axioms, then the
rule of inference will not construct a proof. It is not guaranteed to even
terminate in this case.

- Prove that "Robert is a frog" given "It rained on Monday" and "Seven is a
prime number".
- Prove that "Robert is not a frog" given "It rained on Monday" and "Seven is a
prime number".
- Explain what we mean by statements that could either be true or false, and
connect this to the discussion of undecidable problems (or independent
statements) in the previous article. These statements are (choose one)
*satisfiable/valid* but not *satisfiable/valid*.
- How can you use this rule of inference to prove that something is false?
- How can you use this rule of inference to discover whether a statement is
true or false, given that it is necessarily either valid or invalid? (Hint:
you're allowed to fork two processes and kill them if needed.)

For the purposes of this article, we can assume that the algorithm will
terminate. Later, though, we will generalize to higher forms of logic where
termination is not guaranteed.

---

The rule of inference we are going to use is called **resolution**, first used
practically by John Alan Robinson in 1965. It goes like this:

\\[
\\frac{(P \\vee \\neg Q), (Q \\vee R)}{P \\vee R}
\\]

- Prove, with a truth table, that this rule is valid.
- Convert both premises of the rule to **Kowalski Normal Form**, which means
they should both be in the form "A implies B".
- Use your expressions above to explain how resolution is really the same thing
as "P implies Q, Q implies R together mean P implies R".

Resolution proofs rely on the idea of **refutation** or *reductio ad absurdum*,
which is more commonly known as **proof by contradiction**.

Refutation relies on the idea that if not-S causes a contradiction with your
axioms and rules of inference, then not-S is invalid, so S must be valid.

- What do we mean by "contradiction"?

To use the resolution-refutation scheme to prove S given some axioms, we can
repeatedly apply resolution to pairs of sentences taken from the axioms and
not-S. If you end up deriving a contradiction, you have proven S.

The rest of this post will be dedicated to proving that this scheme actually
works.

---

Resolution operates on **clauses**, which is just a set of propositions that
are joined with "or"s. These propositions can be negated.

- Which one of the following three sentences is a clause?
    1. A &or; (B &and; C)
    2. &not; (A &and; B) &or; C
    3. &not; A &or; &not; B &or; C

Sentences are in **clausal-normal form (CNF)** if they are a set of clauses
that are joined with "and"s.

- Which of the following three sentences is in CNF?
    1. A &or; (B &and; C)
    2. A &and; (B &or; &not;C) &and; D
    3. &not; (A &and; B)

It turns out that any sentence can be written in CNF. To do this, you can
repeatedly apply the following rules:

1. Remove implication using the expression for "A &rArr; B" you've already
found.
2. Use De Morgan's laws to move "not" inwards:
    - What is &not; &not; A?
    - What is &not; (A &and; B)?
    - What is &not; (A &or; B)?
3. Distribute &or; over &and; by replacing A &or; (B &and; C) with (A &or; B)
&and; (A &or; C).
    - Prove that this is true with a truth table.

You can use induction to show that applying these rules again and again will
eventually turn your sentence into CNF.

- Show that none of these rules apply to a sentence already in CNF.

Why do we care so much about sentences in CNF? We can now extend the resolution
rule to sentences in CNF:


\\[
\\frac{(P\_1 \\vee \\dots \\vee P\_{i} \\vee \\neg X), (Q\_1 \\vee \\dots \\vee Q\_{i} \\vee X)}{P\_1 \\vee \\dots \\vee P\_{i} \\vee Q\_1 \\vee \\dots \\vee Q\_{i}}
\\]

- Convince yourself that that's a reasonable thing to do, using the concept of
associativity.

In short, if a proposition appears in both positive and negative polarities in
two clauses, you can join the clauses and remove that proposition.

- Is the singleton clause "P" technically in CNF?
- Use clause-resolution on "P" and "not-P" to find out whether the empty clause
is true or false (hint: is "P &and; &not;P" invalid?).
- Is the empty conjunction true? The empty disjunction? Explain what a vacuous
truth is.
- Use resolution-refutation to prove *modus ponens*. If you only do one
exercise in this article, do this one. (Hint: use the inference rule twice.) 
- Ryan Marcus has a nice article on propositional resolution
[here](http://rmarcus.info/blog/2015/09/02/vulcan.html), which includes an
interactive demo. Play with that demo.

---

We're now going to prove if you have an unsatisfiable set of clauses, then you
can repeatedly resolve them to derive the empty clause. This provides a model
for us to have a terminating theorem-proving algorithm!

This proof is taken almost directly from Russell and Norvig's textbook, though
I tried to cut down on the notation.

Imagine we've already applied resolution to each pair of clauses,
and recursively resolved the results, and so on to obtain an (infinite?) set
of clauses. We call this the resolution *closure* of these clauses.

Suppose also that the set of clauses was unsatisfiable, but this set of
resolved clauses does not contain the empty clause. We're going to show that
you can, in fact, satisfy the clauses, leading to a contradiction.

To satisfy the clauses, follow the following algorithm:

1. Number your propositions from 1 to *k*.
2. For the *i*th proposition P[i]:
    1. If one of the clauses in the set contains &not;P[i], and all other
       propositions in that clause are false based on the values assigned to
       P[1], P[2], ..., P[i-1], then set P[i] to *false*. This is basically
       clauses that look like (*false* &or; *false* &or; ... &or; &not; P[i]).
    2. Otherwise, set P[i] to *true*.

The claim is that this procedure will always work, that is, none of these
assignments will make a clause false. To see this, suppose assigning P[i] did,
in fact, cause a clause to be false. Specifically, no clauses were falsified
by any of the previous assignments. Then the following could happen:

1. That clause was empty from the beginning, and thus always false. We can
ignore this case because we're assuming the set of resolved clauses does *not*
contain the empty clause.
2. The clause was of the form (*false* &or; *false* &or; ... &or; P[i]) and we
assigned P[i] to *false*. (Why is this the only other case?)

If the latter case occurs, then we must also have (*false* &or; *false* &or;
... &or; &not; P[i]), because that's the only situation in which P[i] is
assigned false.

Now, here's the crucial bit: these two clauses resolve! Since they contain P[i]
and &not;P[i], respectively, we resolve them to obtain a clause that has only
false values in it. This contradicts our assumption that no clauses were
falsified by any of the previous assignments.

So, we know that if the empty clause is not part of the set of resolved
clauses, then the clauses are satisfiable. By contrapositive, it follows that
you can always resolve some set of them to get the empty clause. Q.E.D. &#9632;

---

There's another argument that explains this: an inductive one which you can
read [here](http://www.mathcs.duq.edu/simon/Fall04/notes-6-20/node3.html). In
short, it inducts on the total number of propositions, where the base case is
that if you have only one literal per clause, then either it's satisfiable, or
it's unsatisfiable and you can resolve to get the empty clause.

- Convince yourself that this base case is true.

---

So where are we? We have an algorithm that will definitely terminate on a valid
statement, though we have not yet said anything about what happens when it is
given anything else.

The resolution method should feel extremely powerful. Of course, as the number
of propositions increases, it will get exponentially slower (boolean
satisfiability was actually one of the first problems to be proved as
NP-complete---and, in fact, constraint solving algorithms like DPLL correspond
pretty much to resolution-refutation).

But that's okay! It works!

One question you should have is, "What can I prove with propositional logic?"

- Can you use propositional logic to reason about the integers? Why or why not?

Propositional logic is bound to a *finite* number of propositions. That means
you can't say things like "1 is an integer", "2 is an integer", "3 is an
integer", etc.

In the next article, we will extend propositional logic to a much richer form
that supports an infinite number of propositions, and show that
resolution-refutation still works.

- Write your own resolution theorem prover so that you can experiment with
some large proofs. It's not hard; you can think of this as a code golf
challenge if you'd like.
- Find three more things you liked and three more things that could be
improved about this article series, and report them to me.
