from dataclasses import dataclass


@dataclass
class Cell:
    number: int
    marked: bool = False

    def __repr__(self) -> str:
        return f"{self.number}:{self.marked}"


@dataclass
class Board:
    cells: list[list[Cell]]

    def is_bingo(self):
        return (
            self._any_bingo_lines(self.cells)
            or 
            self._any_bingo_lines(self._transposed())
        )

    def mark(self, number):
        for line  in self.cells:
            for cell in line:
                if cell.number == number:
                    cell.marked = True 
    
    def unmarked_sum(self):
        sum = 0
        for line  in self.cells:
            for cell in line:
                if not cell.marked:
                    sum += cell.number
        return sum

    def _any_bingo_lines(self, cells):
        return any([all(cell.marked for cell in line) for line in cells])

    def _transposed(self):
        return [[self.cells[j][i] for j in range(len(self.cells))] for i in range(len(self.cells[0]))]

    def __repr__(self) -> str:
        return "\n".join([",".join([repr(cell) for cell in line]) for line in self.cells])


class Loader:

    def load_numbers(self, line):
        return [int(number.strip()) for number in line.split(',')]

    def load_boards(self, lines):
        boards = []
        board = Board([])

        for line in lines:
            if line == '':
                boards.append(board)
                board = Board([])
                continue
            board.cells.append([Cell(int(number.strip())) for number in line.split(' ') if number != ''])
        boards.append(board)
        return boards

class Bingo:
    boards: list[Board]

if __name__ == "__main__":
    with open("year_2021/ex_01_04_bingo/input.txt") as fp:
        input = [line.strip() for line in fp.readlines()]
        loader = Loader()
        numbers = loader.load_numbers(input[0])
        boards = loader.load_boards(input[2:])
    winner = None

    for number in numbers:
        for board in boards:
            board.mark(number)
        winner = [board for board in boards if board.is_bingo()]
        if winner:
            winner = winner[0]
            break
    print(winner)
    print(winner.unmarked_sum())
    print(number)
    print(winner.unmarked_sum() * number)

    numbers = loader.load_numbers(input[0])
    boards = loader.load_boards(input[2:])

    last_winner = None
    last_number = 0

    for number in numbers:
        for board in boards:
            board.mark(number)
        last_winners = [board for board in boards if board.is_bingo()]
        if last_winners:
            for board in last_winners:
                boards.remove(board)
            last_winner = last_winners[0]
            last_number = number
            last_sum = last_winner.unmarked_sum()

    print(last_winner)
    print(last_sum)
    print(last_number)
    print(last_sum * last_number)