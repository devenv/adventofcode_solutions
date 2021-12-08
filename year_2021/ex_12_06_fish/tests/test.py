from unittest import TestCase
from ..solution import Fish, School

class Test(TestCase):

    def test_fish_tick(self):
        fish = Fish(1, 2)
        self.assertIsNone(fish.tick())
        self.assertEquals(fish.tick(), Fish(8, 2))
        self.assertEquals(fish.timer, 6)

    def test_school_tick(self):
        school = School()
        school.add(Fish(1))
        school.tick()
        school.tick()
        self.assertEquals(school.fishes, [Fish(6), Fish(8)])
        self.assertEquals(school.size(), 2)

    def test_school_compact_on_add(self):
        school = School()
        school.add(Fish(1))
        school.add(Fish(1))
        school.tick()
        self.assertEquals(school.fishes, [Fish(0, 2)])
        self.assertEquals(school.size(), 2)

    def test_school_compact_on_tick(self):
        school = School()
        school.add(Fish(0))
        school.add(Fish(7))
        school.tick()
        self.assertEquals(school.fishes, [Fish(6, 2), Fish(8)])
        self.assertEquals(school.size(), 3)