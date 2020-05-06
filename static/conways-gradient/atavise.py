import torch
import numpy as np
from matplotlib import pyplot as plt
import skimage

def show_tensor(t):
    plt.colorbar(plt.imshow(t.detach()[0, 0]))

def distr(n, mu, sigma):
    return torch.exp(-0.5 * (mu - n)**2 / sigma ** 2) / (sigma * (2 * np.pi) ** 0.5)

def nonlin(b, k):
    live = b * distr(k, 2.5, 0.3) / float(distr(torch.tensor(2), 2.5, 0.3))
    dead = (1 - b) * distr(k, 3, 0.3) / float(distr(torch.tensor(3), 3, 0.3))
    return live + dead

def clamp(x):
    return (((x - 0.5) * 6.).tanh() + 1)/2

def discretize(x):
    return ((x > 0.5) * 1).double()

def step(b):
    return clamp(nonlin(b, torch.conv2d(b, f, padding=1)))

f = torch.ones(1, 1, 3, 3, dtype=torch.double)
f[0, 0, 1, 1] = 0

def blur(img):
    gauss = torch.tensor([
        [1, 2, 1],
        [2, 4, 2],
        [1, 2, 1]
    ], dtype=torch.double).reshape(1, 1, 3, 3) / 16
    
    return torch.conv2d(img, gauss, padding=1)

# Atavism target
# target = torch.tensor(skimage.data.checkerboard()[:100, :100]).double() / 256
# target = torch.tensor(skimage.data.astronaut()[:200, :300, 0]).double() / 256
# target = torch.tensor(skimage.io.imread('conway.jpg')).double() / 256
target = torch.ones(100, 100).double()

seed = torch.randn(1, 1, target.shape[0], target.shape[1], dtype=torch.double) / 5 + 0.5
N = torch.ones(seed.shape).sum()

for i in range(10000):
    seed.requires_grad_()
    board = clamp(seed)
    for j in range(1):
        board = step(board)
    out = torch.abs(target - blur(board))
    loss = out.sum() / N
    loss.backward()
    if i % 1000 == 0:
        print(i, loss.item())
        print('Average grad norm:', torch.abs(seed.grad).sum().item() / N)
        print('Average seed dist:', torch.abs(seed - 0.5).sum().item() / N)
    seed = (seed - seed.grad * N * 0.01).clamp(0, 1).detach()

show_tensor(discretize(seed))
