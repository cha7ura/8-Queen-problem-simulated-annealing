def make_row(rowdata, col, empty, full):
    items = [col] * (2*len(rowdata) + 1)
    items[1::2] = (full if d else empty for d in rowdata)
    return ''.join(items)

def make_board(board_string, col="|", row="---", empty="   ", full=" Q "):
    size = len(board_string)
    bar = make_row(board_string, col, row, row)
    boarda = [bar] * (2*size + 1)
    boarda[1::2] = (make_row([i==q for i in range(size)], col, empty, full) for q in board_string)
    return '\n'.join(boarda)

board_string =[5,2,0,6,4,7,1,3]
print(make_board(board_string))
