I was in Los Angeles over winter break, and on the long drive back home I began
thinking about a billboard I saw just at the edge of the city advertising the
**"closest casino to anywhere in LA."**

This is a fascinating claim. Let me rephrase it, at least the way I interpret
it: the claim is that _wherever_ you are in LA, the closest casino is the one
advertised on the billboard. (This is confusingly distinct from the claim that
the casino is closest to _anywhere_ in LA, in the sense that the placement of
the casino minimizes the distance to the nearest bit of LA soil. Of course,
practically speaking this latter claim is useless because any casino _within_
LA trivially has the minimal distance of zero to "anywhere in LA.")

The question is this: what region does the billboard's claim imply is devoid of
casinos?

Let's start with a simple case to get some intuition. Suppose LA is a
15-mile-radius disk, and the casino is at the center of the disk. Then,
according to the billboard, there must be _no_ other casinos within LA's
15-mile radius (otherwise, if you were in LA, you _might_ be closer to that
other casino!). But actually, the claim is quite a bit stronger: there cannot
be any casinos within _thirty_ miles of the center. Why? Well, suppose there
was a casino 20 miles from the center of LA. Then, someone just within the city
borders would be 5 miles away from that _other_ casino, but 15 miles from the
city-center casino.

One more simple case: suppose LA is a line segment of length 15 miles, and the
casino is located at one endpoint. Can you imagine what the region in question
must be? It is a disk of radius 15 miles, centered at the _other_ endpoint!
This is not entirely obvious, and you might need to draw a picture to convince
yourself that this is true.

Now let's consider a much trickier case: suppose LA is a circle again, but the
casino is located along the _circumference_. Suddenly, it's _much_ harder to
picture what's going on --- sitting in a car without pencil or paper, I had no
idea what the region might look like. My instinct was "circle centered at the
diametrically-opposite point on the circumference," but it turns out that this
is _wrong!_

In the rest of this post, we'll build up some mathematical machinery to answer
this question correctly. If you don't want to work through the math, however,
then feel free to just scroll to the red-bordered squares and enjoy the
interactive demos.

---

**Definition.** Given some region ($ R \subset \mathbb{R}^2 $), the _casino
closure_ with respect to some point ($ p \in \mathbb{R}^2 $) is defined as

\\[
R^p = \left\\{
  c \in \mathbb{R}^2 ~\middle|~
  \exists z \in R, || p - z || > || c - z ||
\right\\}
\\]

Or, informally: the casino closure is the set of _possible casino locations_ ($
c $) such that there exists a person ($ z $) in the region ($ R $) who is
closer to ($ c $) than to ($ p $).

From here on out, I'm only going to worry about "nice" regions, i.e. closed,
connected regions with smooth boundaries. I'm also going to use ($ x, p, z, c
$) to range over points in ($ \mathbb{R}^2 $), but really most math that
follows is equally applicable in ($ \mathbb{R}^n $). It's just harder to
visualize.

**Lemma.** Let the disk ($ D(z, r) $) be the set of all points in ($
\mathbb{R}^2 $) within ($ r $) of point ($ z $). Then,
\\[
R^p = \bigcup\_{z~\in~R} D(z, ||p - z||)
\\]

That is, we can construct ($ R^p $) by combining all the disks at all the
points in ($ R $) that have ($ p $) on their circumference.

**Proof sketch.** This should make sense "by construction." If point ($ c $) is
in this constructed ($ R^p $), then it lies in some disk ($ d $), and thus the
point ($ z \in R $) that created disk ($ d $) fulfills the existence criterion
of our definition.

**Lemma.** If region ($ R $) has a boundary ($ B \subset R $), then ($
B^p = R^p $).

**Proof sketch.** Clearly, ($ B^p \subset R^p $) if you believe the first lemma
--- adding more points to ($ B $) should only increase the union of disks.

The harder direction to show is ($ R^p \subset B^p $). Consider some point ($ z
\in R$). Extend the ray ($ \overrightarrow{pz} $) until it intersects with ($ B
$) at point ($ z^\prime $). Then, we can relate the disks created by ($ z $)
and ($ z^\prime $): ($ D(z, ||p-z||) \subset D(z^\prime, ||p-z^\prime||) $).
Why? Because the disk from ($ z $) is smaller and internally tangent to the
disk from ($ z^\prime $).

Mapping this argument over the entire union, it makes sense that ($ R^p \subset
B^p $).

Okay, time for some empirical verification of all this theory. Try drawing the
boundary of a region (in black) here! The disks will show up in red. Notice how
filling in your region with black dots doesn't change the red blob at all.
(Click to clear.)

<canvas id="world-freestyle" width=300 height=300 style="border: 1px solid red;"></canvas>

