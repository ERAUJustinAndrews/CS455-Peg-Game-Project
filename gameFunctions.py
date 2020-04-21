import displayFunctions

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
"""

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

    :param peg1:
    :param peg2:
    :param peg3:
    :param pegList:
    :return:
    """

    # the move that wants to be performed
    move = [peg1, peg2, peg3]

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
    possibleMoves = switcher.get(peg1)

    # print valid moves from that starting position
    print('Valid Moves =', possibleMoves)

    # check if move is in valid moves list and peg holes are in valid states
    i = 0
    while i < len(possibleMoves):
        if possibleMoves[i] == move and pegList[peg1] and pegList[peg2] and not pegList[peg3]:
            print('Got One! Move:', i)
            valid = True
        else:
            valid = False
        i = i + 1

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
