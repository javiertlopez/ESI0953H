import unittest

def binary_search(seq, tgt):
    l = 0
    h = len(seq)
    m = int((l+h) // 2)
    while(l + 1 < h and seq[m] != tgt):
        if tgt < seq[m]:
            h = m
        elif tgt > seq[m]:
            l = m
        m = int((l + h) / 2)
    if tgt == seq[m]:
        return m
    else:
        return -1

class TestBinarySearch(unittest.TestCase):
    def test_notFound(self):
        test_list = (1,2,4)
        self.assertEqual(binary_search(test_list, 3), -1)

    def test_found(self):
        test_list = (1,2,4)
        self.assertEqual(binary_search(test_list, 4), 2)
