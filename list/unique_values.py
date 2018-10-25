import unittest

def UniqueSequence(seq):
    a = []
    for v in seq:
        i = 0
        a.append(v)
        while a[i] != v:
            i = i + 1
        i = i + 1
        if i != len(a):
            del a[-1]
    return a

test_list = [1, 2, 2, 3]


class TestUniqueSequence(unittest.TestCase):
    def test_Success(self):
        test_list = [1, 2, 2, 3]
        unique_list = [1, 2, 3]

        self.assertEqual(UniqueSequence(test_list), unique_list)