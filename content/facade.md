I think the best way to begin this article is by quoting James Mickens:

> [Cryptographers] are like smarmy teenagers who listen to goth music: they are
> full of morbid and detailed monologues about the pervasive catastrophes that
> surround us, but they are much less interested in the practical topic of what
> people should do before we're inevitably killed by ravens or a shortage of
> black mascara.

Now, I don't listen to goth music and I didn't even know "smarmy" was a word.
But I *am* a teenager and I *do* worry about the pervasive catastrophes that
surround us, including, but not limited to, the following three scenarios that
(for reasons beyond my control or understanding) I spent all winter break
contemplating.

> **Scenario 1:** The CEOs of ACME, Inc. and Ajax, Inc. both want to know
> whether or not the other one is willing to collude. But, they cannot ask the
> question outright: if ACME says "Ajax, I want to collude with you," then Ajax
> can use that message to get ACME in trouble with antitrust laws, and thus
> eliminate competition. So, both companies end up making less money than they
> would in an ideal situation.
>
> **Scenario 2:** Alice and Bob both want to go to prom with each other, but
> each is too afraid to ask the other. If Bob asks Alice to prom and Alice
> rejects Bob, then Bob is in trouble (socially). The same holds if Alice asks
> Bob. Game theoretically, each party has a higher expected payout by not
> playing the game. The only winning move is not to play: they never end up
> going to prom.
>
> **Scenario 3:** Alice is the world's best safecracker and Bob is the world's
> best hacker. If Alice and Bob were to work together, they could pull off a
> really lucrative heist. But neither one would suggest such a thing, because
> the other would rat him or her out: it's a round of potential-prisoners'
> dilemma. As a result, the heist never occurs, and the only thing the world is
> robbed of is another cheap crime novel "based on a true story."

Clearly, these scenarios are isomorphic in some way (no, not because they are
all potential Ryan Gosling movies). The common thread is the following: two
parties, each with a secret bit, wish to compute the logical AND of their bits
without revealing their individual bits. Neither party trusts the other, so
there is a deadlock and opportunities are missed. It's worse than that time Jim
and Della invited a bunch of philosphers for dinner. For that matter, this is
awkwardly reminiscent of that time the two most powerful nations in the world
decided to build lots of nuclear weapons.

Abstractly, what we have is a situation where mutually distrusting parties need
to orchestrate a secure transfer of sensitive information. This sounds like a
job for cryptography.

### Previous Work

