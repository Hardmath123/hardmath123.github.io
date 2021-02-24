<style>
input[type="range"] {
  display: block;
  width: 100%;
}

#imgbox {
  display: inline-block;
  position: relative;
}

#world {
  margin: 0;
  padding: 0;
  max-width: 100%;
}
</style>

<script src="/static/blizzard-blossoms/onnx.min.js"></script>
<script>

window.addEventListener('load', function() {
  var LATENT = 10;
  var fieldset = document.getElementById('sliders');

  sliders = [];
  for (var i = 0; i < LATENT; i++) {
    var slider = document.createElement('input');
    slider.type = 'range';
    slider.min = -4;
    slider.max = +4;
    slider.step = 0.5;
    fieldset.appendChild(slider);
    sliders.push(slider);
  }

  function randomize(suppress_flurry) {
    for (var i = 0; i < LATENT; i++) sliders[i].value = Math.random() * 6 - 3;
    sliders[9].value = +4;
    sliders[5].value = -4;
    update();
    if (!suppress_flurry) flurry();
  }

  document.getElementById('randomize').addEventListener(
    'click', function() {randomize(false)}
  );

  // create a session
  const myOnnxSession = new onnx.InferenceSession();

  function update() {

    // generate model input
    var values = [];
    for (var i = 0; i < LATENT; i++) {
      values.push(sliders[i].value);
    }
    const inferenceInputs = [
      new Tensor(new Float32Array(values), "float32", [1, LATENT])
    ];

    // execute the model
    myOnnxSession.run(inferenceInputs).then((output) => {

      // consume the output
      const outputTensor = output.values().next().value;

      var can = document.createElement('canvas');
      can.height = 32;
      can.width = 32;
      var ctx = can.getContext('2d');
      ctx.scale(can.width / outputTensor.dims[2], can.height / outputTensor.dims[3]);
      for (var x = 0; x < outputTensor.dims[2]; x++) {
        for (var y = 0; y < outputTensor.dims[3]; y++) {
          var value = outputTensor.get(0, 0, x, y);
          ctx.fillStyle = `rgba(100, 100, 255, ${value})`;
          ctx.fillRect(x, y, 1, 1);
        }
      }

      var img = document.getElementById('world');
      img.width = can.width;
      img.height = can.height;
      img.src = can.toDataURL('image/png');
    });

  }

  // load the ONNX model file
  myOnnxSession.loadModel("/static/blizzard-blossoms/model.onnx").then(function() {
    for (var i = 0; i < LATENT; i++) {
      sliders[i].addEventListener('input', update, false);
      sliders[i].addEventListener('change', function() {update(); flurry();}, false);
    }
    document.getElementById('loading').remove();
    randomize(true);
  });


  function flurry() {
    var flake = document.createElement('img');
    var img = document.getElementById('world');
    flake.height = img.height;
    flake.width = img.width;
    flake.src = img.src;
    flake.style.position = 'absolute';
    flake.style.top = img.offsetTop;
    flake.style.left = img.offsetLeft;
    document.getElementById('imgbox').appendChild(flake);

    var dx = 0;
    var xv = Math.random() - 0.5;
    var dy = 0;

    var dtheta = 0;
    var dphi = 0;

    function step_animation() {
      dx += xv;
      xv = xv * 0.99;
      dy += 1;

      dtheta += 1;
      dphi += 1;

      flake.style.transform = `translate(${dx}px, ${dy}px) rotateX(${dtheta}deg) rotateY(${dphi}deg)`;

      if (dy < 1000)
        window.requestAnimationFrame(step_animation);
      else
        flake.remove();
    }

    step_animation();
  }

});
</script>

<fieldset id="sliders">
<span id="loading">(Please be patient as we wait for the snowflake factory to load&hellip;)</span>
<center><span id="imgbox"><img id="world" height=32 width=32></img></span></center><br/>
<center><button id="randomize">Roll the dice</button></center><br/>
</fieldset>









Snow and snowflakes have been on my mind lately. This is not entirely because
of the storm in Texas --- rather, I have been thinking since Christmas about
the snowflake's _shape:_ those small, delicate, spiky circles we all know so
well (err, perhaps there is something of current events here after all...).
This is a blog post about snowflake shapes.

