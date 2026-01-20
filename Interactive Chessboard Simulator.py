import sys, copy

# Starting position of all chess pieces
STARTING_PIECES = {
    'a8': 'bR', 'b8': 'bN', 'c8': 'bB', 'd8': 'bQ',
    'e8': 'bK', 'f8': 'bB', 'g8': 'bN', 'h8': 'bR',
    'a7': 'bP', 'b7': 'bP', 'c7': 'bP', 'd7': 'bP',
    'e7': 'bP', 'f7': 'bP', 'g7': 'bP', 'h7': 'bP',

    'a1': 'wR', 'b1': 'wN', 'c1': 'wB', 'd1': 'wQ',
    'e1': 'wK', 'f1': 'wB', 'g1': 'wN', 'h1': 'wR',
    'a2': 'wP', 'b2': 'wP', 'c2': 'wP', 'd2': 'wP',
    'e2': 'wP', 'f2': 'wP', 'g2': 'wP', 'h2': 'wP'
}

# Chessboard template
BOARD_TEMPLATES = """
  a   b   c   d   e   f   g   h
 ____ ____ ____ ____ ____ ____ ____ ____
8 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
7 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
6 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
5 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
4 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
3 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
2 ||{}|| {} ||{}|| {} ||{}|| {} ||{}|| {} |
  ||||||____||||||____||||||____||||||____|
1 | {} ||{}|| {} ||{}|| {} ||{}|| {} ||{}||
  |____||||||____||||||____||||||____||||||
"""

WHITE_SQUARE = '||'
BLACK_SQUARE = '  '

def print_chessboard(board):
    squares = []
    is_white_square = True

    for y in '87654321':
        for x in 'abcdefgh':
            square = x + y
            if square in board:
                squares.append(board[square])
            else:
                if is_white_square:
                    squares.append(WHITE_SQUARE)
                else:
                    squares.append(BLACK_SQUARE)

            is_white_square = not is_white_square
        
        is_white_square = not is_white_square
    
    print(BOARD_TEMPLATES.format(*squares))

# Program intro
print()
print('Interactive Chessboard')
print('by R.M. Musthak')
print()
print('Pieces')
print(' w - White, b - Black')
print(' P - Pawn, N - Knight, B - Bishop, R - Rook, Q - Queen, K - King')
print()
print('Commands:')
print(' move e2 e4   - Move piece')
print(' remove e2    - Remove piece')
print(' set e2 wP    - Set a piece')
print(' reset        - Reset board')
print(' clear        - Clear board')
print(' fill wP      - Fill board')
print(' quit         - Quit')
print()

main_board = copy.copy(STARTING_PIECES)

while True:
    print_chessboard(main_board)
    response = input('> ').split()

    if len(response) == 0:
        continue

    if response[0] == 'move':
        main_board[response[2]] = main_board[response[1]]
        del main_board[response[1]]

    elif response[0] == 'remove':
        del main_board[response[1]]

    elif response[0] == 'set':
        main_board[response[1]] = response[2]

    elif response[0] == 'reset':
        main_board = copy.copy(STARTING_PIECES)

    elif response[0] == 'clear':
        main_board = {}

    elif response[0] == 'fill':
        for y in '87654321':
            for x in 'abcdefgh':
                main_board[x + y] = response[1]

    elif response[0] == 'quit':
        sys.exit()
        