import unittest

def QuickSort(a, lo, hi):
    if lo < hi:
        split = Partition(a, lo, hi)
        QuickSort(a, lo, split - 1)
        QuickSort(a, split + 1, hi)


def Partition(a, lo, hi):
    x = a[hi]
    i = lo - 1

    for j in range(lo , hi):
        if a[j] <= x:
            i = i + 1
            swap = a[i]
            a[i] = a[j]
            a[j] = swap

    swap = a[i + 1]
    a[i + 1] = a[hi]
    a[hi] = swap
    return i + 1

class TestQuickSort(unittest.TestCase):
    def test_Success(self):
        test_list = [7, 3, 5, 0]
        order_list = [0, 3, 5, 7]
        QuickSort(test_list, 0, len(test_list) - 1)

        self.assertEqual(test_list, order_list)