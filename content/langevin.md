Surely _something_ will happen --- which means that if you integrate over all
possible outcomes, the probabilities must add up to 1. This elementary fact
remains true, even if the probabilities of the outcomes change for some reason.
Are you reminded of something? _Fluids_ behave in the same way: no matter how
the particles are distributed, the total quantity of fluid is conserved, which
means that if you integrate over all of space, the masses must add up to 1.
Indeed, when we talk about _probability density functions_ and _probability
mass functions_, we are borrowing fluidic vocabulary.

I get excited about analogies like this, where the physics of one domain
promises to unexpectedly deliver insight into a different domain. Another
example of this is how spring constants and capacitances play the same
mathematical role in the differential equations that model their respective
mechanical and electrical systems. Harry Olson's wonderful book [_Dynamical
Analogies_](https://archive.org/details/DynamicalAnalogies) shows some more
beautifully-illustrated examples of mechanical, electrical, and acoustic
systems with identical dynamics.

Can we get any mileage out of the probability-fluid analogy? It turns out,
_yes!_ We can apply our physical intuition about fluids to design a clever
statistical machine learning algorithm. That's the subject of this piece. By
the way, you can undoubtedly find better (and more correct) expositions of this
math in other places; my goal here is to emphasize the interaction between
physical intuition and probabilistic applications, bridged so beautifully by
the fluidic analogy.

A little bit about the problem setup: sometimes, when working with data, you
find yourself in a place where you want to sample from a probability
distribution $p(x)$. This might not be so bad if you can compute $p(x)$ exactly
--- for example, you can use rejection sampling or something. Often, however,
you can only compute some scaled quantity $q(x)$ such that $p(x) \propto q(x)$
with some unknown constant of proportionality. Commonly, this happens in
Bayesian inference, where you may want to sample from $\pi(x \mid y) =
\pi(x,y)/\pi(y)$ where $y$ might be data you've seen and $x$ might be the
parameters to your model. Here, the problem is that the normalizing constant
$\pi(y)=\int \pi(x,y)dx$ is hard to compute because that integral is
intractable in high dimensions.

One famous way to do this kind of sampling is by the Metropolis-Hastings
algorithm, which approximates $p(x)$ with the stable distribution of a Markov
chain. The "miracle" of the algorithm is that the transition probabilities
between two states only depend on the _ratios_ of the probability densities at
those states --- the unknown constant simply cancels out!

But now let's think about this from a fluids perspective. Have unknown
normalizing constants popped up in physics anywhere? Yes! The partition
function $Z$ in Boltzmann is often unknown. Recall that a system at
thermodynamic equilibrium at temperature $T$ has probability $p_i \propto
e^{-U_i/k_BT}$ of being in state $i$, where $U_i$ is the potential energy of
that state and $k_B$ is a physical constant that you can find, e.g. on
Wikipedia. A curious application of this distribution is working out how thin
the atmosphere is at altitude $h$ by reasoning about $U_h$ being the
gravitational potential energy at altitude $h$: because $U$ is linear in $h$,
we can instantly conclude that atmospheric density decreases exponentially in
altitude.

But returning to machine learning, here is the insight that the fluidic analogy
makes possible: if we set $U(x) = -\log q(x)$ then a particle simulated at some
"temperature" $T=1/k_B$ in potential $U$ would eventually have probability
$e^{-U(x)}=p(x)$ of being at $x$. So, we can use what we know about the
dynamics of particles that are a part of a fluid at thermal equilibrium, to
sample from probability distributions that may have nothing at all to do with
fluids.

What exactly does it mean to "simulate a particle" of this probability fluid?
You can take those words pretty literally, as it turns out. There are two
sources of motion at each timestep: $U$ and $T$. Given potential $U(x)$, we can
derive the force $-\nabla U$ that acts on our particle, and then apply Newton's
Second Law to infer the velocity. We'll assume that velocity is roughly
independent between timesteps because the particle is repeatedly being bumped
around by other particles and having its velocity reset --- so, no need to
track acceleration. By the way, notice that $\nabla \log q(x)$ doesn't depend
on the unknown normalization constant, because the logarithm turns it into an
additive constant, which disappears under the derivative.

As for the effect of $T$, we can model the thermal motion of the particle as
Brownian motion: that is, at each time, the particle gets bumped to some random
neighboring position drawn independently from a Gaussian that is somehow scaled
with respect to "temperature" $T$. (How do we translate $T=1/k_B$ to this
un-physical world where "joules" and "kelvins" make no sense? Stay tuned…)

This fluidic analogy leads us to what people call the "Unadjusted Langevin
Algorithm." The algorithm is quite simple to state and implement:

1. Initialize some $x_0$.
2. Using some small step size $\Delta t$ integrate $\Delta x = \Delta t \cdot
   \nabla\log q(x_t) + \sqrt{2\Delta t} \cdot \xi_t$ where you sample $\xi_t
\sim N(0,1)$; the Greek letter $\xi$ is chosen for maximum squiggliness, in
order to act as a visual metaphor for its function. Importantly, this step only
requires you to evaluate the unnormalized density $q$!
3. That's it — under some (not _too_ mild but still reasonable) assumptions,
   snapshots of the trajectory $\{x_t\}$ are distributed accoding to $p(x)$!

Are you convinced? Here's a sanity check: without the stochastic component
$\sqrt{2\Delta t}\cdot\xi_t$ at each step, $x_t$ deterministically walks
towards the maximum likelihood estimator --- that is, without the stochastic
component, we'd have invented gradient descent! The stochasticity, however,
makes $x_t$ a random variable instead.

---

The rest of this piece is dedicated to answering the question: where does that
stochastic coefficient $\sqrt{2\Delta t}$ come from? You might have already
worked out that it's the magnitude of the thermal motion, which depends on $T$.
If that coefficient were too small, then, as we just discussed above, we simply
have gradient descent: our particle is analogous to a marble rolling down a
(syrupy --- overdamped!) hill. If the coefficient were too large, then thermal
motion would dominate and the "signal" from the potential $U$ would stop
mattering. So, clearly, the threshold $\sqrt{2\Delta t}$ is "special" in some
way.

First let me convince you that we want this coefficient to indeed be
proportional to $\sqrt{\Delta t}$, even though it looks dimensionally wrong
when placed in a sum right next to the $\Delta t\cdot\nabla \log q$ term.
What's going on? It turns out that this "lots of little Gaussian bumps" motion
doesn't have an intuitive integral calculus. In particular, for Gaussians, it's
the _variance_ that adds, not the standard deviation. So in time $t$ the
variance of the total distance traveled would be $\Sigma\sqrt{\Delta t}^2 =
\Sigma \Delta t = t$, and therefore the standard deviation would be $\sqrt{t}$,
which is exactly what we want for the algorithm to be invariant to how small
$\Delta t$ is. (For more on this, you could read about "Wiener processes.")

Now for the "2." To derive this value, let's return to our fluidic analogy.
Suppose we wanted to compute the change in probability density at a point $x$
over time, that is, ${\partial p(x,t)}/{\partial t}$, with the understanding
that we will set this time derivative to zero later to reason about the
system's behavior at equilibrium. By following the fluidic analogy, we can
hallucinate a "probability flow" $\vec{J}(x, t)$ and assert, by Gauss' Law,
that ${\partial p}/{\partial t} = -\nabla \cdot \vec{J}$.

To measure $\vec{J}(x, t)$, we should think about what's flowing; that is,
about "particles," whose dynamics is given by the Langevin update rule for
$\Delta x_t$ I wrote out above. The deterministic part is easy to deal with:
from a tiny region of volume $\Delta V$, a mass $p\Delta V$ of particles leaves
with velocity $\nabla\log q$, so the flux is $p\nabla \log q$.

For the stochastic part, notice that the dynamics of the thermal motion are
spatially invariant, i.e. independent of $x$. So, whatever amount diffuses out
of $\Delta V$ is proportional to $p$, and whatever amount diffuses in is
proportional to the density in the neighborhood of $\Delta V$: this means the
net flow is proportional to $-\nabla p$. When we talk about fluids, this
observation is also known as Fick's Law, and the constant of proportionality is
called the diffusion coefficient $D$.

How can we compute $D$? Looking at only the stochastic part, we have $\partial
p/\partial t = -D\nabla^2 p$, which we recognize as the heat equation. That is,
for this brief aside, we're going to think of $p$ representing --- not
probability over Bayesian model parameters _or_ fluid density in a potential
well, but --- heat in a block of metal --- a bonus analogy!

Thankfully, the solution to the heat equation turns out to be well-known: it is
a time-varying Gaussian. And it better be! After all, the stochastic diffusion
is just a sum of lots of independent little Gaussian-sampled steps of variance
$\Delta(\sigma^2) = {2\Delta t}$, which together form a big Gaussian of
variance $\sigma^2 = 2t$, as discussed above. But let's say we didn't know the
coefficient was 2. Let's set it to $a$ instead. Now, if we know that $p(x,t) =
e^{-x^2/2(a t)}/\sqrt{2\pi(at)}$, then we can literally take the partial
derivatives on both sides of the heat equation and expand to solve for $D$. A
miracle occurs, and many things cancel, leaving us with simply $-D=a/2$. It's
not worth writing out the algebra here: I encourage you to try it yourself,
since it is that rare combination of straightforward and satisfying. But
furthermore, it gives some mechanical (if not physical) insight into the "2"
that appears in the denominator of the result: algebraically, the $-1/2$ power
of $at$ in the normalization constant $1/\sqrt{2\pi(at)}$ kicks out some
factors of two that are _not_ balanced by the $-1$ power of $t$ in the
exponential.

In any case, though, we conclude from the above that $\Delta p = -(a/2)\Delta t
\nabla^2 p$, which means the stochastic flux is simply $\nabla p$. Perhaps it's
all clear to you by now, but let's take this over the finish line. Putting
these two components together, $U$ and $T$, we have $\partial p/\partial t =
\nabla\cdot (p\nabla\log q-(a/2)\nabla p)$. This nice identity is known as the
Fokker-Planck equation (the devoted reader might note that this is the _second_
reference to Fokker on this blog).

Now, finally, as promised many paragraphs ago, we will now reason about this
equation at equilibrium. At equilibrium the distribution is static in time, so
we have $0 = \nabla \cdot (p\nabla \log q -(a/2) \nabla p)$. Assuming suitable
boundary conditions, we can assume the argument of the divergence is also zero,
so $\nabla \log q = (a/2)\nabla p / p$. Integrating in all directions, we have
$\log q + c = (a/2)\log p$, or rather $p \propto q^{2/a}$. This makes sense:
just as expected, for large $a$ the effect of $q$ is wiped out, and for small
$a$ all but the maximum value get squashed to zero. Crucially, however, if we
want $p \propto q$, then we must set $a=2$. Aha! So _that's_ why the thermal
motion needs to be scaled by $\sqrt{2\Delta t}$. (By the way, that constant of
integration above, $c$, oddly enough encodes that pesky normalization constant
that started off this whole discussion…)

---

Okay. I'm glad I got that out of my system, it's been rattling around for
weeks, now! How wonderful it is, that we can start with the simplest axiom of
probability --- "_something_ must happen" --- and, reasoning only with physical
intuition, reach a sampling algorithm that solves a real problem.
