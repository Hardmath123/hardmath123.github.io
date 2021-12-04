The other day my toilet broke and I involuntarily learned a lot about how flushing works. My friend suggested an analogy for me: flushing toilets is like a neuron's activation: once a critical threshold is met, there's an "all-at-once" response.

That got me thinking, could we implement deep neural networks in plumbing? It turns out, the answer is yes! A very simplified model of a flush toilet's nonlinear behavior is as follows: it's a bucket, into which water can be poured, and there is a hole at height $h \geq 0$. If you pour in volume $v$ of water into the bucket, the output that flows out of the hole is $\text{ReLU}(v - h)$.

The second component we need to build a neural network is a linear map. We can do this by attaching a branching pipe to the hole. This component will have $k$ branches with cross-sectional areas $A_1, A_2, \dots, A_k > 0$. By conservation of mass and a simple pressure argument, the amount of water that pours out of branch $i$ is $A_i / \Sigma_j A_j$.

Together, these components allow us to compute a function from $\mathbb{R}\rightarrow \mathbb{R}^k$, which looks something like $\text{PeLU}(v, \vec{A}, h) = \text{ReLU}(v - h)\cdot \vec{A} / \Sigma_j A_j$. Here, "PeLU" stands for "Porcelain-Emulated Linear Unit." It is clear how to vectorize this expression over $v$, which effectively creates a new kind of neural network "layer" with trainable parameters $\vec{A}$ and $h$ for each input dimension. To enforce the positivity constraint on $h$ and $A_i$, we will actually work with the following key equation: $\text{PeLU}(v, \vec{A}, h) = \boxed{\text{ReLU}(v - h^2) \cdot \text{softmax}(\vec{A})}$.

All that is left to do at this point is to implement this in PyTorch and train it.

```
import torch

class PeLU(torch.nn.Module):
    def __init__(self, in_feat, out_feat):
        super().__init__()
        self.heights = torch.nn.Parameter(
            torch.randn(in_feat))
        self.weights = torch.nn.Parameter(
            torch.randn(in_feat, out_feat)
        )

    def forward(self, X):
        X = torch.nn.functional.relu(X - self.heights ** 2)
        X = X.matmul(self.weights.softmax(dim=1))
        return X
```

Here, I built a PeLU layer that can be slipped into any PyTorch model, mapping `in_feat` inputs to `out_feat` outputs. Next, let's stack some PeLU layers together and train the result on the classic "Iris" dataset, which has 4 features and assigns one of 3 labels. We will create a "hidden layer" of size 3, just to keep things interesting.

```
from iris import feat, labl

m = torch.nn.Sequential(
    PeLU(4, 3),
    PeLU(3, 3)
)
o = torch.optim.Adam(m.parameters(), lr=0.01)
lf = torch.nn.CrossEntropyLoss()

for i in range(10_000):
    o.zero_grad()
    pred = m(feat * 10)
    loss = lf(pred, labl)
    loss.backward()
    o.step()

print('Loss:', loss)
print('Error:', 1. - ((torch.argmax(pred, dim=1) == labl) * 1.).mean())
```

This trains very quickly, in seconds, and gives an error of 2%. Of course, we haven't split the dataset into a train/test set, so may be be overfitting.

By the way, you may have noticed that I multiplied `feat` by 10 before passing it to the model. Because of the conservation of mass, the total amount of water in the system is constant. But each bucket "loses" some water that accumulates below the hole. To make sure there's enough water to go around, I boosted the total amount.

But that's all that needs to be done! Once we export the parameters and write a small visualizer...

![GIF of PeLU network inferring an Iris example](static/iris-pelu.gif)

Isn't that a delight to watch? I may even fabricate one to have as a desk toy --- it shouldn't be hard to make a 3D-printable version of this. If we wanted to minimize the number of pipes, we could add an L1 regularization term that enforces sparsity in the $\vec{A}$ terms.

Some final thoughts: this system has a couple of interesting properties. First, there's a kind of "quasi-superposition" that it allows for: if you pour in more water on top to incrementally refine your input, the output will automatically update. Second, the "conservation of mass" guarantees that the total water output will never exceed the total water input. Finally, it's of course entirely passive, powered only by gravity.

