
last = [0, 0, 0]
count = 0
with open('year_2021/ex_12_01/input.txt') as f:
    for line in f.readlines():
        n = int(line.strip())
        s = n + last[1] + last[2]
        if 0 not in last and s > sum(last):
            count += 1
        last = [last[1], last[2], n]

print(count)