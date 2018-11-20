I recently read this [Atlantic
piece](https://www.theatlantic.com/technology/archive/2016/11/chinese-computers/504851/)
on input methods for computers, and it reminded me of a mathematical adventure
I had this summer that I should have blogged about at the time.

Back in July, I was exploring the City Museum of New York when I came across
this lovely Crown typewriter from the late 1800s. By our modern standards, it
uses a rather clunky input mechanism: you manually shift the pointer to the
character you want to type, press the button, rinse, repeat.

![Crown Typewriter](static/crown-typewriter/crown-typewriter.png)

"What a waste of time," you say. Ah, but even in the late 19th centure time was
the essential ingredient, and in the modern world there was no time. Notice,
then, that the designers of the Crown typewriter did not place the letters in
alphabetical order. Instead, the they placed commonly-together letters near
each other. You can type "AND" and "THE" rather quickly with just 2 shifts
apiece; "GIG," on the other hand, takes 15 shifts from the G to the I, and 15
shifts back to the G.

The question, then, begs to be asked: is this the _most efficient_ permutation
of letters? For example, Q and U are on opposite ends of the typewriter; surely
it would be better to put them together?

I have a doubly disappointing answer to this question: first, this is _not_ the
most efficient permutation of letters (based on my digraph frequency map), but
I also don't _know_ what the most efficient permutation is! That is, I've found
permutations that are more efficient, but cannot prove that they are optimal
--- after all, exploring all 26-factorial permutations is not an option.

My "cost" metric here is defined as "Ignoring non-alphabetic characters, how
many shifts does it take to type all of _Pride and Prejudice_ followed by all
of _The Time Traveller_ followed by all of _The Adventures of Sherlock
Holmes_?" (All three are classic 19th-century novels available from Project
Gutenberg.)

By this metric, the naive alphabetical order (`ABCDEFGHIJKLMNOPQRSTUVWXYZ`)
requires a whopping 9,630,941 shifts. In comparison, the Crown Typewriter
(`XQKGBPMCOFLANDTHERISUWYJVZ`) requires only 6,283,692 shifts. But the
ComfortablyNumbered typewriter (`ZKVGWCDNIAHTESROLUMFYBPXJQ`) requires a mere
5,499,341 shifts. This means we can save nearly one in eight shifts from the
Crown typewriter!

I found this permutation with the following algorithm: start with a random
permutation, then "optimize" it by repeatedly swapping characters such that the
post-swap permutation has a lower cost than the pre-swap permutation. Continue
"optimizing" until no further swaps can be made. Now, do this procedure for a
large number of random starting permutations, and pick the lowest-cost
optimized permutation.

Encouragingly, it turns out that many different random starts get optimized to
my solution. What do I mean by that? Well, the graph below shows two datasets:
the costs of 1,000 random permutations and the costs of those permutations once
optimized. Clearly, optimization is doing great good.

![First graph](static/crown-typewriter/typewriter-graph-1.png)

But let's zoom in on the optimized permutations. Notice that the two
lowest-cost bars are almost an order of magnitude more frequent than the
remaining bars. In fact, the lower-cost bar's "bucket" in the histogram is
populated _only_ with permutations of cost 5499341! This suggests that 5499341
is a "hard ceiling" for my optimizer, rather than the furthest point on the tip
of a long tail that my optimizer samples from.

![Second graph](static/crown-typewriter/typewriter-graph-2.png)

Of course, this is no proof: there might be a single highly-efficient
permutation that is hard to reach by optimizing a random permutation. But that
_feels_ unlikely!

So: I leave this as an open problem for readers to explore.
