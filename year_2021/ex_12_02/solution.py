h = 0
d = 0
a = 0
with open('year_2021/ex_12_02/input.txt') as f:
    for line in f.readlines():
        x = int(line.split(' ')[1])
        match line.split(' ')[0]:
            case 'forward':
                h += x
                d += a * x
            case 'up': a -= x
            case 'down': a += x
print(h)
print(d)
print(h * d)