import unittest

def RecursiveSearch(seq, tgt, lo, hi):
    if (lo + 1) == hi:
        return -1
    m = int((lo + hi) / 2)
    if seq[m] == tgt:
        return m
    if seq[m] < tgt:
        return RecursiveSearch(seq, tgt, lo, m)
    if seq[m] > tgt:
        return RecursiveSearch(seq, tgt, m, hi)


class TestRecursiveSearch(unittest.TestCase):
    def test_Success(self):
        test_list = [1, 2, 3, 4, 5]

        self.assertEqual(RecursiveSearch(test_list, 3, 0, len(test_list)), 2)