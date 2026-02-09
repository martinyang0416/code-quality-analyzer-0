def countBattleships(board):
    count = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'X':
                top_ok = (i == 0) or (board[i-1][j] != 'X')
                left_ok = (j == 0) or (board[i][j-1] != 'X')
                if top_ok and left_ok:
                    count += 1
    return count