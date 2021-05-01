def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

t = int(input())
for count in range(t):
    (a, b, x) = [t(s) for t,s in zip((int,int,int),input().split())]
    if b < 0:
        a, b = modinv(a,x), -b
    print(pow(a,b,x))
