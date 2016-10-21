I'm taking AP Music Theory this year, and I've been spending some time
exploring the number theory of music. This post is just a quick check-in on my
thoughts so far, and an explanation for why I'm trying to build a 19-note
marimba in my spare time.

---

A piano has 12 notes between consecutive C's: C, C#, D, D#, E, F, F#, G, G#, A,
A#, B, and C again. A good question to ask is, "why?"

Well, it comes down to how your ear works. There is plenty of literature on
this (I recommend [this blog
post](https://eev.ee/blog/2016/09/15/music-theory-for-nerds/) or [this
video](https://www.youtube.com/watch?v=i_0DXxNeaQ0)), but the main takeaway is
that for a variety of reasons related to the structure of your cochlea, your
brain likes to hear frequencies that have nice whole-number ratios. For
example, a C is 256 Hertz while a G is 384 Hertz, and 384/256 = 3/2 which is a
nice whole-number ratio. Indeed, if you play a C and a G together, it sounds
pretty good Musicians call this a "perfect fifth", and one musician in
particular liked it so much that he built a tuning system around it.

Pythagoras---yes, the one with the triangle theorem---figured that using the
ratios 2:1 and 3:2, you can build a whole bunch of notes that sound good
together (it's easy to do this kind of tuning for string instruments, because
the lengths are really easy). You do this by going up by the 3:2 ratio, and
then going down by a factor of 2 when it gets higher than 2. So, you get 1,
3/2, (9/4)/2 = 9/8, and so on. As a musician, you might recognize this as
"going up the circle of fifths".

We can then ask, "will going up the circle of fifths ever get us back to our
root note?" Obviously, the answer is no: to get back to the root note you need
to get a ratio of 1 again. But, every time you multiply by 3/2 you add a power
of 3 to the numerator, which will never cancel with the denominator. That is,
we are searching for an integer solution to the equation ($ (3/2)^x / 2^y = 1
$) which clearly does not exist.

However, we can get close! Recall from [A Balance of
Powers](a-balance-of-powers.html) that we can compute really good approximate
solutions for these equations by taking logaritms and using Diophantine
approximation techniques. The first convergent yields x=5 and y=3, which gives
us a ratio of 243/256, or around 0.95. This is pretty bad: the difference is
clearly audible (in fact, it's approximately the difference between a C and a
C#). The second convergent, however, yields x=12 and y=7, which gives us a
ratio of 531441/524288, or around 1.01. This is much better---it's much harder
to hear the difference!

So, twelve fifths gets us reasonably close to the root note: and that's where
our 12-note chromatic scale comes from.

Unfortunately, there were problems with this scheme. The most urgent problem
was that it lacked symmetry: you can only play in "C". If you start a song on
"D", everything sounds awful because the ratios don't work the same relative to
"D". In theory we could start all our songs on "C", but that makes it hard for
singers with different ranges, and also prevents composers from modulating to a
different key.

With this issue in mind, people tried to come up with alternative tunings. One
such alternative was "well-tempering", which is what Bach really loved. He
wrote *The Well-Tempered Clavier* to show off well-tempering: he has a prelude
and fugue in each key, and I'm told that that each piece takes advantage of the
subtle tuning tendencies of its respective key.

The big winner turned out to be "even tempering". Even tempering spaces out the
12 notes of the scale evenly. Since the top note is twice the frequency of the
root note, each consecutive pair of notes in the even-tempered scale differs by
a ratio of ($ 2^{(1/12)} : 1$), which is around 1.06. Crucially, the difference
between "C" and "D" is the same as that between "D" and "E", so if you start a
song on "D" instead of "C", everything still fits. Furthermore, even tempering
frequencies don't stray *too* far from the Pythagorean frequencies, so
everything still sounds good! Well, except for the occasional connoisseurs who
complain that they can hear the difference.

---

But, we have strayed from the original goal: we wanted lots of simple
whole-number ratios. Does the 12-note even tempering achieve that?

Well, I wrote a Python program that calculates a "pleasantness score" for each
n-note even tempering. The pleasantness score takes a set of whole-number
ratios (Pythagorean ratios, mostly), and returns the total error a tempering
achieves with respect to those whole-number ratios. Clearly, a million-note
even tempering would have a very low total error, because it is off by at most
a millionth for each ratio.

```python
>>> ratios = [3/2, 4/3, 5/3, 7/5] # for example
>>> def score(n):
>>> ...     total = 0
>>> ...     for r in ratios:
>>> ...             total += min([(2**(1.0*i/n) - r)**2 for i in range(n)])
>>> ...     return total
>>>
>>> for i in range(2, 32):
>>> ...     print i, '\t',  '%10.2f' % (1/score(i))

n      1/score
--------------
2        12.85
3        25.68
4        69.78
5        80.27
6        51.99
7       252.74
8       282.14
9       182.01
10      413.60
11      249.02
12     2293.78
13      267.00
14      811.75
15     1277.37
16      711.44
17      785.59
18      550.84
19     5030.16
20     1150.78
21      901.15
22     2531.40
23     1238.07
24     2293.78
25     1182.83
26     2645.21
27     6829.60
28     1274.03
29     4398.47
30     1520.35
31    14003.10
```

It turns out that for almost any set of simple ratios you pick, 12 notes has a
significantly better score than anything before it! Note that after 12, you can
do better with a 19-note scale, and even better with a 31-note scale. I do not
know why 12, 19, and 31 work out so well: but they do. 19 and 31 in particular
are very nice because they are prime. So, you can do a "circle of fifths" with
just about any ratio: a "circle of thirds", for example. Both 19- and 31- note
even temperings were explored by Joel Mandelbaum in the 1900s (so, I'm not the
first person to have figured this out).

If you're curious, you can find a piece of 19-note music, *Truth on a Bus*,
[here](http://sethares.engr.wisc.edu/mp3s/truthonabus.html) and a piece of
31-note music, "Music fur die 31-Stufige Orgel",
[here](https://www.youtube.com/watch?v=23ImVLezV4c), which is played on a
31-note Fokker organ.

And *that* is why we're currently building a 19-note marimba for our jazz band.