What shape _is_ a snowflake? In principle, we all know what snowflakes look
like. We can all imagine the six-fold symmetry, and then we can imagine the
embellishments.  And yet--- not so fast! As a little child I (and I do not
think I am alone in this) wanted to see the shape of a snowflake for myself.
Of course, I never quite could --- at least, to the point where I could stuff
and saturate my eyes --- because the delicate snowflakes melted away as soon as
my snow-blind eyes could focus on the crystal caught. Think about it, then:
where does your own conception of snowflake-shape arise from? Does it come from
firsthand experience, or from clip-art and wintertime papercrafts?

> (Of course, there _is_ something to be said for indirect inference of
> snowflake-shape. Years later, I would marvel at the fact that you could infer
> that snowflakes are hexagonal from the existence of [22º
> haloes](https://github.com/kach/rocket-flame-renderer), a kind of
> crystallography at the heavenly scale, linking the macroscopic and
> microscopic. For now however I am concerned with seeing _directly_, and face
> to face, with a presence and visual immediacy that cannot be afforded by
> imagination alone.)

This is no small concern. A year or so ago I visited the California Academy of
Sciences and learned about Wilson Bentley, the first man to photograph a
snowflake. This was on January 15, 1885; he was just shy of 20 years old. To
appreciate this moment, you have to imagine a time _before_ January 15, 1885,
when no such photograph existed. Until Bentley's innovation, no man had seen a
single snowflake for more than a delicate glimpse. Perhaps spatially the
snowflake could be magnified under a microscope (as [Hooke and his
contemporaries](https://en.wikipedia.org/wiki/Timeline_of_snowflake_research)
demonstrated in the 17th century), but how could anyone magnify it
_temporally?_ Bentley's Edgertonesque miracle --- akin to Muybridge's "horse in
motion," captured just seven years earlier --- is to hold still the moment to
reveal _more_ --- to give us the opportunity to gaze without urgency. Dare I
say, Bentley _freezes time?_ The manipulation of time becomes an [act of
unconcealment](electric-guitar.html), and then furthermore an act of creation.
Bentley's snowflakes outlived him, and they will outlive me.

---

Wilson Bentley was not a scientist by training, and perhaps that served him
well. Over the course of his life he collected over 5,000 images of what he
called "ice flowers." There is something marvelous about this devotion, which
spanned years and years, crystal after crystal, wonder undiminished. Surely the
5,000th snowflake brought Wilson as much delight as the 4,999th (and surely it
is the case that you know you are in love when you find yourself falling in
love afresh every day).

There is also something to the uniformity of Bentley's collection. Each
snowflake is framed carefully in the center of a slide, on a black background.
The images are diligently cropped to squares. See for yourself! The University
of Wisconsin-Madison hosts an [online
archive](https://library.ssec.wisc.edu/bentley/) of 1,181 of Bentley's images,
courtesy the Schwerdtfeger Library. Bentley never sought copyright on his
images; they are in the public domain, and so I downloaded them, along with
their labeled categories. The categories have wonderful names, such as "crystal
with broad branches" and "lumped graupel."

When displayed in a grid, the snowflakes look like a box of delicious holiday
sweets. Surely these delights are made of sugar and not ice.

![snowfakes](/static/blizzard-blossoms/snowflakes.png)

What does one _do_ with 1,181 snowflakes? One searches for patterns, the way
Bentley would never have been able to. Bentley's images demand to be studied as
samples from a distribution, and they are strikingly well-suited to our
favorite statistical computer vision techniques. For example, though they are
scanned at a uniform 1000x1000 resolution, they still make sense when
dramatically downscaled, even to as low as 32x32. Notice also how the
snowflakes are highly amenable to _data augmentation_ on account of their
intrinsic symmetry. Each snowflake can be reflected and rotated arbitrarily to
produce several more high-quality synthetic snowflakes "for free." So, even
though there are nominally 1,181 unique images, there is much more juice here
than one might expect at first. You can't always play this game: CIFAR images
can't really be rotated, and most MNIST digits can't even be flipped. But
snowflakes are snowflakes.

One February evening I trained --- with a lot of help from my friends Gautam
and Jack --- a baby variational autoencoder, which embeds the snowflakes in a
small low-dimensional latent space. Here, "low-dimensional" means
10-dimensional: it seems very reasonable to encode 2^10 data points with 10
parameters. In the image below, the top row consists of five randomly-selected
source images, and the bottom row is the VAE's attempted reconstruction. The
contrastive green-and-purple colorscheme comes from matplotlib's default, and
reminds me of the delightful pGLO experiments we did in high-school biology.

![snowfakes](/static/blizzard-blossoms/vae.png)

Of course, as with all things deep-learning, this was easier said than
done. For a technique that falls broadly under "unsupervised learning," a VAE
requires an awful lot of babysitting! ---but then again, one of the joys of
online school is that _nobody can tell_ if you're training machine learning
models behind your Zoom tab. So I trained, and I trained. The current model
takes around 6 hours on my dusty old MacBook, though after the first 30 minutes
the results are already non-embarrassing.

> **Do you want to build a snowgan?** Separately, I also spent some time trying
> to build a model adversarially. The snowgan (so to speak) consists of two
> rival sisters: the generator, Elsa, is of the same architecture as the VAE's
> decoder, and the discriminator, Anna, learns to distinguish Elsa's output
> from real snowflakes. Elsa and Anna compete, and as a result Elsa gets better
> at camouflaging the fakes among the flakes. Alas, GAN convergence is finicky
> enough that I lost interest after a few days… open problem!

It turns out that the VAE's decoder can be used to build a small-scale
snowflake factory. Using ONNX.js and only a little bit of guile, I ported the
VAE's decoder to JavaScript and attached the latent space to some `<input
type="range">` sliders. By using the sliders to choose parameters in the latent
space and feeding these parameters to the decoder, one can interpolate to
hallucinate snowflakes that are _not_ part of Bentley's training set. With some
experimentation, I found the sliders that correspond to parts of the latent
space that map to outliers; those parameters I clamped to extreme values in the
non-outlier-ey direction. This interface is what you see at the top of this
blog post.

> At time of writing, there is only one Google search result for "this
> snowflake does not exist," which points to a 2017 [master's
> thesis](http://etd.lib.metu.edu.tr/upload/12621180/index.pdf) in
> elementary-school education by Eli̇f Dedebaş. The context is an activity where
> children are making paper snowflakes, and investigating the relationship
> between the number of folds and the symmetries. One child creates a
> snowflake-like shape with _eight_-fold symmetry and is asked if she knows why
> such a shape is unnatural. Shape!

---

I imagine this slider infrastructure is on par with the sort of fancy tooling
UI that they have up in the Great Snow Factory In The Sky. I'm reminded of
David Wiesner's wonderful Caldecott-winning picture book _Sector 7_, which I
recall reading ("reading") in my elementary school's library. It is about a
cloud factory, accessed from the top of the Empire State Building. Notice how
the large sousaphone-bell-shaped openings emanating from the factory roof are
exactly a portrait of an autoencoder's decoder.

![snowfakes](/static/blizzard-blossoms/sector-7.png)

"Wiesner visited the Empire State Building on a zero-visibility day to research
this book," reads the About-the-Author at the end, "He was the only person
there." There is something of Wiesner in Bentley and Bentley in Wiesner, I
think. Think of them both, and yourself, too, as Friedrich's _Wanderer_.

![snowfakes](/static/blizzard-blossoms/wanderer.png)

---

The results interpolated by the VAE are surprisingly convincing.  Here are some
snowflakes that do not exist (snowfakes?). I created these images by sliding
the sliders haphazardly and recording a trace of the changing image.  Often,
people display this kind of interpolation in animated form, but in relation
--- and, indeed, deference --- to Bentley's life's work, I would rather see
them spread spatially than temporally.

![snowfakes](/static/blizzard-blossoms/snowfakes.png)

I enjoy trying to work out the exact moment of transition between different
kinds of snowflakes; there is a snowy saltation that occurs at certain
boundaries that I cannot quite point you to. A curious fact is that a t-SNE
plot in the VAE's latent space shows no clustering with respect to the provided
labels; the VAE seems to have hallucinated its own classification scheme, one
which is perhaps more macroscopically morphological in nature than Magono and
Lee's 1966 classification scheme.

---

The BentleyBlizzardBlossoms (B3) dataset, along with some PyTorch utilities and
the source code and trained model of the baby autoencoder, is available [on
Github](https://github.com/kach/bentley-blizzard-blossoms). I think it would
make a wonderful alternative to MNIST for small experiments. If you use it for
anything, please let me know!
