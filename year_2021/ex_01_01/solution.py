from year_2021.utils.input import read_input

last = [0, 0, 0]
count = 0
input = read_input()
for line in input:
    n = int(line.strip())
    s = n + last[1] + last[2]
    if 0 not in last and s > sum(last):
        count += 1
    last = [last[1], last[2], n]

print(count)