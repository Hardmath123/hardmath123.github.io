Suppose two Bayesians, Alice and Bob, put on a variety show where they take
turns tossing a biased coin and announcing outcomes to a live studio audience.
(Bayesians love this kind of thing—it keeps them entertained for hours…)

Unfortunately, just as Alice goes on stage, she realizes with dread that she
forgot to bring the coin. Thinking on her feet, she mimes pulling a tiny
imaginary coin out of her pocket, and says "This is a biased coin!" It
works—the audience buys it and the crowd goes wild.

She mimes tossing the pretend coin and randomly announces "heads" or "tails."
Then, she hands the coin to Bob, who (catching on) also mimes a toss. This has
just turned into a Bayesian improv show.

But now Bob has a problem. Should he announce "heads" or "tails"? He could
choose uniformly at random, but after many rounds the audience might get
suspicious if the coin's bias is too close to 50%. How can he keep up the
charade of a *biased* coin?

Here's what Bob does. In the spirit of "yes, and...," he infers the coin's bias
based on Alice's reported outcome (say, with a uniform prior) and samples a
fresh outcome with that bias. So if Alice said "heads," Bob would be a bit
likelier to say "heads" as well.

Then Alice takes the coin back and does the same, freshly inferring the coin's
bias from the past *two* tosses. In this way, the two actors take turns
announcing simulated outcomes to the oblivious audience, while building a
shared understanding of the coin's bias.

What happens? How can we characterize the sequence of outcomes? Intuitively, we
might expect either a "rich-get-richer" effect where they end up repeating
heads or tails. Or we might expect a "regression-to-the-mean" where they
converge to simulating a fair coin.

The surprising answer is that this process is indistinguishable from Alice and
Bob tossing a *real* coin with fixed bias (chosen uniformly). A critic lurking
in the audience would never suspect something afoot!

This result is a consequence of the correspondence between the Pólya
distribution and the Beta-binomial distribution.

I have a hunch that this observation could be useful: perhaps in designing a
new kind of cryptographic protocol, or perhaps in explaining something about
human cognition. If you have ideas, let me know!


***

Proof sketch: Model the actors' belief with a Beta distribution with parameters
$(h, t)$ initialized to $(1, 1)$, i.e. uniform. At each toss the probability of
heads is given by $h/(h+t)$, and the outcome increments $h$ or $t$ by 1. You
can think of this as a Pólya urn with h black and t white balls: each time you
draw a ball, you put it back and add a "bonus" ball of the same color. It is
well-known (look
[here](https://djalil.chafai.net/blog/2015/11/30/back-to-basics-polya-urns/) or
[here](https://math.uchicago.edu/~may/REU2013/REUPapers/Helfand.pdf) or
[here](https://www.randomservices.org/random/bernoulli/BetaBernoulli.html))
that this is the same as the Beta-binomial process.

> See also: [cool new blog post that riffs on these
> ideas](https://a.exozy.me/posts/asian-bayesian-2/)
