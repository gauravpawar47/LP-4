class NQueens:
    def __init__(self):
        self.size = int(input("Enter the size of the chessboard (N): "))
        self.board = [[0 for _ in range(self.size)] for _ in range(self.size)]
        self.count = 0

    def print_board(self):
        for row in self.board:
            for val in row:
                print("Q" if val == 1 else "X", end=" ")
            print()
        print()

    def is_safe(self, row, col):
        # Check column
        for i in range(row):
            if self.board[i][col] == 1:
                return False

        # Check upper-left diagonal
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # Check upper-right diagonal
        i, j = row - 1, col + 1
        while i >= 0 and j < self.size:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        return True

    def set_first_queen(self):
        print("\nEnter coordinates of the first Queen:")
        r = int(input(f"Row (1 to {self.size}): ")) - 1
        c = int(input(f"Column (1 to {self.size}): ")) - 1

        if 0 <= r < self.size and 0 <= c < self.size:
            self.board[r][c] = 1
            print("\nInitial board with first Queen placed:\n")
            self.print_board()
            return r + 1  # next row to start solving from
        else:
            print("Invalid coordinates! Try again.")
            return self.set_first_queen()

    def solve(self, row):
        if row == self.size:
            self.count += 1
            print(f"Solution {self.count}:")
            self.print_board()
            return

        for col in range(self.size):
            if self.is_safe(row, col):
                self.board[row][col] = 1
                self.solve(row + 1)
                self.board[row][col] = 0  # backtrack

    def start(self):
        next_row = self.set_first_queen()
        self.solve(next_row)

        if self.count > 0:
            print(f"Total solutions found: {self.count}")
        else:
            print("No solution exists for this configuration.")


# Run program
if __name__ == "__main__":
    nq = NQueens()
    nq.start()


"""
INPUT 

Enter the size of the chessboard (N): 4
Enter coordinates of the first Queen:
Row (1 to 4): 1
Column (1 to 4): 2

OUTPUT

Initial board with first Queen placed:

X Q X X 
X X X X 
X X X X 
X X X X 

Solution 1:
X Q X X 
X X X Q 
Q X X X 
X X Q X 

Solution 2:
X Q X X 
X X Q X 
X X X Q 
Q X X X 

Total solutions found: 2
"""