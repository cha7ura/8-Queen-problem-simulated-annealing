import random,  math
import decimal

class Board:
    def __init__(self, queen_count=8):
        self.queen_count = queen_count
        self.reset()

    def reset(self):
        self.queens = [-1 for i in range(0, self.queen_count)]
        for i in range(0, self.queen_count):
            self.queens[i] = random.randint(0, self.queen_count - 1)

    def calculateCostWithQueens(queens):
        hueristic_val = 0
        queen_count = len(queens)
        for queen in range(0, queen_count):
            for next_queen in range(queen+1, queen_count):
                if queens[queen] == queens[next_queen] or abs(queen - next_queen) == abs(queens[queen] - queens[next_queen]):
                    hueristic_val += 1
        return hueristic_val

    def toString(queens):
        board_string = ""
        for row, col in enumerate(queens):
            board_string += "(%s, %s)\n" % (row, col)
        return board_string

    def __str__(self):
        board_string = ""
        for row, col in enumerate(self.queens):
            board_string += "(%s, %s)\n" % (row, col)
        return board_string

class SimulatedAnnealing:
    def __init__(self, board):
        self.board = board
        self.temperature = 64
        self.anneal_rate = 0.95

    def run(self):
        board = self.board
        board_queens = self.board.queens[:]
        solutionFound = False
        for k in range(0, 150000):
            self.temperature *= self.anneal_rate
            board.reset()
            successor_queens = board.queens[:]
            deltaE = Board.calculateCostWithQueens(successor_queens) - Board.calculateCostWithQueens(board_queens)
            exp = decimal.Decimal(decimal.Decimal(math.e) ** (decimal.Decimal(-deltaE) * decimal.Decimal(self.temperature)))

            if deltaE > 0 or random.uniform(0, 1) < exp:
                board_queens = successor_queens[:]

            if Board.calculateCostWithQueens(board_queens) == 0:
                print("Solution: Successfully optimized locations for 8 Queens")
                print(Board.toString(board_queens))
                solutionFound = True
                break

        if solutionFound == False:
            print("Solution: Unsuccessful")

if __name__ == '__main__':
    board = Board()
    print("Board: randomly generated (x,y) locations for the board ")
    print(board)
    SimulatedAnnealing(board).run()
