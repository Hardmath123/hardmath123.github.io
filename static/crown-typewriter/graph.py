from matplotlib import pyplot as plt

f = open('raw-data.txt').readlines()
x = map(int, f)[:1000]

g = open('opt-data.txt').readlines()
y = map(int, g)[:1000]

plt.title('Costs: Optimized Only')
plt.ylabel('Frequency')
plt.xlabel('Cost on 1800s Literature Benchmark')
#plt.yscale('log')

plt.hist(y, bins=100)
plt.savefig('typewriter-graph-2.png', dpi=300)
