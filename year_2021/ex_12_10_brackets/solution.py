from collections import deque

from year_2021.utils.input import read_input

# copy-paste from: https://www.reddit.com/r/adventofcode/comments/rd0s54/2021_day_10_solutions/ho3v37y/?utm_source=reddit&utm_medium=web2x&context=3


pairs = {"(": ")", "[": "]", "{": "}", "<": ">"}
points = {")": 3, "]": 57, "}": 1197, ">": 25137}
part1, part2 = 0, []

input = read_input()
for line in input:
    stack = deque()
    for c in line:
        if c in "([{<":
            stack.appendleft(pairs[c])
        elif c != stack.popleft():
            part1 += points[c]
            break
    else:
        score = 0
        for c in stack:
            score = score * 5 + ")]}>".index(c) + 1
        part2.append(score)

print(part1)
print(sorted(part2)[len(part2) // 2])