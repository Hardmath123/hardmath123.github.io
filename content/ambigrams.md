The other day I ordered a book on art history from Amazon... which reminded me
of the movie _Angels and Demons_, which reminded me of ambigrams. Ambigrams are
those stylized words that look the same when you turn them upside down. Here is
the classic, [by John
Langdon](http://www.johnlangdon.net/works/angels-demons/).

![earth air fire water](static/ambigrams/langdon.png)

I've been thinking a lot about the absurd power of gradient descent these days,
and so almost immediately I felt the need to try and synthesize ambigrams
on-demand by gradient descent.

It turns out that this isn't too hard to implement. Let's start with just
single-character ambigrams. Here's the plan: first, we train some sort of
neural net to recognize characters. This training is by gradient descent on the
weights / convolution filter / whatnot; specifically, we imagine a function of
the weights that outputs some loss and take its derivative _with respect to the
weights_ to do gradient descent. Once the neural net is trained, however, we
can just treat it as a single function from tensors (input image) to tensors (a
one-hot encoding of the classification... or some softmaxed approximation).
Taking that one-hot output and converting it into a cross-entropy loss against
some desired output, we can now do gradient descent to minimize this loss _with
respect to the input image_ (keeping the weights constant). This process lets
us "dream" of images representing whichever characters we want.

Similarly, we can do the same thing but with the tensor turned upside-down, to
dream images of upside-down characters. Okay, so now we can just combine these
two processes --- literally, by adding the loss functions --- to dream an image
that matches one character right-side-up and another character upside-down.
That's it! Now we let it run all day to generate an image for each alphanumeric
character pair (36^2 = 1296) and we start to get a nice little "ambigram font":

![grid](static/ambigrams/grid.png)

Combining letters from this "font" lets us make arbitrary ambigrams.

This was a low-effort operation, hacked together over an evening and a morning,
plus a full day of "training." I'm sure it's possible to do better. Here are
some technical notes for anyone who wants to have a go at it. My code is all
online, [here](https://github.com/kach/neural-ambigrams).
* It's all written in PyTorch. The neural net itself is literally PyTorch's
  built-in [MNIST
  example](https://github.com/pytorch/examples/tree/master/mnist).
* I used the [EMNIST](https://www.nist.gov/node/1298471/emnist-dataset)
  dataset, which is MNIST that also adds in the alphabets from the NIST
  database (and comes with PyTorch). I used the "balanced" split.
* I added an L1 regularizer to force the output images to be sparse, i.e.
  mostly "blank paper" with some "ink." Without this, you get very dark images.

Okay, now time for some pictures. Some turned out better than others, and there
is plenty of scope for improvement...

P.S. Depending on your browser, images in this post may or may not flip
upside-down automatically if you hover over them.

<style>
img {
  transform: rotate(0deg);
  transition: transform 0.5s;
}

img:hover {
  transform: rotate(180deg);
  transition: transform 0.5s;
}
</style>

## ANGEL AND DEMON

![ANGEL AND DEMON](static/ambigrams/angel-and-demon.png)

## BANANA

![BANANA](static/ambigrams/banana.png)

## YEAR, 2016

![YEAR, 2016](static/ambigrams/year-2016.png)

## GOOD, EVIL

![GOOD, EVIL](static/ambigrams/good-evil.png)

## TEAMWORK

![TEAMWORK](static/ambigrams/teamwork.png)

## BLUES, SKATE

![BLUES, SKATE](static/ambigrams/blues-skate.png)

## DREAM, WORLD

![DREAM, WORLD](static/ambigrams/dream-world.png)

---

Update (3/26/20): Alex Pietrow created [a
website](https://makeambigrams.com/ambigram-generator/) that lets you use this
font to build your own ambigrams (along with more ambigram fun).
