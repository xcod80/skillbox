import random
class Cell:
    number = 0
    symbol = ' '
    def __init__(self, number):
        self.number = number
class Board:
    board = [[Cell(0), Cell(1), Cell(2)],
             [Cell(3), Cell(4), Cell(5)],
             [Cell(6), Cell(7), Cell(8)]]
    def GetCellNumber(self, x, y):
        return self.board[y][x].number
    def print_board(self):
        print('  0 1 2')
        print(' ','-'*6)
        print('0|{}|{}|{}|'.format(self.board[0][0].symbol,self.board[0][1].symbol,self.board[0][2].symbol))
        print('1|{}|{}|{}|'.format(self.board[1][0].symbol,self.board[1][1].symbol,self.board[1][2].symbol))
        print('2|{}|{}|{}|'.format(self.board[2][0].symbol,self.board[2][1].symbol,self.board[2][2].symbol))
        print(' ','-'*6)
    def SetCellSymbol_byNumber(self, number, symbol):
        for y in range(3):
            for x in range(3):
                if self.board[y][x].number == number and self.board[y][x].symbol == ' ':
                    self.board[y][x].symbol = symbol
                    return True
        return False
    def SetCellSymbol(self, x, y, symbol):
        if self.board[y][x].symbol == ' ':
            self.board[y][x].symbol = symbol
            return True
        else:
            return False
    def ClearBoard(self):
        for y in range(3):
            for x in range(3):
                self.board[y][x].symbol = ' '
    def GetCellSymbol(self, x, y):
        return self.board[y][x].symbol
    def CheckWiner(self):
        for x in range(3):
            if self.board[x][0].symbol == self.board[x][1].symbol == self.board[x][2].symbol:
                return self.board[x][0].symbol
        for y in range(3):
            if self.board[0][y].symbol == self.board[1][y].symbol == self.board[2][y].symbol:
                return self.board[0][y].symbol
        if self.board[0][0].symbol == self.board[1][1].symbol == self.board[2][2].symbol:
            return self.board[0][0].symbol
        if self.board[0][2].symbol == self.board[1][1].symbol == self.board[2][0].symbol:
            return self.board[0][0].symbol
        return ' '
    def FreeCells(self):
        for x in range(3):
            for y in range(3):
                if self.board[x][y].symbol == ' ':
                    return True
        return False
class Player:
    cell_number = 0
    def __init__(self, name = 'Niemand'):
        self.name = name
    def choice(self, board:Board()):
        x_y = input('Введите координаты хода через пробел(горизонталь вертикаль):').split()
        self.cell_number = board.GetCellNumber(int(x_y[1]), int(x_y[0]))
        if board.GetCellSymbol(int(x_y[1]), int(x_y[0])) == ' ':
            board.SetCellSymbol_byNumber(self.cell_number, 'X')
            return True
        else:
            print('Ячейка не пустая!!!')
            return False
board = Board()
player = Player(input('Введите свое имя: '))
while board.FreeCells():
    board.print_board()
    if not player.choice(board):
        continue
    while not board.SetCellSymbol_byNumber(random.randint(0, 8), 'O'):
        pass
    if board.CheckWiner() == 'X':
        print('Победил игрок ', player.name)
        break
    elif board.CheckWiner() == 'O':
        print('Победил Компьютер!!!')
        break
else:
    print('Ничья!!!')
