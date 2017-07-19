# https://en.wikipedia.org/wiki/List_of_21st-century_earthquakes
# pbpaste | grep -A 1 "|-" | grep "| [A-Za-z]" | sed s/"| "// | tee -a earthquakes.txt
# ipython --pylab osx earthquakes.txt

from dateutil import parser
from math import exp, factorial

home = parser.parse("January 1, 2000")

f = open("earthquakes.txt")
eq = []
while True:
    x = f.readline().rstrip()
    if not x:
        break
    eq.append((parser.parse(x) - home).total_seconds())
f.close()

l = len(eq)/(max(eq) - min(eq))
t = 60*60*24*30 # a monthworth of seconds
n = 1

bins = []
i = min(eq) + t
while i < max(eq):
    bins.append(len([ee for ee in eq if ee < i and ee >= i - t]))
    i += t

def PE(n):
    return len([b for b in bins if b == n])*1.0 / len(bins)


def PT(n):
    return (l*t)**n / exp(l*t) / factorial(n)



bce = bincount(bins)
bs  = xrange(len(bce))
bct = [PT(i)*len(bins) for i in bs]

emp, = plt.plot(bs, bce, 'r--')
tho, = plt.plot(bs, bct, 'k')

plt.legend(
    [emp, tho],
    [
        "Reality according to Wikipedia",
        "Prediction (lambda*t)^n / e^(lambda*t)n!"
    ]
)

plt.xlabel('Number of earthquakes in a month')
plt.ylabel('Number of months')
plt.title('Earthquake Frequency Distribution')

plt.savefig('earthquakes.png', dpi=200)

def calculate_e(n):
    return (PE(n)*factorial(n) / (l*t)**n) ** (-(l*t)**-1)

print calculate_e(1)
