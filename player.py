import copy
from math import sqrt, log
import random
from mytool import *

C = 2           # constant for ucb function
endPoint = 20   # decide when to end buildTree 

class treeNode():
    def __init__(self, board: list, visit: int, score: int, oldPos: tuple, newPos: tuple):
        self.board = board
        self.visit = visit
        self.score = score
        self.move = (oldPos, newPos)
        self.child = []

def ucb(node: treeNode) -> int:
    if node.visit == 0:
        return 999
    return node.score + C * sqrt(log(node.visit) / node.visit)

def rollOut(board: list, player: int, n: int) -> int:
    """
    randomly simulate the game in n moves 
    and return the score of the final board
    """
    currBoard = copy.deepcopy(board)
    for t in range(n):  # simulate in n moves
        randList = []
        for i in range(5):
            for j in range(5):
                if currBoard[i][j] == player:
                    randList.append((i, j))
        if len(randList) == 0:
            break
        avalableMove = []
        while len(avalableMove) == 0:
            pos = random.choice(randList)
            avalableMove = legal_move(currBoard, pos)
        nextPos = random.choice(avalableMove)
        currBoard = make_a_move(currBoard, pos, nextPos)
        player = -player
    
    score = 0
    for i in range(5):
        for j in range(5):
            if currBoard[i][j] == player:
                score += 1
            elif currBoard[i][j] == -player:
                score -= 1

    return score

def buildTree(node: treeNode, player: int) -> int:
    currNode = node
    if len(node.child) == 0:    # check if this is leaf node, 0 mean leaf node
        if node.visit == 0:     # check if this node has been visited before, 0 mean hasn't
            score = rollOut(node.board, -1, 60)
        else:
            currBoard = currNode.board
            for i in range(5):
                for j in range(5):
                    if currBoard[i][j] == player:
                        lm = legal_move(currBoard, (i, j))
                        if len(lm) == 0:
                            lm.append(1)
                        for move in lm:
                            node.child.append(treeNode(make_a_move(currBoard, (i, j), move), 0, 0, (i, j), move))
            score = buildTree(node.child[0], player)

    else:
        maxUcb = -1
        for n in node.child:
            temp = ucb(n)
            if temp > maxUcb:
                maxUcb = temp
                bestNode = n
        score = buildTree(bestNode, player)

    node.visit += 1
    node.score += score
    return score



def move(board: list, player: int):
    root = treeNode(board, 0, 0, (), ())
    
    for i in range(100):
        buildTree(root, -1)
    
    bestScore = -1
    bestNode = None
    for node in root.child:
        if node.score > bestScore:
            bestScore = node.score
            bestNode = node

    print(root.child)
    

# def move(board: list, player: int, remain_time):
#     pass

def board_print(board):
    for i in [0, 1, 2, 3, 4]:
        print("[{}]".format(i), ":", end=" ")
        for j in range(5):
            if board[i][j] == -1:
                print("{}".format(board[i][j]), end=" ")
            else:
                print(" {}".format(board[i][j]), end=" ")
        print()
    print("     ", "[0", " 1", " 2", " 3", " 4]")
    print("")

board = [
    [ 1, 1, 1, 1, 1],
    [ 1, 0, 0, 0, 1],
    [ 1, 0, 0, 0,-1],
    [-1, 0, 0, 0,-1],
    [-1,-1,-1,-1,-1]
]

move(board, -1)


