def ganhable_color_pieces_pos(board: list, pos: tuple) -> list:

    x = pos[0]
    y = pos[1]

    pos_piece_color = board[x][y]

    result = []

    # check for row
    if (
        1 <= x <= 3
        and board[x - 1][y] == board[x + 1][y]
        and board[x - 1][y] != 0
        and board[x - 1][y] != pos_piece_color
    ):
        result.insert(0, (x - 1, y))
        result.insert(0, (x + 1, y))

    # check for column
    if (
        1 <= y <= 3
        and board[x][y - 1] == board[x][y + 1]
        and board[x][y - 1] != 0
        and board[x][y - 1] != pos_piece_color
    ):
        result.insert(0, (x, y - 1))
        result.insert(0, (x, y + 1))

    # top to bottom, left to right
    if (
        1 <= x <= 3
        and 1 <= y <= 3
        and board[x - 1][y - 1] == board[x + 1][y + 1]
        and board[x - 1][y - 1] != 0
        and board[x - 1][y - 1] != pos_piece_color
    ):
        result.insert(0, (x - 1, y - 1))
        result.insert(0, (x + 1, y + 1))

    # top to bottom, right to left
    if (
        1 <= x <= 3
        and 1 <= y <= 3
        and board[x - 1][y + 1] == board[x + 1][y - 1]
        and board[x - 1][y + 1] != 0
        and board[x - 1][y + 1] != pos_piece_color
    ):
        result.insert(0, (x - 1, y + 1))
        result.insert(0, (x + 1, y - 1))

    return result

# return possible adding to current pos move
def legal_move_helper(board: list, pos: tuple, surrounds_pos: list) -> list:
    return [
        (x, y)
        for x, y in surrounds_pos
        if -1 < pos[0] + x < 5 and -1 < pos[1] + y < 5
    ]

# return all possible move of a pos
def legal_move(board: list, pos: tuple) -> list:
    # if it's on the upper row edge
    if pos[0] == 0:
        # in the odd column
        if pos[1] % 2 != 0:
            surrounds = legal_move_helper(board, pos, [(0, -1), (0, 1), (1, 0)])
        # in the even column
        else:
            surrounds = legal_move_helper(
                board, pos, [(0, -1), (1, -1), (1, 0), (1, 1), (0, 1)]
            )

        surrounds = [
            (pos[0] + x, pos[1] + y)
            for (x, y) in surrounds
            if board[pos[0] + x][pos[1] + y] == 0
        ]

        return surrounds

    # if it's on the bottom row edge
    if pos[0] == 4:
        # in the odd column
        if pos[1] % 2 != 0:
            surrounds = legal_move_helper(board, pos, [(0, -1), (0, 1), (-1, 0)])
        # in the even column
        else:
            surrounds = legal_move_helper(
                board, pos, [(0, -1), (0, 1), (-1, -1), (-1, 1), (-1, 0)]
            )

        surrounds = [
            (pos[0] + x, pos[1] + y)
            for (x, y) in surrounds
            if board[pos[0] + x][pos[1] + y] == 0
        ]

        return surrounds

    # if it's on the left column edge
    if pos[1] == 0:
        # it it's on the odd row
        if pos[0] % 2 != 0:
            # surrounds = legal_move_helper(board, pos, [(-1, 0), (0, 1), (1, 0)])
            surrounds = legal_move_helper(board, pos, [(0, 1), (-1, 0), (1, 0)])
        # in the even row
        else:
            surrounds = legal_move_helper(
                board, pos, [(-1, 0), (1, 0), (-1, 1), (0, 1), (1, 1)]
            )

        surrounds = [
            (pos[0] + x, pos[1] + y)
            for (x, y) in surrounds
            if board[pos[0] + x][pos[1] + y] == 0
        ]

        return surrounds

    # if it's on the right column edge
    if pos[1] == 4:
        # it it's on the odd row
        if pos[0] % 2 != 0:
            surrounds = legal_move_helper(board, pos, [(0, -1), (-1, 0), (1, 0)])
        # in the even row
        else:
            surrounds = legal_move_helper(
                board, pos, [(0, -1), (-1, 0), (1, 0), (-1, -1), (1, -1)]
            )

        surrounds = [
            (pos[0] + x, pos[1] + y)
            for (x, y) in surrounds
            if board[pos[0] + x][pos[1] + y] == 0
        ]

        return surrounds

    # six ways move
    if (pos[0], pos[1]) in [(1, 1), (1, 3), (2, 2), (3, 1), (3, 3)]:
        surrounds = legal_move_helper(
            board,
            pos,
            [(-1, -1), (1, 1), (-1, 0), (1, 0), (0, 1), (0, -1), (-1, 1), (1, -1)],
        )

        surrounds = [
            (pos[0] + x, pos[1] + y)
            for (x, y) in surrounds
            if board[pos[0] + x][pos[1] + y] == 0
        ]

        return surrounds

    # four ways move
    if (pos[0], pos[1]) in [(1, 2), (2, 1), (2, 3), (3, 2)]:
        surrounds = legal_move_helper(board, pos, [(1, 0), (-1, 0), (0, 1), (0, -1)])
        surrounds = [
            (pos[0] + x, pos[1] + y)
            for (x, y) in surrounds
            if board[pos[0] + x][pos[1] + y] == 0
        ]
        return surrounds

    return []

