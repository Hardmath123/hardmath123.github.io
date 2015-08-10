So a notorious Scratch user,
[TheLogFather](http://scratch.mit.edu/users/TheLogFather/), posted a
[project](http://scratch.mit.edu/projects/41196030/) where he compared two
different ways to prepend to a list. Here they are, as both an image and as
a pseudocode.

![The project](/static/scratch-splice.png)

```python
    mylist = [1,2,3,4,5,6,7,...,20000]
    def prepend1(n):
        repeat n times:
            insert random number at beginning of mylist
    
    def prepend2(n):
        temp = new list
        for each item in list:
            append item at end of temp
        delete all of mylist
        repeat n times:
            append random number at end of mylist
        for each item in temp:
            append item at end of mylist
```

It should be pretty clear that the two are semantically equivalent, that is,
that they will have the same net effect. However, notice that `prepend2` uses
only `append` instructions, while `prepend1` uses the `insert` instruction.

Now, from a cursory look, `prepend2` looks much slower: you are iterating over
the initial contents of `mylist` *twice* when copying it in and out of `temp`.

Surprisingly, though, `prepend2` is significantly faster. A quick speedtest
on my MacBook Pro says that `prepend1` takes **4.616** seconds while `prepend2`
takes a mere **0.724** seconds for 20,000 items.

Hopefully the reason why will be clear at the end of this blog post.

The first thing to do here is dig into the source and find the implementation
of the `insert` and `add` blocks in Scratch. Scratch 2.0 is open-source and
written in Actionscript. We find it all [on
Github](https://github.com/LLK/scratch-flash/). A little digging reveals the
file `src/primitives/ListPrims.as`. This is where the list blocks are
implemented. Looking around, we find the important sections:

    protected function listAppend(list:ListWatcher, item:*):void {
        list.contents.push(item);
    }

and

    protected function listInsert(list:ListWatcher, i:int, item:*):void {
        list.contents.splice(i - 1, 0, item);
    }

Now, `ListWatcher` is defined in `src/watchers/ListWatcher.as`. We see that
`contents` is an `Array`:

    public var contents:Array = [];

Let me say that again: in Scratch, a **List** is actually an **Array**. If this
doesn't bother you now, don't worry, it will bother you soon.

Anyhow, we're looking at the difference between `Array.splice` and
`Array.push`. From Adobe's documentation, we know that `Array.splice` inserts
and deletes elements of an array at an arbitrary index, and `Array.push` tacks
elements on to the end of an array. Why is this important? To see that, you
need to know a bit about how memory works.

---

ActionScript is an incarnation of ECMAScript, much like JavaScript. There isn't
much documentation about ActionScript's VM, but there's tons about how JS
handles `Array`s. So, though it's not a completely legitimate assumption, I'm
going to explain what's going on based on how JavaScript does things.

In a computer's RAM, you can access any memory address in constant-time. That
means it takes just as long to get the contents of the billionth address as it
does to get the contents of the first.

When you run a computer program, at a sufficiently low level, you're allocating
some segment of the RAM for the program to access. The program basically treats
this segment as a really long list, where each element has an upper limit on
size.

It's easy to store an integer (within limits) or a boolean value in memory,
because it takes up just one cell of memory. But anything larger---a string, a
list, an image, or a sprite---takes up multiple cells, and so you need a scheme
by which those cells are allocated in an organized way.

In low-level programming languages like C, you have the `malloc` function that
allocates the given amount of memory as a sequence of contiguous cells and
returns the address of the first one. However, the catch is that once you're
done using that memory, *you* are responsible for freeing it (with the `free`
function). Otherwise future calls to `malloc` will assume that you're still
using those addresses and pick some other addresses to allocate. Eventually
you'll run out of memory and things will start dying.

In higher-level languages (like ActionScript and JavaScript), the interpreter
manages memory for you. You're free to run around creating sprites and lists
and mammoths and cows and whatever, and the interpreter destroys them when it
notices that you're done with them. This is called Garbage Collection, and is
beyond the *scope* of this article (seasoned CS students will get that joke).

When you create an `Array` in JavaScript, the interpreter allocates a block of
memory for you. If you want to access the 5th element, the interpreter says
"`malloc` told me the array starts at address 900, so I want to return the item
at address 900+5=905".

Since RAM has constant lookup time, your Array will also have constant lookup
time (it'll just take a hair longer because you need to find the address).

---

Now that you know how Arrays work, it should be obvious that inserting an
element into an array is hard. Why? Well, there's no space! Think of the RAM as
people sitting on a bus. The first few seats are full. If you make a fuss and
insist on sitting in the front seat, you need to first move everyone else down
one seat.

If you're trying to put an item at the beginning of an array with 5000
elements, you need to move down each of those 5000 elements one cell. This
takes 5000 operations. This is bad.

Similarly, deleting is hard because you'll leave an empty seat, and then you
need to move everyone up a seat to fill the hole (remember, the fast
index-lookup only works if the array is contiguous!). If you delete the first
element of an array with 5000 elements, the remaining 4999 need to be moved up
a spot, which takes 4999 operations. This is also bad.

But this is often necessary, and is done all the time in JS or ActionScript
programs with the `splice` function.

You might have already realized how `push` is better. If you sit at the back of
the bus, you don't need to relocate everyone in front of you. So it's actually
a constant-time operation.

Of course, in a computer's RAM, that cell might be occupied by the beginning of
another array. If that's the case, the interpreter needs to move things around.
It's unpleasant, but it only happens once in a while. So `push` occasionally
takes a long time. But most of the time, it's blazingly fast.

And that's the reason why `insert` is slower than `add` in Scratch.

---

As an afterword, it's worth mentioning that if you do lots of inserting and
deleting, there's a better way to store a list than an Array. It's called a
List. A List in CS is not the same thing as a List in Scratch.

A List consists of lots of *pairs*. A *pair* is a 2-element Array. The first
element contains some data, and the second element is the address of the next
pair (we can call this the "address pointer" because it *points* to the next
pair).

For historic reasons, the "value" cell and the "address pointer" cell are
called the "address register" and "decrement register", and so old languages
will provide functions like "contents of address register" (`car`) and
"contents of decrement register" (`cdr`, rhymes with udder). Lisp programmers
use `car` and `cdr` all the time to manipulate pairs. In fact, Lisp's name
comes from List Processing.

The order in which the pairs are stored in memory doesn't matter. So, when you
want to insert something, you create a new pair *anywhere* in the RAM, and then
change the address pointers to incorporate the new pair.

To delete something, you `free` the pair and fix the pointers. Fixing pointers
is easy (just an assignment), so Lists are easy to mutate.

Of course, finding the 5000th element of a list would require you to follow
5000 address pointers (Lispers call it `cdr`ing down the list), so lookups are
not constant-time anymore. Choosing the right data structure is important.

By the way, Snap*!* is extra-clever: it stores your lists as Lists *or* Arrays
depending on how they were created. If you use Array-ey operations on them,
they get converted to Arrays, and if you use List-ey operations on them, they
get converted to Lists. If you want to be fast, you need to pick a style and
stick with it. But that's good programming practice anyway.
