from unittest import TestCase
from ..solution import Octopus, School

class Test(TestCase):

    def test_octopus_tick(self):
        self.assertEquals(Octopus(8).tick(), False)
        self.assertEquals(Octopus(9).tick(), True)

    def test_octopus_step(self):
        octopus = Octopus(9)

        octopus.flashed = False
        self.assertEquals(octopus.tick(), True)
        for _ in range(9):
            self.assertEquals(octopus.tick(), False)
        self.assertEquals(octopus.tick(), False)

        octopus.flashed = False
        for _ in range(9):
            self.assertEquals(octopus.tick(), False)
        self.assertEquals(octopus.tick(), True)

    def test_school_tick(self):
        input = ["11111", "19991", "19191", "19991", "11111"]
        after_1_step = ["34543", "40004", "50005", "40004", "34543"]
        after_2_step = ["45654", "51115", "61116", "51115", "45654"]

        school = School().load(input)
        school_after_1_step = School().load(after_1_step)
        school_after_2_step = School().load(after_2_step)

        school.tick()

        self.assertEquals(school.octopuses, school_after_1_step.octopuses)
        self.assertEquals(school.flashes, 9)

        school.tick()
        self.assertEquals(school.octopuses, school_after_2_step.octopuses)
        self.assertEquals(school.flashes, 9)

    def test_school_tick_advanced(self):
        input = ["6594254334", "3856965822", "6375667284", "7252447257", "7468496589", "5278635756", "3287952832", "7993992245", "5957959665", "6394862637"]
        after_1_step = ["8807476555", "5089087054", "8597889608", "8485769600", "8700908800", "6600088989", "6800005943", "0000007456", "9000000876", "8700006848"]
        after_2_step = ["0050900866", "8500800575", "9900000039", "9700000041", "9935080063", "7712300000", "7911250009", "2211130000", "0421125000", "0021119000"]

        school = School().load(input)
        school_after_1_step = School().load(after_1_step)
        school_after_2_step = School().load(after_2_step)

        school.tick()

        self.assertEquals(school.octopuses, school_after_1_step.octopuses)
        self.assertEquals(school.flashes, 35)

        school.tick()

        self.assertEquals(school.octopuses, school_after_2_step.octopuses)
        self.assertEquals(school.flashes, 80)