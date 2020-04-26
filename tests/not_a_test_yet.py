import unittest
from Medusa.Sort import sort as srt

class TestSortingAlgs(unittest.TestCase) {
    @classmethod
    def test_short_numeric_sorting() {
        a = [4, 1, -23, 59, 34, 30]
        self.assertTrue(srt(a), [-23, 1, 4, 30, 34, 59])
    }
}
