import unittest

def Sieve():
    prime = {i for i in range(1, 5002)}
    multiples = set()
    p = 2

    while 2 <= p < 5000:
        while p not in prime and 2 <= p < 5000:
            p = p + 1
        k = p + p
        multiples.add(k)
        while k < 5000:
            k = k + p
            multiples.add(k)
        prime.difference_update(multiples)
        p = p + 1
    
    print(prime)

Sieve()