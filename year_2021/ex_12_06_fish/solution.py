from typing import List
from dataclasses import dataclass
from year_2021.utils.input import read_input


@dataclass
class Fish:
    timer: int
    amount: int

    def __init__(self, timer, amount=1):
        self.timer = timer
        self.amount = amount

    def tick(self):
        self.timer -= 1
        if self.timer < 0:
            self.timer = 6
            return Fish(8, self.amount)

    def __repr__(self) -> str:
        return f"{self.timer}:{self.amount}"

class School:
    fishes: List[Fish]

    def __init__(self):
        self.fishes = []

    def tick(self):
        new_fishes = []
        for fish in self.fishes:
            new_fish = fish.tick()
            if new_fish:
                new_fishes.append(new_fish) 
        for fish in new_fishes:
            self.add(fish)
        self._compact()

    def add(self, fish: Fish):
        for school_fish in self.fishes:
            if school_fish.timer == fish.timer: 
                school_fish.amount += 1
                return
        self.fishes.append(fish)
    
    def size(self):
        return sum(fish.amount for fish in self.fishes)

    def _compact(self):
        fish_to_delete = []
        for a_fish in self.fishes:
            similar_fishes = [fish for fish in self.fishes if fish.timer == a_fish.timer and fish is not a_fish]
            if similar_fishes and similar_fishes[0] not in fish_to_delete:
                similar_fishes[0].amount += a_fish.amount
                fish_to_delete.append(a_fish)
        for fish in fish_to_delete:
            self.fishes.remove(fish)


    def __repr__(self) -> str:
        return repr(self.fishes)


if __name__ == "__main__":
    input = read_input()

    school = School()
    for n in input[0].split(','):
        school.add(Fish(int(n)))

    for _ in range(80):
        school.tick()
    
    print(school.size())


    school = School()
    for n in input[0].split(','):
        school.add(Fish(int(n)))

    for _ in range(256):
        school.tick()
    
    print(school.size())