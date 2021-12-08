from year_2021.utils.input import read_input

h = 0
d = 0
a = 0
input = read_input()
for line in input:
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