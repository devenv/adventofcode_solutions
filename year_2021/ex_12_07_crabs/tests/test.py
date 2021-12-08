from unittest import TestCase
from ..solution import Crabs

class Test(TestCase):

    def test_sum(self):
        self.assertEquals(Crabs([])._crab_distance(1, 3), 3)
        self.assertEquals(Crabs([])._crab_distance(1, 4), 6)
        self.assertEquals(Crabs([])._crab_distance(1, 5), 10)
        self.assertEquals(Crabs([])._crab_distance(3, 1), 3)
        self.assertEquals(Crabs([])._crab_distance(4, 1), 6)
        self.assertEquals(Crabs([])._crab_distance(5, 1), 10)

    def test_fuel_consumption(self):
        self.assertEquals(Crabs([1, 2, 3]).fuel_consumtion_to(2), 2)
        self.assertEquals(Crabs([1, 2, 3]).fuel_consumtion_to(1), 4)
        self.assertEquals(Crabs([1, 2, 3, 4]).fuel_consumtion_to(1), 10)

    def test_best_target(self):
        self.assertEquals(Crabs([1, 2, 3]).best_target(), 2)
        self.assertEquals(Crabs([1, 2, 3, 4]).best_target(), 2)
        self.assertEquals(Crabs([1, 2, 3, 4, 10]).best_target(), 4)
        self.assertEquals(Crabs([16, 1, 2, 0, 4, 2, 7, 1, 2, 14]).best_target(), 5)