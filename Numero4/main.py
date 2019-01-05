from functools import reduce

def euclidGCD(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q, r = b//a, b%a
        m, n = x-u*q, y-v*q
        b,a, x,y, u,v = a,r, u,v, m,n
        gcd = b
    return gcd, x, y

def factor(n):
    # slow step
    count = 2.0
    while(not (n / count).is_integer()):
        count += 1

    # divide by test values until primes are found
    return (int(count), int(n/count))

def computePrivate(p, q, e):
    totient = (p - 1) * (q - 1)

    gcd, d, b = modInv = euclidGCD(e, totient)

    return d % totient

def getPrivateKey(n, e):
    # get primes
    p,q = factor(n)

    # compute private key
    return computePrivate(p, q, e)

if __name__ == '__main__':
    print(getPrivateKey(1037, 7))
    input("press enter to close")
