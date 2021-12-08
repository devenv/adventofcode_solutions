from functools import  reduce
from typing import Optional
from dataclasses import dataclass

from year_2021.utils.input import read_input


class Digit:

    digit: Optional[int]

    def __init__(self, letters: str):
        self.letters = letters
        match len(letters):
            case 2: self.digit = 1
            case 3: self.digit = 7
            case 4: self.digit = 4
            case 7: self.digit = 8
            case _: self.digit = None

    def __repr__(self) -> str:
        return f"{self.digit}:{self.letters}"


if __name__ == "__main__":
    input = read_input()
    digits = []
    for line in input:
        right = line.split('|')[1].strip()
        for letters in right.split(' '):
            digits.append(Digit(letters))

    known = sum(1 for digit in digits if digit.digit != None)
    print(known)


# second part stolen from reddit: https://www.reddit.com/r/adventofcode/comments/rbj87a/2021_day_8_solutions/hnq47cy/

def find_first(seq, pred):
    return next(item for item in seq if pred(item))


def solve(input):
    total = 0
    for line in input:
        patterns, output = line.split(' | ')
        patterns = [set(pattern) for pattern in patterns.split(' ')]
        output = [set(pattern) for pattern in output.split(' ')]

        solved = [None] * 10

        solved[1] = find_first(patterns, lambda digit: len(digit) == 2)
        solved[7] = find_first(patterns, lambda digit: len(digit) == 3)
        solved[8] = find_first(patterns, lambda digit: len(digit) == 7)
        solved[4] = find_first(patterns, lambda digit: len(digit) == 4)

        # this is very smart
        maybe_069 = [digit for digit in patterns if len(digit) == 6]
        solved[6] = find_first(maybe_069, lambda digit: len(digit & solved[1]) == 1)
        solved[9] = find_first(maybe_069, lambda digit: len(digit & solved[4]) == 4)
        solved[0] = find_first(maybe_069, lambda digit: digit != solved[9] and digit != solved[6])

        maybe_235 = [digit for digit in patterns if len(digit) == 5]
        solved[3] = find_first(maybe_235, lambda digit: len(digit & solved[1]) == 2)
        solved[5] = find_first(maybe_235, lambda digit: len(digit & solved[6]) == 5)
        solved[2] = find_first(maybe_235, lambda digit: digit != solved[3] and digit != solved[5])

        total += reduce(lambda acc, digit: 10 * acc + solved.index(digit), output, 0)

    return total

print(solve(read_input()))