---

The boundary-circle lemma gives us a nicer characterization of ($ R^p $): it is
the region bounded by the curve that is tangent to all of the disks created by
the points on ($ B $). It turns out that there is a very nice mathematical
theory of "the curve that is tangent to all curves in a given family of
curves," and that is the theory of _envelopes_. The account below is
paraphrased from ["What is an
Envelope?"](https://www.jstor.org/stable/3617131?seq=1#metadata_info_tab_contents),
a lovely 1981 paper.

Let the function ($ F(x, t) : \mathbb{R}^2 \times \mathbb{R} \rightarrow
\mathbb{R} $) define a family of curves parameterized by ($ t $), in the sense
that ($ F(x, 0) = 0 $) defines a curve and ($ F(x, 1) = 0 $) defines another
curve, and so on. Then, we seek to characterize the envelope curve which is
tangent to every curve in ($ F $).

**Lemma.** If the boundary of ($ R $) can be (periodically) parameterized as ($
B(t), t \in \mathbb{R} $) then the boundary of ($ R^p $) is the _envelope_ with
respect to ($ t $) of
\\[
F(x, t) = || x - B(t) ||^2 - || p - B(t) ||^2
\\]

**Proof sketch.** Again, this should make sense "by construction": ($ F $) is
chosen to correspond to circles centered at ($ B(t) $) passing through ($ p $).

---

Ah, but how do we find the envelope? Here we need a tiny bit of multivariable
calculus.

Let ($ X(t) $) be the parameterization of the envelope of ($ F $). Then for all
($ t $), we have that ($ F(X(t), t) = 0 $) because the envelope must lie on the
respective curve in the family ("tangent" means "touch"!). We also have that
the curve ($ X(t) $) must be parallel to the member of family ($ F $) at ($ t
$). We can then express this condition by saying that the gradient (with
respect to ($ X $)) of ($ F $) at ($ t $) is perpendicular to the derivative of
($ X $) at ($ t $). Or:

\\[
d X(t) / dt    \cdot    \nabla_X F(X(t), t) = 0
\\]

In two dimensions, with ($ X(t) = (x(t), y(t)) $), this equation manifests
itself as ($ x^\prime(t)\partial F(x, y, t) / \partial x + y^\prime(t)\partial
F(x, y, t) / \partial y $).

The left hand side is oddly reminiscent of the multivariable chain rule.
Indeed, if we took the partial derivative of our equation ($ F(X(t), t) = 0 $)
with respect to ($ t $), we would get:

\\[
dF(X, t)/dt = dX/dt\cdot\nabla_X F(X, t) + dt/dt\cdot \partial F(X, t)/\partial t = 0
\\]

So we must have ($ \partial F(X, t) / \partial t = 0$).

There is a simpler but less rigorous derivation if you believe that the
envelope is exactly the points of intersection of infinitesimally close curves
in the family ($ F $). Then we want every point ($ X $) on the envelope to
satisfy both ($ F(X, t) $) and ($ F(X, t + \delta) $) for some ($ t $) and some
infinitesimal ($ \delta $). Taking the limit as ($ \delta $) approaches zero
gives the same condition that ($ \partial F(X, t) / \partial t = 0 $). The
paper above discusses how this notion is subtly different in some strange
cases, but it suffices to say that for all "nice" ($ R $), we're fine.






**Almost-a-theorem.** The boundary of ($ R^p $) is given by the parameterized
vectors ($ X $) that satisfy ($ F(X, t) = 0 $) and ($ \partial F (X, t) /
\partial t = 0 $) for the ($ F $) defined above.

**Almost-a-proof-sketch.** Almost! In general, the solution for ($ X $) might
self-intersect, so we want to take only the "outermost" part of ($ X $). But
this is easy to work out on a case-by-case basis.

**Example.** Suppose ($ R $) is the unit disk centered at ($ (a, 0) $), and ($
p $) is located at the origin. Then ($ B(t) = (\cos t + a, \sin t) $) and ($ p
= (0, 0) $). We have

\\[
F((x, y), t) =
  ((x - (\cos t + a))^2 + (y - \sin t)^2) - ((\cos t + a)^2 + \sin^2 t)
\\]

\\[
F((x, y), t) = -2ax + x^2 - 2x\cos t + y^2 - 2y \sin t = 0
\\]

We also have

\\[
\partial F((x, y), t) / \partial t = 2x\sin t - 2y\cos t = 0
\\]

Solving these by eliminating ($ t $) is a simple exercise in polar coordinates.
Discover from the second equation that ($ t = \theta $), then recall that ($
r^2 = x^2 + y^2 $). The resulting boundary of ($ R^p $) is (almost!) the curve
($ r = 2(1 + a\cos\theta) $). In other words, it's (almost!) a limaçon! As ($ a
$) varies, the character of the limaçon varies, and at the critical points ($ a
= \pm 1 $), we get a cardioid with a cusp. Beyond those critical points, the
curve has an inner loop that we have to ignore; hence, "almost!"

