import displayFunctions

# -----------------------------------------------
# -----------------------------------------------

"""
Justin Andrews
Spring 2020
CS455 - Artificial Intelligence
Peg Game - Final Project

File Description:
This file contains functions related to game state and playing the game.

Function Declarations:
    checkClick(clickX, clickY)
    
    checkMove(peg1, peg2, peg3, pegList)
    
    doMove(peg1, peg2, peg3, pegs, screen)
    
    anyMoves(pegs)
"""


# -----------------------------------------------
# -----------------------------------------------


def checkClick(clickX, clickY):
    """
    Function Description:
    here

    :param clickX:
    :param clickY:
    :return:
    """

    # check based on click position which peg was selected
    if 520 > clickX > 480 and 165 < clickY < 198:
        pegSelected = 0
        validClick = True
    elif 460 > clickX > 427 and 262 < clickY < 288:
        pegSelected = 1
        validClick = True
    elif 569 > clickX > 537 and 257 < clickY < 286:
        pegSelected = 2
        validClick = True
    elif 402 > clickX > 369 and 355 < clickY < 382:
        pegSelected = 3
        validClick = True
    elif 514 > clickX > 484 and 357 < clickY < 384:
        pegSelected = 4
        validClick = True
    elif 628 > clickX > 600 and 357 < clickY < 384:
        pegSelected = 5
        validClick = True
    elif 342 > clickX > 315 and 452 < clickY < 480:
        pegSelected = 6
        validClick = True
    elif 458 > clickX > 427 and 453 < clickY < 479:
        pegSelected = 7
        validClick = True
    elif 569 > clickX > 536 and 451 < clickY < 484:
        pegSelected = 8
        validClick = True
    elif 688 > clickX > 658 and 452 < clickY < 481:
        pegSelected = 9
        validClick = True
    elif 290 > clickX > 262 and 547 < clickY < 577:
        pegSelected = 10
        validClick = True
    elif 401 > clickX > 373 and 547 < clickY < 577:
        pegSelected = 11
        validClick = True
    elif 515 > clickX > 486 and 547 < clickY < 576:
        pegSelected = 12
        validClick = True
    elif 628 > clickX > 595 and 547 < clickY < 577:
        pegSelected = 13
        validClick = True
    elif 748 > clickX > 718 and 546 < clickY < 576:
        pegSelected = 14
        validClick = True
    else:
        pegSelected = -1
        validClick = False

    # return if a peg was clicked and what peg was clicked
    return validClick, pegSelected


# -----------------------------------------------


