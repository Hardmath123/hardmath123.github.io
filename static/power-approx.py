from mpmath import *
# http://www.ttmath.org/online_calculator
mp.dps = 10000

PREFIX  = input("Prefix? --> ")
BASE    = input("Base? ----> ")
RADIX   = input("Radix? ---> ")

RADIX_log = log(RADIX)
BASE_log  = log(BASE)
PREFIX_log = log(PREFIX)

# stream of (a, r)
def gcd_stream(x, y):
    t = x
    u = y
    while True:
        a, r = floor(t/u), fmod(t, u)
        yield (a, r)
        t = u
        u = r

# stream of ((n, d), r)
def approx_stream(cf):
    h = [0, 1]
    k = [1, 0]
    while True:
        a, r = cf.next()
        h.append(a*h[-1] + h[-2])
        k.append(a*k[-1] + k[-2])
        yield ((h[-1], k[-1]), r)

G = gcd_stream(RADIX_log, BASE_log)
A = approx_stream(G)

ans_a = 0
ans_b = 0
PREFIX_log_temp = PREFIX_log
while True:
    (n, d), r = A.next()
    if r < PREFIX_log_temp:
        s = sign(n*BASE_log - d*RADIX_log)
        k = floor(PREFIX_log_temp / r)
        ans_a += s * n * k
        ans_b += s * d * k
        PREFIX_log_temp = fmod(PREFIX_log_temp, r)
    if ans_a > 0 and ans_b > 0:
        print "Accurate to",
        print int(floor(-log(e**PREFIX_log_temp-1,RADIX))),
        print "digits:"
        print """{}^{} ~~ {}*{}e+{}""".format(
            nstr(BASE, 15),
            int(ans_a),
            nstr(PREFIX),
            RADIX,
            int(ans_b)
        )
