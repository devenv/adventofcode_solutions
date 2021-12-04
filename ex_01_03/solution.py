from enum import Enum

def dec(line):
    return int(line, 2)

class OC(Enum):
    OXYGEN = 0
    CARBON = 1

class Bits:
    bits = None
    additions = 0
    def __init__(self, length) -> None:
        self.bits = [0] * length

    def add(self, line):
        n = 0
        for char in line:
            if char == '1':
                self.bits[n] += 1
            n += 1
        self.additions += 1
    
    def g(self):
        return dec(''.join(['1' if bit > self.additions / 2 else '0' for bit in self.bits]))

    def e(self):
        return dec(''.join(['1' if bit < self.additions / 2 else '0' for bit in self.bits]))

    def power(self):
        return self.g() * self.e()

    def right(self, line, oc, n):
        bit = self.bits[n]
        match oc:
            case OC.OXYGEN:
                if bit >= self.additions / 2 and line[n] != '1':
                    return False
                if bit < self.additions / 2 and line[n] != '0':
                    return False
            case OC.CARBON:
                if bit < self.additions / 2 and line[n] != '1':
                    return False
                if bit >= self.additions / 2 and line[n] != '0':
                    return False
            case _: return True
        return True

if __name__ == "__main__":
    bits = None
    with open('ex_01_03/input.txt') as f:
        for line in f.readlines():
            if not bits:
                bits = Bits(len(line.strip()))
            bits.add(line.strip())
    print(bits.bits)
    print(bits.power())


    data = []
    with open('ex_01_03/input.txt') as f:
        data = [line.strip() for line in f.readlines()]

    def find(data, oc):
        n = 0
        while len(data) > 1:
            new_data = []
            bits = Bits(len(data[0]))
            for line in data:
                bits.add(line.strip())
            for line in data:
                if bits.right(line, oc, n):
                    new_data.append(line)
            data = new_data
            n += 1
        return data[0]


    o_winner = find(data, OC.OXYGEN)
    c_winner = find(data, OC.CARBON)
    print(o_winner)
    print(c_winner)
    print(dec(o_winner) * dec(c_winner))