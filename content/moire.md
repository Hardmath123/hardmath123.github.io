Another magic trick. Watch these two grids overlap to reveal a secret image!
Can you spot the phantom horse?

<style type="text/css">
.slideme {
  animation: reveal;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
  -webkit-animation-delay: 5ms; /*
https://stackoverflow.com/questions/30735571/css-rotate-animation-doesnt-start-properly-in-safari
*/
  margin-bottom: 0;

  width: 50%;
}

.slideup {
  animation: revealb;
  animation-duration: 2s;
  animation-iteration-count: infinite;
  animation-direction: alternate;
  -webkit-animation-delay: 5ms; /*
https://stackoverflow.com/questions/30735571/css-rotate-animation-doesnt-start-properly-in-safari
*/
  margin-top: 0;
  width: 50%;
}

@keyframes reveal {
  from {
    transform: translateY(0);
  }
  50% {
    transform: translateY(0);
  }
  to {
    transform: translateY(100%);
  }
}

@keyframes revealb {
  from {
    transform: translateY(0);
  }
  50% {
    transform: translateY(0);
  }
  to {
    transform: translateY(-100%);
  }
}

</style>

<img class="slideme" src="static/moire/warp.png"></img><br/>
<img class="slideup" src="static/moire/screen.png"></img>


If my janky CSS animation didn't work for you, here is another way to see it:
simply shrink the top grid slowly until the horse "pops" out. It's hard to show
this effect consistently across displays/browsers because of varying pixel
spacings and various browsers' aggressive anti-aliasing tactics, but here is a
screen recording I captured.

<video controls="controls" name="Moire" style="width: 100%;" src="static/moire/moire.mov"></video>

Magic trick? Not quite. Graphics folks will immediately recognize this effect
as a curious instance of the dreaded _moiré pattern,_ caused by the
interference between two almost-but-not-quite-the-same grids. Researchers work
really hard to escape such "glitchy" artifacts --- they are often a result of
sloppily sampling a texture in a grid, leading to jagged edges or moiré streaks
(image below from Wikipedia). 

![bricks](static/moire/bricks.jpg)

