import unittest
import math
import random

def RandomEvaluation(seq):
    count = [0 for i in range(1, 11)]
    for i in seq:
        x = i * 10
        x = int(round(x, 0))
        count[x] = count[x] + 1
    
    for i in count:
        print (i)

prime = [random.random() for i in range(1, 23)]
RandomEvaluation(prime)