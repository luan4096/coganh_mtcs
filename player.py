import copy
from math import sqrt, log
import random
from mytool import *
import time

C = 2               # constant for ucb function
rollOutTime = 500   # number of roll out time
buildTreeTime = 100 # decide the amount of time to build tree

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
    score = 0
    if len(node.child) == 0:    # check if this is leaf node, 0 mean leaf node
        if node.visit == 0:     # check if this node has been visited before, 0 mean hasn't
            score = rollOut(node.board, -1, rollOutTime)
        else:
            # currBoard = copy.deepcopy(currNode.board)
            thereIsPlayer = False   # this variable is used to check if there is our player in the 
            for i in range(5):
                for j in range(5):
                    if currNode.board[i][j] == player:
                        thereIsPlayer = True
                        lm = legal_move(currNode.board, (i, j))
                        if len(lm) == 0:
                            continue
                        for move in lm:
                            currBoard = copy.deepcopy(currNode.board)
                            node.child.append(treeNode(make_a_move(currBoard, (i, j), move), 0, 0, (i, j), move))
            if thereIsPlayer:
                score = buildTree(node.child[0], player)

    else:
        maxUcb = -1
        bestNode = None
        for n in node.child:
            temp = ucb(n)
            if temp > maxUcb:
                maxUcb = temp
                bestNode = n
        if bestNode != None:
            score = buildTree(bestNode, player)
        else: score = buildTree(node.child[0], player)

    node.visit += 1
    node.score += score
    return score

def moveNoTime(board: list, player: int):
    root = treeNode(board, 0, 0, (), ())
    
    for i in range(buildTreeTime):
        buildTree(root, -1)
    
    bestScore = -9999
    bestNode = None
    for node in root.child:
        if node.score > bestScore:
            bestScore = node.score
            bestNode = node

    board_print(bestNode.board)
    return bestNode.move
    
def move(board: list, player: int, remain_time):
    pass

board = [
    [ 1, 1, 1, 1, 1],
    [ 1, 0, 0, 0, 1],
    [ 1, 0, 0, 0,-1],
    [-1, 0, 0, 0,-1],
    [-1,-1,-1,-1,-1]
]

board0 = [
    [ 1, 1,-1,-1,-1],
    [ 1, 1,-1, 0,-1],
    [-1,-1, 0, 0,-1],
    [-1, 0,-1, 0,-1],
    [-1,-1,-1,-1,-1]
]

small_board = [
    [ 1, 1, 1, 0, 0],
    [ 1, 0, 1, 0, 0],
    [-1,-1,-1, 0, 0],
    [ 0, 0, 0, 0, 0],
    [ 0, 0, 0, 0, 0]
]

x = time.time()
print(moveNoTime(board0, -1))
# board_print(make_a_move(board0, (3, 2), (2, 2)))
print(f"time: {time.time() - x}")


