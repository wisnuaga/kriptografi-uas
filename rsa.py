import math
import random

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n)) + 1

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def generate_prime():
    n = random.randint(0, 100)
    if(is_prime(n)):
        return n
    else:
        return generate_prime()

def generate_key():
    p = generate_prime()
    q = generate_prime()

    if p == q:
        return generate_key()
    return p, q

def public_key(p, q):
    n = p * q
    m = (p-1) * (q-1)
    e = generate_prime()

    if e > m:
        return public_key(p, q)
    return n, e

def private_key(p, q, e):
    d = 0
    n = p * q
    m = (p - 1) * (q - 1)

    for k in range(1, m):
        d = (1 + (k * m)) / e
        if d % 1 == 0 and d != e:
            return n, int(d)
    return n, int(d)

def encrypt(n, e, msg):
    temp = ""
    for c in msg:
        x = ord(c) ** e % n
        temp += chr(x)
    return temp

def decrypt(n, d, e_msg):
    temp = ""
    for c in e_msg:
        x = ord(c) ** d % n
        temp += chr(x)
    return temp

p, q = generate_key()
n, e = public_key(p, q)
n, d = private_key(p, q, e)
msg = "kontol buto ijo dowo"

e_msg = encrypt(n, e, msg)
d_msg = encrypt(n, d, e_msg)

print("p = " + str(p) + " | q = " + str(q) + " | n = " + str(n))
print("e = " + str(e) + " | d = " + str(d))
print("===================")
print("message : " + msg)
print("===================")
print("encrypt message : " + e_msg)
print("decrypt message : " + d_msg)
