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
    searchBFS(pegs)
    
    searchDFS(pegs)
    
    findMove(pegs)
"""


# -----------------------------------------------
# -----------------------------------------------


def searchBFS(pegs):

    """
    Function Description:
    This function recursively applies a modified Breadth First Search algorithm to solve the Peg Game.

    :param pegs: array of true or false values corresponding to locations of pegs - true or empty peg holes - false
    :return: this function has no returns but does print outputs
    """

    # find the possible moves for the current peg locations
    moves = findMoves(pegs)
    print(moves)

    # make a copy of the pegs variable to be used later while not changing the value of pegs
    pegsCopy = pegs

    # create an empty list of lists to hold the pegs arrays of the moves that can be done
    pegsList = [[], [], [], []]

    # if there are possible moves for the board state
    if moves:

        # for each move possible
        for i in range(len(moves)):

            # get the current move being completed
            currentMove = moves[i]
            print(currentMove)

            # update a copy of the pegs array with the currentMove completed
            pegsCopy[currentMove[0]] = False
            pegsCopy[currentMove[1]] = False
            pegsCopy[currentMove[2]] = True

            # add this copy of the pegs array to the list of copies
            pegsList[i] = pegsCopy

        # print for spacing
        print()

        # recursively search starting from the board states of each completed move
        searchBFS(pegsList[0])
        searchBFS(pegsList[1])
        searchBFS(pegsList[2])
        searchBFS(pegsList[3])

    # if there are no possible moves
    else:

        # print to indicate the search of this branch is done
        print('done')

        # print the fitness of this branch of the search based on how many pegs are left on the board
        print('fitness =', sum(pegs))

    return


# -----------------------------------------------


def searchDFS(pegs):
    """
    Function Description:
    This function recursively applies a modified Depth First Search algorithm to solve the Peg Game.

    :param pegs: array of true or false values corresponding to locations of pegs - true or empty peg holes - false
    :return: this function has no returns but does print outputs
    """

    # find possible moves based on the board state
    moves = findMoves(pegs)
    print(moves)

    # if there are any possible moves for the board state
    if gameFunctions.anyMoves(pegs):

        # for each move
        for i in range(len(moves)):

            # set the current move being dealt with
            currentMove = moves[i]
            print(currentMove)

            # update the pegs to reflect this move
            pegs[currentMove[0]] = False
            pegs[currentMove[1]] = False
            pegs[currentMove[2]] = True

            # recursively search based on the board state of the move that was just completed
            searchDFS(pegs)

    # if no moves are possible
    else:

        # print to indicate the end of the branch
        print('done')

        # print the fitness of this branch based on how many pegs are left of the board
        print('fitness =', sum(pegs))

    return


# -----------------------------------------------


def findMoves(pegs):

    """
    Function Description:
    This function finds all moves that are possible based on the current board state.

    :param pegs: array of true or false values corresponding to locations of pegs - true or empty peg holes - false
    :return moves: return the list of possible moves based on the board state
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
