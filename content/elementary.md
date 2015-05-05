This is The Awesome Elements Problem. I wrote it for my AP Computer Science
class, but I decided to put it up here because I think it's pretty, uh,
*elementary*.

Perhaps more than the actual problem, I love the bonus problems at the bottom.
They show how all these "boring" Scheme exercises can be used to do all sorts
of neat things. They're written to introduce a new idea with lots of
questions--the solver is expected to explore them both on their own, with
external resources, and, of course, with other friends.

Finally, it's worth noting that (as the first bonus problem should make amply
clear) this problem is an absolute pain to do in an imperative language. I
think it lets beginners see a rare outside-the-textbook example of functional
programming rocking out in the wild, rather than silly contrived scenarios
involving bank accounts or store inventories or parking meters.

Teachers are welcome to steal this for their classes.

---

Some names are inherently different from others. For instance, the name Casey
can be written as a list of element symbols, as Ca-Se-Y
(Calcium-Selenium-Yttrium). However, Josh cannot be written this way. In this
project, you get to write a Scheme program to break up a word into
its--ahem--constituent elements.

We begin by defining a list of all the elements. An element's symbol is
described by a list of Scheme symbols, so Helium is `'(h e)`. As a sanity
check, you can run `(length elements)` and get 118.

    (define elements '((a c) (a g) (a l) (a m) (a r) (a s) (a t) (a u) (b) (b
    a) (b e) (b h) (b i) (b k) (b r) (c) (c a) (c d) (c e) (c f) (c l) (c m) (c
    o) (c r) (c s) (c u) (d b) (d s) (d y) (e r) (e s) (e u) (f) (f e) (f m) (f
    r) (g a) (g d) (g e) (h) (h e) (h f) (h g) (h o) (h s) (i) (i n) (i r) (k)
    (k r) (l a) (l i) (l r) (l u) (m d) (m g) (m n) (m o) (m t) (n) (n a) (n b)
    (n d) (n e) (n i) (n o) (n p) (o) (o s) (p) (p a) (p b) (p d) (p m) (p o)
    (p r) (p t) (p u) (r a) (r b) (r e) (r f) (r g) (r h) (r n) (r u) (s) (s b)
    (s c) (s e) (s g) (s i) (s m) (s n) (s r) (t a) (t b) (t c) (t e) (t h) (t
    i) (t l) (t m) (u) (u u b) (u u h) (u u o) (u u p) (u u q) (u u s) (u u t)
    (v) (w) (x e) (y) (y b) (z n) (z r)))

Whew. For extra credit, come up with a way to make that list automatically from
some table you find on the Internet.
[Here's](http://akiscode.com/project_files/pt/periodictabledump.csv) a nice
one.


Let's warm up with some easy helper functions. Write
`(get-rest-of-string str len)`. It should return the list `str` after the first
`len` elements have been removed.

If you've written `compose` before, think of a super-elegant way to do this.

Now, write `(begins-with-element str el)`, where `str`
and `el` are lists of symbols. The function should return true if `el` is
exactly the beginning of `str`, and false otherwise. Think about what should
happen if either string is empty.

    (begins-with-element '(d o c t o r w h o) '(d o c))
    --> #t
    (begins-with-element '(a m e l i a p o n d) '(a m y))
    --> #f

It turns out that these are all the helpers we need to write `elementize`.
`elementize` is our main function. It breaks up the word `str` into elements
in the list `els`, and returns *all* possible results. Fill in the blanks to
complete `elementize`.

Or, if you can think of a better way to write it that doesn't fit in the
blanks, do that instead.

    (define (elementize str els)
        (cond ((null? els) ___)
              ((null? str) ___) ; Hint: this is not the same as above.
              ((begins-with-element ___ (___ ___))
               (append
                   (elementize ___ (___ ___)) ; Remember, `append` concatenates
                                              ; two lists into one bigger list.
                   (map
                        (lambda (list-of-subsolutions)
                            (cons (___ ___) ___))
                        (___
                            (___
                                ___
                                (length (___ ___)))
                            ___))))
              (else (elementize ___ (___ ___)))))


You can use these tests to try out `elementize`. I've provided the solutions
at the bottom of this page.

    (write (elementize '(j a v a) elements))
    (newline)
    (write (elementize '(i s) elements))
    (newline)
    (write (elementize '(u n n e c e s s a r y) elements))
    (newline)

---

Great job! Now for the fun part. Try solving each of the bonus problems below.
They're in no particular order of difficulty. Each one is meant to introduce
you to a new, exciting CS topic.

**Bonus problem 0!** Rewrite your solution in C or Java. Time yourself. Then
realize how much you love Scheme.

**Bonus problem 1!** UNIX computers come with a built-in dictionary of English
words in the file `/usr/share/dict/words`. Each word is on its own line. Spend
some time hacking Scheme to see if you can find the single English word that
can be elementized the most ways. How about the longest elementizable word? Are
there any "unnecessary" elements which can be removed from the list without
making any words un-elementizable?

**Bonus problem 2!** You've just discovered a new element! With all your
modesty, you decide not to name it after yourself. Instead, you decide to name
it so that the addition of the new element will maximize the number of new
elementizable words in English (based on the list above). What do you name it?
(This one is hard because the program needs to be fast! See if *memoization*
can be useful.)

**Bonus problem 3!** On a small planet in the vicinty of Betelguese, only two
elements can exist in a stable state: Zaphodium and Zemzine. Their symbols were
carelessly named Z and Zz by the Chief Chemist (who was later thrown into a vat
of zaphodous zemzide (ZZz) by his angry confused chem students).

How many different ways are there to elementize the word `zzzzzzzzzzzzzzzz`
with Z and Zz? How is this related to the question *"how many ways are there to
cover a two-by-ten grid with dominoes"*? (Hint: this is purely a math problem.
You can use a computer to help find the answer, but try to use math to prove
it.)

**Bonus problem 4!** Read about *lazy lists*. Figure out how to implement them
in Scheme, and then use them to solve this problem. Is your solution faster?
More space-efficient? Does it look prettier?

Once you've done that, read about `call-with-current-continuation`. Figure out
how to use it cleverly to solve this problem (if you're confused, read about
*backtracking*, or consult the Python program linked at the bottom of this
page). Is your solution faster? More space-efficient? Does it look prettier?

Think about how the above two implementations are the same, and how they are
different. Can you use `call-with-current-continuation` to implement lazy
lists?

**Bonus problem 5!** Read about *regular expressions*. Which regex do names
like "Casey" match? Which regex do names like "Josh" match? Which of the
previous two questions is easier, and why?

You can use a program called `grep` to test your solutions.

---

(Non-aqueous) Solutions to the tests above:

    java (0)
    ()  -- Java is *clearly* not an awesome name. Try Lisp instead.

    is (1)
    (((i) (s)))

    unnecessary (2)
    (((u) (n) (n e) (c e) (s) (s) (a r) (y))
     ((u) (n) (n e) (c) (e s) (s) (a r) (y)))

---

(This problem was written in November 2014. It is based on a [bad Python
program](https://gist.github.com/Hardmath123/7862258) I wrote in December 2013.
The only modification is that it was originally distributed as a Scheme source
file where all the text was commented out, and method stubs were left for
students to fill in. I have also added a couple of bonus problems--only 1-3
were in the original source. Please contact me directly if you'd like the
original file, along with its solution file.)
