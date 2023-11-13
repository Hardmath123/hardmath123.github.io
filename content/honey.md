I knocked over a tall jar of honey. Clumsy, clumsy! But the jar was nearly empty; jars tend to fall when they are nearly empty.

But jars also tend to fall when they are full, which got me thinking: for both full and empty jars, we can argue by symmetry that their center of mass is halfway up. By Rolle's Theorem, then, at some point when the jar is partially filled it should have a minimally- or maximally-high center of mass. It's easy to see that the center of mass can never get higher than halfway up. This suggests that the jar's stability increases and then decreases as the honey is consumed.

When is the jar most stable? Working in units where the empty jar's height and mass are 1, its radius is $r$, and honey's density is $\alpha$, the height of the center of mass is given by:
$$
c = \frac{\alpha r^2h(h/2) + 1/2}{\alpha r^2h + 1}
$$

Let's assume honey is extremely viscous (i.e. changes shape slowly), and that the jar tips over if its center of mass is over its rim. Then the maximum angle you can tip the jar before it falls over is:
$$
\theta^\star = \tan^{-1}(r/c)
$$
The question is then, for a given $r$ and $\alpha$, what $h$ maximizes $\theta^\star$? Intuitively, it seems like it should be somewhere halfway between empty and full.

We can compute the optimal $h$ by differentiating $\theta^\star$ with respect to $h$ and setting the derivative to zero:
$$
\frac{d\theta^\star}{dh}=-\frac{r^2}{r^2+c^2}\frac{dc}{dh} = 0
$$
The positive solution to this, thanks to WolframAlpha, is given by:
$$
h^\star=\frac{1}{1+\sqrt{\alpha r^2+1}}
$$
Does this make sense? As $\alpha r^2$ increases (heavier honey), the optimal height gets lower, which makes sense because the honey begins to have a ballasting effect.

Now we can plug in some numbers. A standard 8-oz honey bottle is about 6 inches tall, has a base radius of about 1 inch, and weighs about 1oz. The density of honey is 0.8oz per cubic inch. In our units, this means the jar's radius is $1/6$ and the density of honey is $0.8/(1/6)^3$. Plugging this in, we find remarkably that $h^\star \approx 0.3$. So a jar of honey is most stable when only about 1/3 full!