In fact, a [lot of
effort](http://www.pbr-book.org/3ed-2018/Sampling_and_Reconstruction.html) has
gone into finding "good" sampling patterns that avoid moirés; for example, in
an odd crossover of sampling theory and anatomy, if you look at the
distribution of [photoreceptors in a monkey's
retina](https://www.nap.edu/read/1570/chapter/13) they are neither in a grid
_nor_ uniformly random, but rather arranged in a _low-discrepancy_ pattern to
avoid exactly this kind of artifact.

But for all the hard work gone into avoiding these patterns, you kind of have
to admit that they are beautiful and mysterious. In fact "moiré" gets its name
from a desirable form of silk weave that exhibits this phenomenon owing to
interference from the weave (photo from Wikipedia again). Similarly, [this
sculpture](https://en.wikipedia.org/wiki/Guardian_(sculpture) (and a lot more
art) exploits moiré patterns for their hypnotic beauty.

![moire silk](static/moire/silk.jpg)

There are lots of real-world ways you can play with this effect, and indeed
soon enough you can't stop seeing it everywhere you go (this is the joy and
frustration of being interested in visual phenomena):

1. Point a camera at a checkered shirt; the camera's pixel grid interferes with
   the fabric pattern (I've been told not to wear checkered shirts when giving
talks at certain venues where everything is recorded).
2. Align two kitchen strainers and gently bend them to see the patterns change.
3. Watch a screen door's shadow interfere with the screen itself, poke the
   screen a bit to see the patterns change.
4. Watch the wire fences on either side of a pedestrian walkway above a road
   interfere with each other.
5. Look at an office chair from behind, watch the mesh of the back interfere
   with the mesh of the seat. Depending on their relative curvature you can get
some beautiful effects.

These patterns are seemingly random, like marbled paper. But can we control
this randomness? Satisfyingly, an on-demand moiré such as the effect above is
extremely simple to generate using differentiable programming in PyTorch.

What I am optimizing is a _small distortion_ to the image of the grid such that
when the grid and its distortion are superimposed, the resulting image has low
L2 difference from a given target, such as the horse image. What exactly is
this "distortion"? Imagine the image printed on play-dough and deforming it by
stretching and squeezing parts. The result is a warping of the image. To
express this warping, each pixel is assigned a "motion vector" which tells it
where to go. To make sure the motion vectors are smooth and continuous between
adjacent pixels, I actually learn a heavily downsampled set of motion vectors
(even a 12-by-12 array gets good results) and then upsample it to full
resolution with bicubic interpolation.

Here is the wonderful thing: all of these operations are built in to PyTorch
and differentiable, apparently to support [Spatial Transformer
Networks](https://arxiv.org/pdf/1506.02025.pdf). So, a straightforward 30-line
implementation of the above algorithm is all it takes to start "learning" a
moiré grid perturbation. [Here](static/moire/Moire.ipynb) is a Jupyter notebook
with all you need to get started.

How much computation does it take to get good results? See this animation: it
converges extremely rapidly, in just 800 iterations or so of plain gradient
descent (a couple of minutes on my laptop).

![learning](static/moire/morph.gif)

---

I'm of course not the first person to try this trick; I found references in
2001 and 2013. I think my results look significantly better than those
     presented in the paper [_Variational Approach to Moire Pattern Synthesis_
(Lebanon and Bruckstein 2001)](static/moire/2001.pdf), even though my technique
is much simpler than their gradient-based technique. On the other hand, I think
the more mathematically-motivated results presented in [_Target-Driven Moiré
Pattern Synthesis by Phase Modulation_ (Tsai & Chuang
2013)](static/moire/2013.pdf) are much more impressive, even though they have a
slightly different setup than mine. They also had the resources to print out
their patterns on transparent film and overlay them physically, as well as to
mess with a camera whose Bayer pattern was known! And they suggest using this
trick for cryptography. Very neat.

To understand what they do we need to understand the mechanics of moiré
(instead of leaving it all to SGD!). I've always been told that when two
high-frequency signals such as grids are superimposed, they can alias to form
interesting low-frequeny content (famously there is [this
comic](https://xkcd.com/1814/)). But I've never been given more detail than
that high-level overview, so I looked it up myself. It's actually quite
wonderful and principled. Here is my understanding as informed by [_A
Generalized Fourier-based Method for the Analysis of 2D Moiré Envelope-forms in
Screen Superpositions_ (Amidror 1994)](static/moire/1994.pdf), specifically by
Figure 4 reproduced below.

![fig 4](static/moire/lattice.png)

First, we need to come up with a useful characterization of grids. Recall that
you can take a 2D signal (i.e. image) and perform a 2D Fourier transform, which
is _also_ an image. Each point in frequency-space represents a set of stripes
(i.e. a sine wave) rotated to match the point's angle with respect to the
origin (see (a) and (b) in the figure for examples of what I mean). The
frequency of the stripes is given by the distance from the point to the origin,
and the amplitude is given by the point's brightness (complex-valued
brightnesses let you set phase). To get "sharp" stripes instead of a "smooth"
sine wave gradient, you have to add "harmonics" at regular multiples of that
point (recall the Fourier transform of a square wave if that helps). This is
(d) and (e) in the figure from the paper.

Next, we note that superimposing two sets of stripes is like pointwise
multiplication (if you treat zeros as "occlusion", then multiplying by zero
always sends the result to zero as desired). Because pointwise multiplication
is convolution in frequency space, the superposition looks like a _lattice_
spanned by the harmonics in frequency space. This lattice is depicted in (f) in
the figure.

The key to the illusion is that this lattice might include points much closer
to the origin than either of the harmonics that span it! Because the human
visual perceptual system acts as a low-pass filter, the result is that you see
a low-frequency "phantom" in the superposition. This is visible in (c) in the
figure.

Tsai and Chuang use this exact insight to reverse the moiré effect
analytically, with excellent results.
 
---

**Open questions:** I think there's a lot more to do here. In my mind, the holy
grail is a T-shirt you can wear which, _only when photographed_ reveals a
secret message. Another neat application would be a wire mesh rolled into a
cylinder such that as you rotated it, the moiré patterns animated into
something cool (perhaps a galloping horse, as a nod to Muybridge). There is
some precedent for this in "barrier-grid" animation (see, e.g. [these vinyl
record
covers](https://thevinylfactory.com/features/freaky-formats-moire-effect/)),
but the benefit of a moiré-based approach would be that the barriers need not
be as thick, allowing for finer detail.

Another direction to go in is audio moiré; that is, could we make two sounds,
both above human aural range (20 kHz) such that when played together you hear a
perfectly clear, audible voice?

As you might have guessed, I think naïve gradient descent should be able to get
us a long way there...
