Look. I get it. Monad tutorials are a meme, memes about monad tutorials are a
meme, and we're almost at the point where memes about memes about monad
tutorials are a meme. Before we go any farther down this infinite stack of
turtles, though, I want to share one way to think about monads that doesn't
involve burritos or boxes or any Haskell code at all. I present to you, [the
Sugarloaf Transformation](https://www.youtube.com/watch?v=i4njPe2_rho).

The overall idea makes sense to me because I'm a fan of visual metaphors. Your
mileage may vary.

---

Consider the dataflow programming paradigm (think of Quartz Composer or
LabView-G). A dataflow language takes the idea of an abstract syntax tree and
extends it to the tree's close relative, the directed acyclic graph. A dataflow
program is a DAG where the edges entering and leaving each node are ordered.
Each edge is associated with a value, and a node computes the values of its
out-edges based on the values of its in-edges. Nodes with no in-edges are
called *sources*, and nodes with no out-edges are called *sinks*. The program
below computes the difference between 3 and 1, and prints the number 2. The two
nodes on the left are sources that return constants; the `print` node is a
sink.

    +---+
    | 3 |--+
    +---+  |   +-------+
           +-->|       |   +-------+
               | minus |-->| print |
           +-->|       |   +-------+
    +---+  |   +-------+
    | 1 |--+
    +---+

To interpret a dataflow program, we have a variety of strategies. We could
begin at sinks and recursively descend into in-edges until we reach sources,
which can be evaluated with no further work. This corresponds to a
recursive-descent interpreter of an AST. Alternatively, we could begin by
collecting the set of sources, evaluating them, assigning the results to the
respective out-edges. Then, we iteratively find and evaluate nodes whose
in-edges have all been assigned values, until at last we have evaluated the
entire program.

The point I wish to make is that *the order in which nodes are evaluated is
nondeterministic.* Thus, the following "obvious" program to subtract two
numbers is *not* well-defined. If given inputs "3, 1" by a human, it may output
"2" or "-2" depending on the order in which the two `read` nodes were
evaluated.

    +------+
    | read |--+
    +------+  |   +-------+
              +-->|       |   +-------+
                  | minus |-->| print |
              +-->|       |   +-------+
    +------+  |   +-------+
    | read |--+
    +------+

The problem is that nondeterministic evaluation order for IO results in the
evaluator potentially diverging. This is really bad! How can we force a
deterministic order of execution for IO primitives? Well, notice that the only
way to force node *x* to evaluate before node *y* is to make *y* depend on the
output of *x*. We can have each node output an "ordering sentinel" that becomes
the input to future nodes: this allows us to impose a partial ordering on node
evaluation, as shown below.

    +-------+   +------+     +------+
    | start |-->|      |---->|      |
    +-------+   | read |     | read |
                |      |-+   |      |-+
                +------+ |   +------+ |
                         |            |   +-------+
                         |            +-->|       |   +-------+
                         |                | minus |-->| print |
                         +--------------->|       |   +-------+
                                          +-------+

The `start` node simply emits an ordering sentinel, to kick off the
computation.

This looks really good: this program is, in fact, well-defined in its execution
order. Sadly, a partial ordering still allows divergent programs. Why? It's
because, [in the words of Philip
Wadler](http://homepages.inf.ed.ac.uk/wadler/papers/lineartaste/lineartaste-revised.pdf),
"Truth is free." Once you have computed a sentinel, you can use it wherever you
want. What prevents us from doing this?

                   +------+
               +-->|      |
               |   | read |      +-------+
               |   |      |----->|       |   +-------+
    +-------+  |   +------+      | minus |-->| print |
    | start |--+             +-->|       |   +-------+
    +-------+  |   +------+  |   +-------+
               +-->|      |  |
                   | read |  |
                   |      |--+
                   +------+

Nothing. Yikes.

---

If the problem is that "truth is free," we might be able to solve the problem
by simply restricting the flow of information created by IO primitives. One
solution is to sandbox all computation that uses the output of an IO node. An
easy way to do this is to "lock" the output of an IO node in a special pipe
that can only be unlocked by entering a sandbox. Of course, sandboxes must only
allow locked values to exit---otherwise you can trivially pass a value through
the null sandbox to unlock it. Our program then becomes the following (the
dotted boxes denote sandboxes, and fat arrows are locked).


                .................................................
    +------+    :                                               :
    | read |===>@---------------+                               :
    +------+    :               |                               :
                :             ..|............................   :
                :             : |                           :   :
                :             : |   +-------+               :   :
                :             : +-->|       |   +-------+   :==>:==> ...
                : +------+    :     | minus |-->| print |==>:   :
                : | read |===>@---->|       |   +-------+   :   :
                : +------+    :     +-------+               :   :
                :             :                             :   :
                :             :.............................:   :
                :                                               :
                :...............................................:

Notice that since a sandbox only unlocks one pipe at a time, and does not allow
the unlocked value to escape, our previous divergence hack becomes impossible.
`minus` takes two unlocked inputs, so they *must* be computed in nested
sandboxes which ensure sequential execution. Indeed, by generalizing, it is not
hard to see that now *there is only one way to compute the contents of a locked
pipe.* This means that the result of a locked pipe is literally the same as the
computation that goes into evaluating its contents---and so our programs must
have a well-defined execution order.

In Haskell, locked pipes correspond to values "boxed" in a value of type `IO a`
(this is where the burrito metaphor stems from). Sandboxes are lambdas, and the
unlocking mechanism `@` is the monadic binding operator `>>=`. The `return`
function in Haskell is simply a node that locks its input---this lets us
*return* an arbitrary value from a sandbox.  Finally, `do`-notation is just
syntactic sugar to save programmers from reasoning about lots of nested
sandboxes, in the same spirit that C has in letting you write `1+2+3+4` instead
of `1+(2+(3+4))`.

---

P.S. The title of this post refers to the idea that this transformation in a
way inverts the traditional flow of control. Normally, `minus` would call
`read` twice to get the values of its inputs. Here, however, the `reads` are
calling `minus` to create their output. "Don't call us, we'll call you."