Apparently Scott Aaronson solved this problem before I did. See
[here](http://stellar.mit.edu/S/course/6/sp08/6.080/courseMaterial/topics/topic1/lectureNotes/lec181/lec18.pdf).
S. Dukhovni, J. Weisblat, and I. Chung improved upon his work. Their solution,
the SENPAI protocol, can be found
[here](http://sigtbd.csail.mit.edu/pubs/veryconference-paper10.pdf).

The problem with both protocols is *asymmetry*: Bob learns the result of the
protocol before Alice does. This means that Bob can carry out the protocol by
inputting a "1", and obtain a proof that Alice also input "1", which, if Bob
were malicious, could be catastrophic for Alice's social life. Or, in the
isomorphic colluding-businesses case, ACME could obtain a proof that Ajax
intended to collude, and thus sabotage Ajax without completing the protocol.

In fact, if you think about it, *any* finite protocol should have this
weakness, because if you exchange information in a finite number of turns, then
at some point one person must have the proof before the other person (the act
of sending never creates information for the sender).

How can we solve this? I spent this winter break thinking deeply about this
problem. My result is a protocol that I named, following the tradition of
SENPAI, the FACADE (Feelings Are Complicated And I Don't Even) protocol. In
case of a "1" result, FACADE gives *both* parties some proof of the other's
guilt, thus solving the problem with SENPAI. Much like nuclear disarmament and
the formation of a friendship, both parties take turns making themselves a
little bit more vulnerable, until at last they reach a mutually-agreed-upon
level of nuclear and/or social détente.

Unfortunately, FACADE has some unfortunate quirks that I haven't been able to
iron out yet---more on that in a moment.

### How does FACADE work?

The FACADE protocol is based on Rabin's 1981 paper, [*How to Exchange Secrets
with Oblivious Transfer*](https://eprint.iacr.org/2005/187.pdf).

1. Alice creates a large semiprime *N = pq* and sends *N* to Bob.
2. Bob selects some 1 < *a* < *N* and sends Alice *s*, the square of *a* mod
   *N*.
3. Alice sends Bob exactly one square root *r* of *s* mod *N* (there are four
   possibilities; she randomly selects one).
4. With 50% probability, Bob can now factor *N* by computing the GCD of *N* and
   *r &plusmn; s*. If Bob's bit is "1" or if he *cannot* factor *N*, then he
   sends Alice *MAYBE*, otherwise he sends Alice *NO* followed by *p* and *q*.
5. The protocol repeats, with Alice and Bob's roles reversed. Each *MAYBE*
   increases the chances that the corresponding sender's bit is "1".
6. The protocol ends when one party sends a valid *NO* message, or when both
   parties are satisfied that both bits are "1".

The way the FACADE protocol works is by creating plausible deniability for
*MAYBE* responses. If Bob has sent 10 *MAYBE* messages, then

- If Bob's bit is "0", the probability of this occurring is less than one in a
  thousand.
- If Bob's bit is "1", the probability of this occurring is one.

In other words, each successive *MAYBE* makes it harder to believe that Bob's
bit is "0". However, Bob could still deny having a "1" bit and claim to be
extremely unlucky. Since he keeps *a* a secret, it is impossible for anyone to
tell whether or not he was "forced" to send *MAYBE*. Moreover, since Alice and
Bob alternate messages, if Alice decides to rat Bob out with her "evidence" of
*n* consecutive *MAYBE* messages from Bob, then Bob can retaliate by showing
*n-1* consecutive *MAYBE* messages from Alice, which should be good enough to
convince a jury that neither (or both) of them were up to no good.

### *Why* does FACADE work?

For completeness, I want to briefly touch on the number theory behind Rabin's
oblivious transfer mechanism: why does this number-theoretic gymnastics make
sense?

When Bob generates *s*, it is a quadratic residue mod *N*, and consequently mod
both *p* and *q*. *s* has two square roots mod *p* and two square roots mod *q*
because a quadratic polynomial can only have at most two roots in the ring of
integers mod a prime, and we know that if *r* is a root then *-r* is also a
root. Using the Chinese Remainder Theorem on each pair, we can reconstruct a
total of four square roots mod *N*. (To find square roots mod the primes, Alice
can select primes such that both are congruent to 3 mod 4. Then, raising *s* to
the power *(p+1)/4* yields a square root of *s*. Showing that this works should
be easy if you know Fermat's Little Theorem.)

Now, Alice has no idea which of the four square roots Bob chose when choosing
*a*. So, she *must* report a random root. With probability 50%, that root *r*
will be *&plusmn;a*. Bob already knows this root, it's easy to compute! Let's
call this a *trivial* root: it means Bob can't really do anything new with this
information, because he already knew it.

However, if Alice chooses a *nontrivial* root *r*, then the difference of
squares of *a* and *r* is zero; that is, we have the equation *(a+r)(a-r) = 0*.
Since *r* is a nontrivial root, neither of the factors is individually equal to
zero: so, by Euclid's lemma, we must have *p* divide one of them and *q* divide
the other. That is, the GCD of *N = pq* and *a &plusmn; r* must be *p* or *q*,
and thus Bob can factor *N* easily.

In summary: Alice has no way of selecting a trivial (or nontrivial) root on
purpose, and thus Bob has a fair 50% chance of factoring *N*. Crucially, Alice
does not know whether or not Bob can factor *N* because she doesn't know
whether or not her root was nontrivial.

I think Rabin's oblivious transfer trick is one of the cleverest cryptographic
ideas ever, because of how elegantly it accomplishes something seemingly
impossible ("try to tell me something without knowing whether or not you told
it to me").

### Why *doesn't* FACADE work?

An unfortunate "gotcha" of this protocol is that it is not reusable, because
*all* previous *MAYBE* messages are fair game to be used as evidence against
the sender. Alice can keep knocking at Bob's door, getting a "1" response,
sending a "0" response, and eventually conclude that Bob's bit is "1".

Solving this problem is tough, because FACADE by nature inherently *does* leak
information. I experimented with strategies where you randomly choose to
pretend your bit is "0" every once in a while to throw off an adversary: that
turned out to be a fruitless endeavor since *any* such strategy will eventually
be detected by statistically analyzing a large enough set of transcripts
(convincing yourself of this is left as a fun exercise).

In any case, my opinion is that a one-time protocol is definitely better than
no protocol at all, and in each of the potential use-cases listed above, the
secret bits are unlikely to change in a short timeframe.

### Bonus protocol: TOXIC

TOXIC stands for "Two Operators eXchange Information Concurrently," and to be
perfectly honest it is kind of a cop-out because it requires both parties to be
present in the same physical space. But I think it's kind of clever anyway, and
it is definitely worth sharing with you, if only because it is fun to imagine.

1. Alice prepares a concentrated lead nitrate solution (solution A) and Bob
   prepares a concentrated sodium chloride solution (solution B). Note that
   both solutions are clear and visually indistinguishable from distilled
   water.
2. In beaker A, Alice adds a quantity of either solution A or distilled water,
   depending on whether her bit is "1" or "0", respectively.
3. In beaker B, Bob adds a quantity of either solution B or distilled water,
   depending on whether his bit is "1" or "0", respectively.
4. Alice and Bob simultaneously empty their beakers onto a large plate.
5. The result of the protocol is "1" if a precipitate forms, and "0" if it does
   not.
6. The result is immediately washed out to dispose of any evidence.

As long as you discard the result immediately, there is no way for anyone to
know what the contents of beaker A and beaker B were. I suppose in practice an
adversary could use some high-tech forensics (e.g. licking the beaker with
their tongue) to recover some information, but in practice you shouldn't be
doing sketchy protocols in a chemistry lab anyway.

### Open questions

One of my favorite blogs, GLL, closes each post with a set of open questions. I
think that is a lovely tradition, and so I invite you to ponder the following
with me:

What other applications are there for this type of protocol? What other flaws
are there in FACADE, and are there ways to fix them? How, at a fundamental
level, is the FACADE protocol related to the concept of a zero-knowledge proof,
or to that of homomorphic encryption? *What makes this problem hard?*