def possiblePos(pos: tuple):
    """return the possible position can go from one position
    incase a chess going out of the board.
    """
    surroundPos = [(-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1), (1, 0), (0, 1), (1, 1)]
    posNotHasCrossMove = [
        (0, 1),
        (1, 0),
        (0, 3),
        (3, 0),
        (2, 1),
        (1, 2),
        (4, 3),
        (3, 4),
        (4, 1),
        (1, 4),
        (2, 3),
        (3, 2),
    ]

    if pos in posNotHasCrossMove:
        possiPos = [
        (x, y) for x, y in surroundPos if -1 < pos[0] + x < 5 and -1 < pos[1] + y < 5 and (x == 0 or y == 0)
        ]
    else :
        possiPos = [
        (x, y) for x, y in surroundPos if -1 < pos[0] + x < 5 and -1 < pos[1] + y < 5
        ]

    return possiPos

def lostChiRecursive(
    board: list,
    enemy: int,
    enemyPos: tuple,
    lostedChiEnemy: list,
    visitedEnemy: list,
    notLostChiEnemy: list,
):
    if enemyPos in visitedEnemy:
        if enemyPos in notLostChiEnemy:
            return False
        else:
            return True
    else:
        visitedEnemy.append(enemyPos)

    if len(legal_move(board, enemyPos)) == 0:
        lostedChiEnemy.append(enemyPos)
    else:
        notLostChiEnemy.append(enemyPos)
        return False

    for move in possiblePos(enemyPos):
        if board[enemyPos[0] + move[0]][enemyPos[1] + move[1]] == enemy:
            if (
                lostChiRecursive(
                    board,
                    enemy,
                    (enemyPos[0] + move[0], enemyPos[1] + move[1]),
                    lostedChiEnemy,
                    visitedEnemy,
                    notLostChiEnemy,
                )
                == False
            ):
                notLostChiEnemy.append(enemyPos)
                return False
    return True

# board: moved but hasn't changed color yet ; nextPos: current post
def lostChi(board: list, player: int, nextPos: tuple):
    """return the number of enemy has been taken chi"""
    lostedChiEnemy = []
    notLostChiEnemy = []
    oneDirection = []
    visitedEnemy = []

    for (x, y) in possiblePos(nextPos):
        if board[nextPos[0] + x][nextPos[1] + y] == -player:
            if (
                lostChiRecursive(
                    board,
                    -player,
                    (nextPos[0] + x, nextPos[1] + y),
                    oneDirection,
                    visitedEnemy,
                    notLostChiEnemy,
                )
                == False
            ):
                oneDirection.clear()
            else:
                lostedChiEnemy += oneDirection
                oneDirection.clear()

    return lostedChiEnemy

def make_a_move(board: list, current_pos: tuple, next_pos: tuple) -> int:
    # current_pos piece type?
    player = board[current_pos[0]][current_pos[1]]
    # set current_pos piece type = 0, moving piece
    board[current_pos[0]][current_pos[1]] = 0
    # set next_pos piece = player, done moving
    board[next_pos[0]][next_pos[1]] = player
    # ganhable pieces surround new pos
    surrounds = ganhable_color_pieces_pos(board, next_pos)
    # position where loss chi
    # lost_chi = lostChi(board, player, (next_pos[0], next_pos[1]))
    # combine surrounds and lost_chi
    # surrounds = surrounds + lost_chi
    for piece in surrounds:
        board[piece[0]][piece[1]] = player

    lostChiEnemy = []
    lostChiEnemy += lostChi(board, player, (next_pos[0], next_pos[1]))
    for (x, y) in surrounds:
        lostChiEnemy += lostChi(board, player, (x, y))

    for piece in lostChiEnemy:
        board[piece[0]][piece[1]] = player

    return board