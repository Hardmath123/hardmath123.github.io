Welcome to the 134th [*Carnival of
Mathematics*](http://aperiodical.com/carnival-of-mathematics/), a monthly
roundup of mathematics-related blog posts organized by [*The
Aperiodical*](http://aperiodical.com/). The previous edition was hosted by
Matthew at [*Chalkdust Magazine*](http://chalkdustmagazine.com/blog/).

Tradition obliges me to begin with some facts about the number 134.

One of my best friends works backstage at my high school's theater. He has a
grueling and often thankless job, which involves staying backstage till
midnight painting sets only to watch the actors get the applause the next
evening. But he does it anyway, because he honestly loves it.

He reminds me of the number 134: the stage tech of numbers, enabling primes to
shine without ever being recognized as one.

134 is the average of two consecutive odd primes, and both its double and its
square are one less than a prime. The number
134<sup>4</sup>+134<sup>3</sup>+134<sup>2</sup>+134<sup>1</sup>+134<sup>0</sup>
is prime, as is 10<sup>134</sup>+7. The sum of the first 134 primes divides the
product of the first 134 primes, and the sum of squares of 134's prime
factors... is prime.

Yet a number does not have to be prime to be special. 134 redeems itself by
having the beautiful property,

\\[ \binom{1+3+4}{1} + \binom{1+3+4}{3} + \binom{1+3+4}{4} \\]

And now, the Carnival.

---

Writing this edition of the Carnival felt like writing a series of book
reviews, but instead of dull Victorian literature, I got to review exciting
mathematics written by fellow bloggers around the world. To celebrate this, I'd
like to begin this roundup with a rather thought-provoking book review---of an
actual book.

- **Tanya Khovanova**
[reviews](http://blog.tanyakhovanova.com/2016/05/really-big-numbers/) a book
about really big numbers, called (funnily enough) *Really Big Numbers* by
Richard Schwartz.

> I received a book *Really Big Numbers* by Richard Schwartz for review. I was
> supposed to write the review a long time ago, but I've been procrastinating.
> Usually, if I like a book, I write a review very fast. If I hate a book, I do
> not write a review at all. With this book I developed a love-hate
> relationship.

The same blogger also writes about her feelings towards math, and I would like
to mention one such article.

- **Tanya Khovanova**
[discusses](http://blog.tanyakhovanova.com/2016/04/the-battle-i-am-losing/) how
it's sad that we give away answers to puzzles too easily:

> I remember I once bought a metal brainteaser that needed untangling. The
> solution wasn't included. Instead, there was a postcard that I needed to sign
> and send to get a solution. The text that needed my signature was, "I am an
> idiot. I can't solve this puzzle." I struggled with the puzzle for a while,
> but there was no way I would have signed such a postcard, so I solved it. In
> a long run I am glad that the brainteaser didn't provide a solution.
> ...[T]here are no longer any discoveries. There is no joy. People consume the
> solution, without realizing why this puzzle is beautiful and
> counterintuitive.

Perhaps appropriately, the next entry is a puzzle, and its creator (who
describes himself as a "stand-up mathematician"!) admits to not knowing the
answer.

- **Matt Parker** [poses](https://www.youtube.com/watch?v=xHh0ui5mi_E) a puzzle
about fairly mapping dice rolls in an elegant way.

<iframe width="560" height="315" src="https://www.youtube.com/embed/xHh0ui5mi_E?rel=0" frameborder="0" allowfullscreen></iframe>

For completeness, I also include an article about *solving* a puzzle---about
the joy of discovery and the frustration of exploring large search spaces.

- **Oliver Dunk**
[hunts](http://chalkdustmagazine.com/blog/hunting-for-polydivisibles/) for
polydivisible numbers, whose first N digits are divisible by N.

> I'm a software developer myself and so the most interesting part for me was
> finding shortcuts to the answer. While a computer can find the solution by
> brute force fairly quickly, it still takes a bit of time as there are
> 3,628,800 possible answers to check. ... I read a little further, and found
> out that indeed there were shortcuts that could be made—this is the power of
> mathematical thinking in problem-solving: a monumental task can become
> considerably easier by simply applying a little bit of thought.

---

As we all know, mathematics isn't just about solving brain-teasers. With that
in mind, here are some practical applications of math.

- **Greg Ross**
[summarizes](http://www.futilitycloset.com/2016/05/08/travel-delays/) what we
know about optimal airplane-loading strategy.

> What's the most effective strategy for loading an airplane? Most airlines
> tend to work from the back to the front, accepting first the passengers who
> will sit in high-numbered rows (say, rows 25-30), waiting for them to find
> their seats, and then accepting the next five rows, and so on. Both the
> airline and the passengers would be glad to know that this is the most
> effective strategy. Is it?

On a less serious but equally practical note, we can apply math to almost any
game you can think of.

- **Ana Swanson**
[shows](https://www.washingtonpost.com/news/wonk/wp/2015/05/08/how-to-win-any-popular-game-according-to-data-scientists/)
how to win at 14 games using some clever infographics.

> From Risk to tic-tac-toe, popular games involve tons of strategic decisions,
> probability and math. So one happy consequence of being a data nerd is that
> you may have an advantage at something even non-data nerds understand:
> winning.

---

While applying math to games is practical (and perhaps even lucrative!) we all
know that the proof of the pudding lies... in proofs. Proofs are there to
reassure us that a statement really is true.

- **Matthew Scroggs** [shares](http://www.mscroggs.co.uk/blog/27) several
proofs of Pythagoras' Theorem.

> Pythagoras's Theorem is perhaps the most famous theorem in maths. It is also
> very old, and for over 2500 years mathematicians have been explaining why it
> is true.

Thinking about it, perhaps I lied to you. Often, the most beautiful proofs are
there, not to reassure us, but to explain why a seemingly ridiculous statement
might actually be true. Here is one such outrageous statement and its proof.

- **Paul Hankin** [explains](http://paulhankin.github.io/Fibonacci/) a
fascinating formula for the Nth Fibonacci number:

> This code, somewhat surprisingly, generates Fibonacci numbers.
> ```
> def fib(n):
>     return (4 << n*(3+n)) // ((4 << 2*n) - (2 << n) - 1) & ((2 << n) - 1)
> ```
> In this blog post, I'll explain where it comes from and how it works.

However, proofs are often written in scary, technical language with no
intuition behind them. In reality, a proof is a narrative, and what better way
to present a narrative than a story? The next entry takes on the challenge.

- **Dan McQuillan**
[proves](http://voices.norwich.edu/daniel-mcquillan/2016/04/28/a-parity-theorem-for-drawings-of-complete-graphs/)
Kleitman's parity theorem for complete graphs---the number of crossings in a
"good" drawing of the complete graph of (odd) n vertices has the same parity as
"n choose 5".

> This may seem much harder than just counting the crossings, but it works well
> on an abstract level---that is, when we don't know what the drawing looks
> like, but still have to prove things about it. This is what makes the theorem
> and its proof beautiful---we will prove there is something common to
> infinitely many different drawings of K_5. ... This presentation is a first
> attempt at a response to the criticism: "Why don't mathematicians or
> scientists ever write the way they think?" In fact, this "unnecessarily" long
> exposition does not mean that it is difficult; my hope is quite the opposite.

---

While an appreciation for proofs is healthy for any mathematician, some
fascinating mathematics can emerge from seat-of-the-pants conjectures,
calculations, and manipulations.

- **Stephen Wolfram**
[recounts](https://backchannel.com/who-was-ramanujan-83b4d5b05665#.6pfebmx1p)
the story of Ramanujan and his unique approach to mathematics, coinciding with
the release of the film *The Man Who Knew Infinity*.

> For most people it'd be bad news to end up with some complicated expression
> or long seemingly random number — because it wouldn't tell them anything. But
> Ramanujan was different. Littlewood once said of Ramanujan that "every
> positive integer was one of his personal friends." And between a good memory
> and good ability to notice patterns, I suspect Ramanujan could conclude a lot
> from a complicated expression or a long number. For him, just the object
> itself would tell a story.

While we're on the topic of biographies, here's another interesting character
in the history of math.

- **Siobhan Roberts**
[tells](http://www.newyorker.com/tech/elements/claude-shannon-the-father-of-the-information-age-turns-1100100)
us about Claude Shannon, the father of information theory, who turns 100 this
year.

> ...Shannon built a machine that did arithmetic with Roman numerals, naming it
> THROBAC I, for Thrifty Roman-Numeral Backward-Looking Computer. He built a
> flame-throwing trumpet and a rocket-powered Frisbee. He built a chess-playing
> automaton that, after its opponent moved, made witty remarks. Inspired by the
> late artificial-intelligence pioneer Marvin Minsky, he designed what was
> dubbed the Ultimate Machine: flick the switch to "On" and a box opens up; out
> comes a mechanical hand, which flicks the switch back to "Off" and retreats
> inside the box.

---

Often, the most brilliant mathematicians are not the most adept at solving
equations, but the most insightful in finding math in places you may never have
dreamed of.

- **Daniel J. Heath**
[narrates](https://community.plu.edu/~heathdj/GeometryGames/SymmetricMusic.html)
a beautiful story involving one of his students, R. Brandon Meyers, and his
final essay on mathematical symmetry in the everyday world.

> Several students came to speak with me about the essay, including the second
> author. He told me that he just didn't see any symmetry around him. At the
> time, we were standing in a building (the cafeteria) with sine-curve shaped
> ceiling beams arranged in parallel, supported by arms with 4-fold rotational
> symmetry. The light fixtures were hemispherical, with slits cut out in in an
> 8-fold rotational pattern. Parallel sliced kiwi fruits were being served,
> with their near rotational symmetry. I merely pointed these things out,
> saying that we are surrounded by symmetry, all we need to do is look and
> listen.

And, for a completely different perspective, here's a lighthearted webcomic to
bring a humorous end to this edition of the Carnival of Mathematics.

- **Zach Wienersmith** [provides](http://smbc-comics.com/index.php?id=3777)
some funny translations of what people really mean when they say "math is
everywhere".

---

That's all for this edition of the Carnival of Mathematics! Join us next time
for the 135th edition, hosted by
[*Gaurish4Math*](https://gaurish4math.wordpress.com).