Okay, time for more empiricism. Move your mouse around in the square below to
see how the relative placement of LA and the casino affects the envelope.
Notice also the inner loop predicted by the envelope, which we should of course
ignore for the purposes of bounding ($ R^p $).

<canvas id="world-cardioid" width=300 height=300 style="border: 1px solid red;"></canvas>

An amazing fact is that a cardioid is the same shape you get on the surface of
your coffee mug when you put it under a light! Well, not quite --- it depends
subtly on where the light source is. Read more about caustics at
[Chalkdust](http://chalkdustmagazine.com/features/cardioids-coffee-cups/), from
whom I also borrowed the image below:

![coffee
cardioid](https://i0.wp.com/chalkdustmagazine.com/wp-content/uploads/2017/10/photo-1.jpg?resize=768%2C576)

---

Further reading: Wikipedia has [great
diagrams](https://en.wikipedia.org/wiki/Cardioid#Cardioid_as_envelope_of_a_pencil_of_circles)
to accompany.  Dan Kalman's article ["Solving the Ladder Problem on the Back of
an Envelope."](http://dankalman.net/AUhome/pdffiles/ladder_paper_MM.pdf)
includes a nice pedagogically-oriented discussion of envelope subtleties. It
cites Courant's [Differential and Integral Calculus (vol
2)](https://archive.org/details/DifferentialIntegralCalculusVol2/page/n183),
which is freely available on Archive.org.


<script>
  var worldFreestyle = document.getElementById('world-freestyle');
  var worldCardioid = document.getElementById('world-cardioid');

  function mark(world, ctx, X, Y) {
    var originX = world.width / 2;
    var originY = world.height / 2;

    ctx.strokeStyle = 'rgba(255, 0, 0, 0.3)'
    ctx.beginPath();
    ctx.arc(
      X, Y,
      Math.sqrt(
      	(X - originX) * (X - originX) +
        (Y - originY) * (Y - originY)),
      0, Math.PI * 2
    );
    ctx.stroke();
    ctx.fillRect(X, Y, 2, 2);
  }

  function clear(world, ctx) {
    var originX = world.width / 2;
    var originY = world.height / 2;

    // Clear
    world.height = world.height;
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';

    // Casino
    ctx.strokeRect(originX - 2, originY - 2, 4, 4);
    ctx.fillText("Casino", originX, originY - 12);
  }

  worldFreestyle.addEventListener('click', function(event) {
    var ctx = this.getContext('2d');
    clear(this, ctx);
  }, false);
  clear(worldFreestyle, worldFreestyle.getContext('2d'));
  worldFreestyle.addEventListener('mousemove', function(event) {
    var ctx = this.getContext('2d');
    var X = event.clientX - this.offsetLeft + window.scrollX;
    var Y = event.clientY - this.offsetTop  + window.scrollY;
    mark(this, ctx, X, Y);
  }, false);

  worldCardioid.addEventListener('mousemove', function(event) {
    var ctx = this.getContext('2d');
    var X = event.clientX - this.offsetLeft + window.scrollX;
    var Y = event.clientY - this.offsetTop  + window.scrollY;
    var originX = this.width / 2;
    var originY = this.height / 2;
    clear(this, ctx);

    // Region
    var R = this.width / 6;
    var N = 18;
    for (var i = 0; i < N; i++) {
      mark(
        this, ctx,
        X + Math.sin(i / N * Math.PI * 2) * R,
        Y + Math.cos(i / N * Math.PI * 2) * R
      );
    }

    // Circle
    ctx.beginPath();
    ctx.arc(X, Y, R, 0, Math.PI * 2);
    ctx.stroke();
    ctx.fillStyle = 'black';
    ctx.fillText("Los Angeles", X, Y - 12);


    // Limacon
    ctx.save();
    ctx.lineWidth = 10;
    ctx.beginPath();
    for (var theta = 0; theta < 2 * Math.PI; theta += 0.01) {
      var phi = Math.atan2(originX - X, originY - Y);
      var a = Math.sqrt(Math.pow(originX - X, 2) + Math.pow(originY - Y, 2)) / R;
      var r = 2 * (1 + a * Math.cos(theta)) * R;
      ctx.lineTo(
        originX + r * Math.cos(theta - phi - Math.PI / 2),
        originY + r * Math.sin(theta - phi - Math.PI / 2)
      );
    }
    ctx.stroke();
    ctx.restore();
  }, false);
</script>