def checkMove(peg1, peg2, peg3, pegList):
    """
    Function Description:
    here

    :param peg1: int value of the first peg in the move, the peg to jump
    :param peg2: int value of the second peg in the move, the peg to be jumped
    :param peg3: int value of the third peg in the move, the spot for the first peg to jump to
    :param pegList: array of True and False values corresponding to current peg locations
    :return: True or False value if the move is valid and the move can be completed with the current game state
    """

    # the move that wants to be performed
    move = [peg1, peg2, peg3]

    moveValid = False

    valid = False

    # check if the move is valid
    if peg1 == 0:
        if (peg2 == 1 or peg2 == 2) and (peg3 == 3 or peg3 == 5):
            moveValid = True

    elif peg1 == 1:
        if (peg2 == 3 or peg2 == 4) and (peg3 == 6 or peg3 == 8):
            moveValid = True

    elif peg1 == 2:
        if (peg2 == 4 or peg2 == 5) and (peg3 == 7 or peg3 == 9):
            moveValid = True

    elif peg1 == 3:
        if (peg2 == 1 or peg2 == 4 or peg2 == 7 or peg2 == 6) and (peg3 == 0 or peg3 == 5 or peg3 == 12 or peg3 == 10):
            moveValid = True

    elif peg1 == 4:
        if (peg2 == 7 or peg2 == 8) and (peg3 == 11 or peg3 == 13):
            moveValid = True

    elif peg1 == 5:
        if (peg2 == 2 or peg2 == 4 or peg2 == 8 or peg2 == 9) and (peg3 == 0 or peg3 == 3 or peg3 == 12 or peg3 == 14):
            moveValid = True

    elif peg1 == 6:
        if (peg2 == 3 or peg2 == 7) and (peg3 == 1 or peg3 == 8):
            moveValid = True

    elif peg1 == 7:
        if (peg2 == 8 or peg2 == 4) and (peg3 == 9 or peg3 == 2):
            moveValid = True

    elif peg1 == 8:
        if (peg2 == 4 or peg2 == 7) and (peg3 == 1 or peg3 == 6):
            moveValid = True

    elif peg1 == 9:
        if (peg2 == 5 or peg2 == 8) and (peg3 == 2 or peg3 == 7):
            moveValid = True

    elif peg1 == 10:
        if (peg2 == 6 or peg2 == 11) and (peg3 == 3 or peg3 == 12):
            moveValid = True

    elif peg1 == 11:
        if (peg2 == 7 or peg2 == 12) and (peg3 == 4 or peg3 == 13):
            moveValid = True

    elif peg1 == 12:
        if peg2 == 11 or peg2 == 7 or peg2 == 8 or peg2 == 13:
            if peg3 == 10 or peg3 == 3 or peg3 == 5 or peg3 == 14:
                moveValid = True

    elif peg1 == 13:
        if (peg2 == 12 or peg2 == 8) and (peg3 == 11 or peg3 == 4):
            moveValid = True

    elif peg1 == 14:
        if (peg2 == 13 or peg2 == 9) and (peg3 == 12 or peg3 == 5):
            moveValid = True

    else:
        moveValid = False

    # if move valid and peg locations are valid
    if moveValid and pegList[peg1] and pegList[peg2] and not pegList[peg3]:
        valid = True

    # return if move was valid and can be completed
    return valid


# -----------------------------------------------


def doMove(peg1, peg2, peg3, pegs, screen):
    """
    Function Description:
    here

    :param peg1:
    :param peg2:
    :param peg3:
    :param pegs:
    :param screen:
    :return:
    """

    # set empty peg locations
    pegs[peg1] = False
    pegs[peg2] = False
    pegs[peg3] = True

    pegs = displayFunctions.setBoard(pegs, screen)

    return pegs


# -----------------------------------------------


def anyMoves(pegs):
    """
    Function Description:
    here

    :param pegs:
    :return:
    """

    possibleMove = True

    # check move against possible moves
    switcher = {
        # all possible valid moves starting at peg hole 0 to 14
        0: [[0, 1, 3], [0, 2, 5]],
        1: [[1, 3, 6], [1, 4, 8]],
        2: [[2, 4, 7], [2, 5, 9]],
        3: [[3, 1, 0], [3, 4, 5], [3, 7, 12], [3, 6, 10]],
        4: [[4, 7, 11], [4, 8, 13]],
        5: [[5, 2, 0], [5, 4, 3], [5, 8, 12], [5, 9, 14]],
        6: [[6, 3, 1], [6, 7, 8]],
        7: [[7, 8, 9], [7, 4, 2]],
        8: [[8, 4, 1], [8, 7, 6]],
        9: [[9, 5, 2], [9, 8, 7]],
        10: [[10, 6, 3], [10, 11, 12]],
        11: [[11, 7, 4], [11, 12, 13]],
        12: [[12, 11, 10], [12, 7, 3], [12, 8, 5], [12, 13, 14]],
        13: [[13, 12, 11], [13, 8, 4]],
        14: [[14, 13, 12], [14, 9, 5]]
    }
    # get moves starting at the first peg selected
    possibleMoves = switcher.get(pegs[0])

    print(possibleMoves)

    for i in range(15):

        if pegs[i]:
            currentMoves = switcher.get(i)

    """
    testy = [[1, 2, 3], [7, 8, 9]]
    testTime = testy[0]
    print(testTime[1])
    # prints 2
    """

    return possibleMove
