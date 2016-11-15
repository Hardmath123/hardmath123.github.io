> I recently had the privilege of attending a talk by Guy Steele: and that
> reminded me of one of his most famous lectures, *Growing a Language*. I don't
> want to spoil the talk for you, so I encourage you to watch it [on
> YouTube](https://www.youtube.com/watch?v=_ahvzDzKdB0), or at least to read a
> [transcript](https://www.cs.virginia.edu/~evans/cs655/readings/steele.pdf). I
> promise that it's relevant.

In the ring of integers, prime numbers can be enumerated using the "Sieve of
Eratosthenes". In *linguistics*, we define a [semantic
prime](https://en.wikipedia.org/wiki/Semantic_primes) as an idea that can't be
expressed in simpler terms (for example, "there exists" or "because"). The
question I ask in this blog post is, how do I enumerate semantic primes? In
other words, *does there exist an efficient semantic sieve?*

The motivation here isn't to build some sort of [Basic
English](http://ogden.basic-english.org)---or Newspeak---but rather to better
understand the building blocks of our communication. However, this problem has
more than just linguistic appeal. Consider the popular computer game Alchemy,
which lets you combine elements like "fire" and "water" to produce "steam".
Given all the elements of alchemy, as well as the possible recipes, what are
the possible starting elements? Similarly: approximately twice a year like
clockwork, someone in the Scratch community notices that [some Scratch blocks
can be defined in terms of
others](https://wiki.scratch.mit.edu/wiki/List_of_Block_Workarounds), and then
proceeds to ask what the minimal set of Scratch blocks is (you can see, for
example, the [October](https://scratch.mit.edu/discuss/topic/223486/) and
[April](https://scratch.mit.edu/discuss/topic/195968/) editions of this
conversation). Clearly, any block that has no "workaround" (and, analogously,
any word without a definition) must remain in a set of semantic primes, which I
will call the "basis set" from now on.

Beyond that, though, it is not immediately obvious which blocks or words must
be kept in order to minimize the basis. If you define a "puppy" as a "small
dog" and a "dog" as a "large puppy", then which should you keep in your basis
set? Perhaps you already have "small", in which case it makes sense to keep
"dog" to get "puppy" for free. Clearly, there are many possible basis sets
(trivially, all words together form a basis). We're just searching for the
*smallest* such set (which may not even be unique!).

All this is to say, this is not an easy problem.

If you're impatient for a solution (or just want to get the answer from a more
reliable source), David P. Dailey has the answer in his paper, [The extraction
of a minimum set of semantic primitives from a monolingual dictionary is
NP-Complete](http://www.aclweb.org/anthology/J86-4003), published in 1986.

Here, I want to present three subtly different ways to solve this problem.
While the solutions I will present are perhaps evident to you already (and
honestly not that profound), I would like to take this as an opportunity to
explore the delightful subtlety that connects various areas of math---something
that is getting dangerously close to becoming a theme of this blog.

### Act I: In which we dissolve our problems to get a solution

A dictionary is something that takes knowledge and gives you more knowledge.
This is immediately reminiscent of formal logic, where you can take two
statements and derive a new statement using an inference rule (we explored much
of this theory in my 4-part series on formal logic and automated
theorem-proving, [Meet the
Robinson](meet-the-robinson.html)).

Let each word be associated with a proposition. We can now reason about the
provability of propositions equivalently with the definability of the
associated words. In particular, a definition corresponds to an implication,
where the conjunction of the definition's propositions together imply the
defined word's proposition. Thus, "a bird is a winged animal" turns into
`winged` &wedge; `animal` &rarr; `bird`.

Now, to reason about provability, I used what I knew about
resolution-refutation. We want to prove the conjunction of the propositions of
all the words in the dictionary by adding as few fresh axioms as possible,
where each added axiom is just a lone proposition. One way to do this is to
resolution-refute against the negation of this conjunction, searching for
clauses that *only* have terms in negative polarity. The smallest such clause
represents the minimal set of axioms needed to make the negation disprovable,
and thus the desired conjunction provable.

Notice, however, that we can't use the full power of resolution-refutation
here, because we are limited to only one incomplete inference rule: *modus
ponens*. For instance, if `P` &rarr; (`Q` &vee; `R`) and `Q` &rarr; `Z` and `R`
&rarr; `Z`, then we cannot prove `Z` via modus ponens even though it is
"obviously" true.

So, rather than "resolving" two clauses, we need to do some other kind of
operation, which I'm going to call "dissolve" for lack of a better name.
Dissolving is kind of the opposite of modus ponens. To solve the problem at
hand, you compute the closure of the set of axioms (along with the negation you
want to disprove) under dissolution, and filter out clauses that only have
negative terms. Once you've saturated the set, the smallest such clause gives
you the basis.

```haskell

import Data.List(nub, union, (\\))
import qualified Data.Set as Set
import Control.Exception.Base(assert)

type Clause = (Set.Set String, Set.Set String)
-- Polarity =  Positive        Negative

isOnlyNegative :: Clause -> Bool
isOnlyNegative (a, _) = Set.null a

-- Only applies when dissolving (a & b & ...) => e against !x | !y | ...
dissolve :: Clause -> Clause -> Clause
dissolve (a, x) (b, y) =
    let u = Set.intersection x b in -- u is probably a singleton set
        assert (Set.size u <= 1)    -- or so we hope!
        (Set.union a (Set.difference b u),
         Set.union (Set.difference x u) y)

dissolveAll :: [Clause] -> [Clause] -> [Clause]
dissolveAll x y =
    let apex =
            filter isOnlyNegative $ nub [dissolve b a | a <- x, b <- y] \\ x in
        if null apex then
            []
        else
            apex ++ (dissolveAll (x++apex) apex)

dissolveStream :: [Clause] -> [Clause]
dissolveStream cs =
    let bad = [(Set.empty, Set.unions $ map fst cs)] in
        dissolveAll (cs++bad) bad

solutions cs =
    map snd $ filter isOnlyNegative (dissolveStream cs)


-- You gotta know when to fold 'em.
bestSolutions [] n = []
bestSolutions (s:ss) n =
    if n<0 || Set.size s < n then
        s:(bestSolutions ss (Set.size s))
    else
        bestSolutions ss n

solve d = bestSolutions (solutions d) (-1)

mkdfn (a:as) = (Set.singleton a, Set.fromList as)

w = map mkdfn [
    "water":["hydrogen", "oxygen", "fire"],
    "oxygen":["plant", "water"],
    "fire":["oxygen", "heat", "hydrogen"],
    "wood":["plant", "soil"],
    "plant":["water", "time", "soil"],
    "soil":["nitrogen", "time"],
    "nitrogen":["hydrogen", "heat"],
    "heat":["time"]
    ]

main = putStrLn $ show $ solve w
```

Against all odds, this seems to work, and with a little thought you can
probably convince yourself that it will always work.


### Act II: What is an animal, but a bird without wings?

What else lets us take things and make new things? We talked about statements
in logic, so how about the other kind of mathematical statement: the equation?
We can certainly combine equations to derive more knowledge, so it doesn't
sound far-fetched to model words with variables and definitions with equations,
and then reason about the *solvability* of the equations (rather than the
*provability* of the terms).

More formally: assign each word a unique positive integer and a variable.
Construct linear equations using the sum of the definition-words on the
left-hand-side, and the word-to-be-defined with the correct coefficient on the
right-hand-side. So, if a bird=4 is a winged=2 animal=3, then construct
the equation "winged + animal = (5/4) bird", which is clearly true.

How does this help?

Well, solvability of linear equations is well-studied stuff. If you encode the
equations in a matrix, and convert it to reduced-row echelon form using
Gauss-Jordan elimination, the result is a matrix where

1. The first few rows show you how to get some variables in terms of other
   variables -- indeed, the maximal linearly-independent set
2. The remaining rows say that those variables can't be solved for in terms of
   the rest

Thus, if we supply "values" of all variables in the latter rows, then we can
deduce values of the variables in the former. Since the Gauss-Jordan
elimination procedure minimizes this set, we're already done.

```python

from __future__ import division
import sympy

n_cache = []
def numify(g):
    def n(x):
        try:
            return n_cache.index(x)
        except ValueError:
            n_cache.append(x)
            return len(n_cache)-1
    return [map(n, r) for r in g]


def mktrix(g):
    count = len(g)
    m = []
    for d in g:
        row = [0]*(len(n_cache)+1)
        for k in d[1:]:
            row[k] = 1
        row[d[0]] = -(sum(d[1:])+len(d[1:]))/(d[0]+1)
        m.append(row)
    return m

def solve(m):
    return sympy.Matrix(m).rref()[1]

def basis(g):
    return set(n_cache) - {n_cache[x] for x in solve(mktrix(numify(g)))}

test = [
    ["water", "hydrogen", "oxygen", "fire"],
    ["oxygen", "plant", "water"],
    ["fire", "oxygen", "heat", "hydrogen"],
    ["wood", "plant", "soil"],
    ["plant", "water", "soil"],
    ["soil", "nitrogen", "time"],
    ["nitrogen", "hydrogen", "heat"],
    ["heat", "time"]
]

print basis(test)
```

But: Gauss-Jordan elimination is O(n<sup>3</sup>) and Dailey claims this
problem is NP-complete. Clearly, we haven't just proven that P=NP. So what
gives?

It turns out that we made a subtle extra assumption when encoding a
"provability" problem in terms of a "solvability" problem. Logical implications
are one-way: if P implies Q, then Q does not imply P. However, the linear
equations we're working with are *not* one-way! If you can solve for x in terms
of y, then you can usually also solve for y in terms of x.

So, for example, given definitions of "bird" and "winged", and the relationship
"a bird is a winged animal", the linear equation model assumes we can deduce
what an "animal" is. And in many cases, this is a reasonable assumption:
indeed, it's kind of how the game *Jeopardy!* works: "if you add wings to
*this*, you get a bird" is not the worst way to hint at the word "animal". It
relies, in the end, on what you mean by "define".

That being said, I do want to note that this kind of reasoning can lead you
straight to deriving Buckingham's &Pi; Theorem in dimensional analysis (we
discussed this theorem in detail [in a recent
article](dimensional-analysis.html)). This fact shouldn't come as a surprise to
anyone: dimensional analysis, too, deals with getting more knowledge from
existing knowledge. The reasoning shown here can help identify redundant units,
and thus discover the "fundamental" kinds of quantities in the physical world.
Do we necessarily need units for frequency *and* for time?

### Act III: Come on! We've got a diem to Karp(e)!

In our hearts, we always knew this was a graph theory problem, and so naturally
I feel compelled to present a graph-theoretic solution. This is the one Dailey
presents in his 1986 paper cited above.

Consider a graph where each word corresponds a vertex, and a directed edge
travels from a word to another if the former is used in the definition of the
latter. Naively, we may imagine that all we need to do is find all the leaves
of this graph. However, this doesn't work in the presence of cycles (if "GNU"
is defined as "GNU's Not UNIX", then you definitely want "GNU" in your basis
set).

What we really seek is the smallest possible set of vertices such that:

1. All leaves of the graph are in the set
2. If each vertex in the set is removed from the graph, the result is
   cycle-free

In other words, what we want is the minimum [feedback vertex
set](https://en.wikipedia.org/wiki/Feedback_vertex_set) of the graph, which is
one of Karp's 21 NP-Complete problems. This is unfortunate, but on the bright
side, computers are fast and so we can at least hope to find solutions.

There exist a bunch of algorithms to compute the FVS, but I chose to stick with
the theme of logic by using an SMT solver (inspired by
[this](https://github.com/firedrakeproject/glpk/blob/master/examples/mfvsp.mod)).
That is, I encoded each vertex with (1) a "guard" bit that says "am I part of
the basis", and (2) an integer that corresponds to an index into a topological
sort. Then, for each pair of vertices, I check that if neither vertex is part
of the basis, then the topological indices obey any edges between the vertices.
This gives me a cheap cyclic-ness check that is easy to execute symbolically
because it is nonrecursive. Finally, using
[Rosette](http://emina.github.io/rosette) to run the algorithm symbolically, I
can solve for guard bits and indices that make the graph cycle-free. All that's
left is to minimize the number of guard bits that are "true", which is
supported by Z3 via a "minimize" call.

```scheme
#lang rosette

(define graph
  '((water hydrogen oxygen fire)
    (oxygen plant water)
    (fire oxygen heat hydrogen)
    (wood plant soil)
    (plant water time soil)
    (soil nitrogen time)
    (nitrogen hydrogen heat)
    (heat time)
    (hydrogen)
    (time)
    ))

(define (cycle-free? graph)
  (andmap
    (λ (vertex)
       (define v (car vertex))
       (define children (cdr vertex))
       (define topology (cdr (assoc v s-cache)))
       (andmap
         (λ (c)
            (define topology+ (cdr (assoc c s-cache)))
            (if (or (car topology) (car topology+))
              #t
              (> (cadr topology) (cadr topology+))))
         children))
    graph))

(displayln "Initializing...")

(define s-cache
  (map (λ (v)
          (define name (car v))
          (define-symbolic* guard boolean?) ; am I part of the initial spawn
          (define-symbolic* index integer?)
          (list name guard index))
       graph))

(define fvs-count (apply + (map (λ (x) (if (cadr x) 1 0)) s-cache)))

(displayln "Solving...")

(define sol
  (optimize #:minimize  (list fvs-count)
            #:guarantee (assert (cycle-free? graph))))
(if (unsat? sol)
  (displayln "dude you failed")

  (append
    ; leaves
    (map car (filter (λ (x) (= (length x) 1)) graph))
    ; feedback vertex set
    (map car
         (filter
           (λ (x)
              (define u (evaluate (cadr x) sol))
              (and (not (constant? u)) u))
           s-cache))))
```

Tim scraped the Scratch Wiki's workaround database for me, and though the
scraping is dodgy at best, my analysis showed that of the 103 blockspecs
mentioned, only about half are needed (Brian, of course, pointed out that in
Snap*!* all you need is lambda). So that answers *that* question. As for the
English language, well, I would almost certainly need a bigger computer to deal
with millions of words. I guess I could scrape from [GNU's free
dictionary](http://gcide.gnu.org.ua), but that's a project for another day.

Meanwhile, I want to note that this procedure doesn't allow one word to have
multiple equivalent definitions, unlike both the propositional-provability
approach *and* the linear-algebra approach.

### Conclusion

If nothing else, I loved this little question because it forced me to think
deeply about how to model something new and unfamiliar in terms of math I
already knew.

My chemistry teacher used to put at least one "toolbox" question on his tests.
A toolbox question is one that doesn't imply what tool you should use to solve
it: unlike standard textbook stoichiometry problems that can all be solved with
the same trick, a toolbox problem forces you to look at your toolbox and pick
the tools yourself.

Well, in the same spirit---and I've [used this metaphor
before](no-rules-in-math.html)---I feel that high school mathematics has given
me an incredible set of tools, but not nearly enough opportunities to use them.
Sure, I've often had to solve linear equations and prove theorems in
propositional logic: but I have rarely *chosen* to do so in order to solve a
problem.

Maybe that's why I care so much about finding math in the world around me.
