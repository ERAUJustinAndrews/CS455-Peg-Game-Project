import gameFunctions

# -----------------------------------------------
# -----------------------------------------------

"""
Justin Andrews
Spring 2020
CS455 - Artificial Intelligence
Final Project - Peg Game

File Description:
This file contains functions related to the search algorithm.

Function Declarations:
    search(pegs)
    
    findMove(pegs)
"""


# -----------------------------------------------
# -----------------------------------------------


def searchBFS(pegs):

    """
    Function Description:
    here

    :param pegs:
    :return:
    """

    moves = findMoves(pegs)
    print(moves)

    pegsCopy = pegs

    pegsList = [[], [], [], []]

    if moves:

        for i in range(len(moves)):

            currentMove = moves[i]
            print(currentMove)

            pegsCopy[currentMove[0]] = False
            pegsCopy[currentMove[1]] = False
            pegsCopy[currentMove[2]] = True

            pegsList[i] = pegsCopy

        print()

        pegList1 = pegsList[0]
        searchBFS(pegsList[0])
        searchBFS(pegsList[1])
        searchBFS(pegsList[2])
        searchBFS(pegsList[3])

    else:
        print('done')
        print('fitness =', sum(pegs))

    return


# -----------------------------------------------


def searchDFS(pegs):
    """
    Function Description:
    here

    :param pegs:
    :return:
    """

    moves = findMoves(pegs)
    print(moves)

    if gameFunctions.anyMoves(pegs):

        for i in range(len(moves)):

            currentMove = moves[i]
            print(currentMove)

            pegs[currentMove[0]] = False
            pegs[currentMove[1]] = False
            pegs[currentMove[2]] = True

            searchDFS(pegs)

    else:
        print('done')
        print('fitness =', sum(pegs))

    return


# -----------------------------------------------


def findMoves(pegs):

    """
    Function Description:
    here

    :param pegs:
    :return:
    """

    # array to hold possible moves
    moves = []

    # array for empty peg holes
    emptySpots = []

    # go through array of pegs and find which peg holes are empty
    for i in range(len(pegs)):

        # if peg hole is empty
        if not pegs[i]:
            # array of empty positions on the board
            emptySpots.append(i)

    # switcher of all possible moves ordered by the 3rd peg of the move
    switcher = {

        # all possible moves sorted by the peg to be jumped to for the move
        0: [[3, 1, 0], [5, 2, 0]],
        1: [[6, 3, 1], [8, 4, 1]],
        2: [[7, 4, 2], [9, 5, 2]],
        3: [[0, 1, 3], [5, 4, 3], [10, 6, 3], [12, 7, 3]],
        4: [[11, 7, 4], [13, 8, 4]],
        5: [[0, 2, 5], [3, 4, 5], [12, 8, 5], [14, 9, 5]],
        6: [[1, 3, 6], [8, 7, 6]],
        7: [[2, 4, 7], [9, 8, 7]],
        8: [[1, 4, 8], [6, 7, 8]],
        9: [[2, 5, 9], [7, 8, 9]],
        10: [[3, 6, 10], [12, 11, 10]],
        11: [[4, 7, 11], [13, 12, 11]],
        12: [[3, 7, 12], [5, 8, 12], [10, 11, 12], [14, 13, 12]],
        13: [[4, 8, 13], [11, 12, 13]],
        14: [[5, 9, 14], [12, 13, 14]]
    }

    # for each spot on the board missing
    for i in range(len(emptySpots)):

        # get list of moves for current position being checked
        moveList = switcher.get(emptySpots[i])

        # go through list of moves
        for j in range(len(moveList)):

            # get current move being checked from list
            currentMove = moveList[j]

            # check if the move is possible based on current board state
            if pegs[currentMove[0]] and pegs[currentMove[1]] and not pegs[currentMove[2]]:
                # if possible add to moves list
                moves.append(currentMove)

    # return moves list
    return moves
