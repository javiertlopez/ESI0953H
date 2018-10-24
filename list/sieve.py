import unittest

def SieveList():
    prime = [True for i in range(1, 5002)]
    p = 2

    while 2 <= p < 5000:
        while prime[p] == False and 2 <= p < 5000:
            p = p + 1
        k = p + p
        while k < 5000:
            prime[k] = False
            k = k + p
        p = p + 1
    
    p = 2
    while 2 <= p < 5000:
        if prime[p]: print(p)
        p = p + 1