This has me wondering if we can build extremely low-power neural network inference devices by optimizing analog systems using gradient descent in this way (a labmate pointed me to [this](https://arstechnica.com/science/2018/07/neural-network-implemented-with-light-instead-of-electrons/), for example).

Below is a little widget you can use to enjoy playing with PeLU networks. All inputs must be between 0 and 10. :)


Sepal length (cm): <input id="sl" type="text" value="6.2"></input><br/>
Sepal width (cm):  <input id="sw" type="text" value="3.4"></input><br/>
Petal length (cm): <input id="pl" type="text" value="5.4"></input><br/>
Petal width (cm):  <input id="pw" type="text" value="2.3"></input><br/>
<input type="button" id="go" value="Predict!"></input><br/>

<canvas id="world" width="500" height="500"></canvas>

<script>
var m = [{'h': [2.0516297817230225, 2.18482890761347e-30, 4.2594499588012695, 2.937817096710205], 'w': [[0.08244021981954575, 0.35453349351882935, 0.5630263090133667], [0.783989667892456, 0.0022806653287261724, 0.2137296199798584], [0.0007646767771802843, 0.8042643070220947, 0.19497093558311462], [0.0004950931761413813, 0.9982838034629822, 0.0012211321154609323]]}, {'h': [2.2704419876575757e-26, 33.44374465942383, 12.223723411560059], 'w': [[0.9706816077232361, 0.021526599302887917, 0.007791891228407621], [0.0013629612512886524, 0.022002533078193665, 0.9766345620155334], [0.018276285380125046, 0.9780184626579285, 0.0037053129635751247]]}];

function Chamber(x, y, f, h, w, p) {
  this.x = x;
  this.y = y;
  this.f = f;

  this.h = h;
  this.w = w;
  this.p = p;

  this.l = null;
}

Chamber.prototype.flow = function(dl) {
  if (this.f <= this.h) return;

  dl = Math.max(0.1 * this.f - this.h, dl);
  for (var j = 0; j < this.p.length; j++) {
    this.p[j].f += dl * this.w[j];
  }
  this.f -= dl;
};

Chamber.prototype.draw = function(ctx) {
  var height = 100;
  ctx.save();
  ctx.translate(this.x, this.y);

  if (this.l !== null) {
    ctx.save();
    ctx.font = '8pt Helvetica';
    ctx.translate(0, height);
    ctx.rotate(-Math.PI / 2);
    ctx.fillText(this.l, 0, 5);
    ctx.restore();
  }

  ctx.fillStyle = '#acf';
  ctx.fillRect(10, height - this.f, 30, this.f);

  ctx.beginPath();
  ctx.arc(0, 10, 10, -Math.PI / 2, 0);
  ctx.lineTo(10, height);
  ctx.lineTo(40, height);
  ctx.lineTo(40, 10);
  ctx.arc(50, 10, 10, Math.PI, -Math.PI / 2);
  ctx.stroke();

  if (this.h !== null) {
    ctx.beginPath();
    ctx.arc(35, height - this.h, 5, 0, Math.PI * 2, true);
    ctx.stroke();
  }
  ctx.restore();

  if (this.h !== null) {
    for (var j = 0; j < this.p.length; j++) {
      ctx.save();
      ctx.beginPath();
      ctx.moveTo(this.x + 35, this.y + height - this.h);
      ctx.bezierCurveTo(
        this.x + 35, this.y + height - this.h + 20,
        this.p[j].x + 25, this.p[j].y - 20,
        this.p[j].x + 25, this.p[j].y
      );
      ctx.strokeStyle = 'black';
      ctx.lineWidth = this.w[j] * 10;
      ctx.stroke();
      ctx.lineWidth = ctx.lineWidth * 0.8;
      ctx.strokeStyle = this.f > this.h ? '#acf' : 'white';
      ctx.stroke();

      if (this.f > this.h) {
        ctx.strokeStyle = '#acf';
        ctx.beginPath();
        ctx.moveTo(this.p[j].x + 25, this.p[j].y);
        ctx.lineTo(this.p[j].x + 25, this.p[j].y + 100);
        ctx.stroke();
      }
      ctx.restore();
    }
  }

  if (this.h === null) {
    var best = true;
    for (var j = 0; j < cs[cs.length - 1].length; j++) {
      if (this.f < cs[cs.length - 1][j].f) best = false;
    }
    if (best) {
      ctx.save();
      ctx.fillStyle = 'rgba(255, 255, 0, 0.2)';
      ctx.fillRect(this.x - 10, this.y - 10, 50 + 20, height + 20);
      ctx.restore();
    }
  }
};

var cs = [];
for (var i = 0; i < m.length; i++) {
  cs.push([]);
  for (var j = 0; j < m[i].h.length; j++) {
    var c = new Chamber(30 + 20 * i + 80 * j, 20 + 150 * i, 0, m[i].h[j], m[i].w[j], []);
    cs[cs.length - 1].push(c);
  }
}

cs.push([]);
for (var j = 0; j < cs[cs.length - 2][0].w.length; j++) {
  var c = new Chamber(30 + 20 * i + 80 * j, 20 + 150 * i, 0, null, [], []);
  cs[cs.length - 1].push(c);
}

for (var i = 0; i < m.length; i++) {
  for (var j = 0; j < cs[i].length; j++) {
    cs[i][j].p = cs[i + 1];
  }
}

cs[0][0].l = 'sepal length (cm)';
cs[0][1].l = 'sepal width (cm)';
cs[0][2].l = 'petal length (cm)';
cs[0][3].l = 'petal width (cm)';
cs[2][0].l = 'P(iris setosa)';
cs[2][1].l = 'P(iris versicolour)';
cs[2][2].l = 'P(iris virginica)';

cs[0][0].f = 62;
cs[0][1].f = 34;
cs[0][2].f = 54;
cs[0][3].f = 23;

function frame() {
  var world = document.getElementById('world');
  world.width = world.width;
  var ctx = world.getContext('2d');
  for (var i = 0; i < cs.length; i++) {
    for (var j = 0; j < cs[i].length; j++) {
      cs[i][j].draw(ctx);
    }
  }
  for (var i = 0; i < cs.length - 1; i++) {
    for (var j = 0; j < cs[i].length; j++) {
      cs[i][j].flow(0.1);
    }
  }

  window.requestAnimationFrame(frame);
}

window.addEventListener('load', function() {
  var sl = document.getElementById('sl');
  var sw = document.getElementById('sw');
  var pl = document.getElementById('pl');
  var pw = document.getElementById('pw');
  var go = document.getElementById('go');
  go.addEventListener('click', function() {
    for (var i = 0; i < cs.length; i++) {
      for (var j = 0; j < cs[i].length; j++) {
        cs[i][j].f = 0.;
      }
    }
    cs[0][0].f = Math.max(0., Math.min(100., (parseFloat(sl.value) || 0) * 10));
    cs[0][1].f = Math.max(0., Math.min(100., (parseFloat(sw.value) || 0) * 10));
    cs[0][2].f = Math.max(0., Math.min(100., (parseFloat(pl.value) || 0) * 10));
    cs[0][3].f = Math.max(0., Math.min(100., (parseFloat(pw.value) || 0) * 10));
  });
  frame();
});
</script>