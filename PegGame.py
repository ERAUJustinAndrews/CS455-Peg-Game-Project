import sys
import pygame

# -----------------------------------------------

# Justin Andrews
# Spring 2020
# CS455 - Artificial Intelligence
# Peg Game - Final Project
# This is based off of the Peg Game made famous by Cracker Barrel restaurants.
# This project plays the game using multiple search algorithms.

# -----------------------------------------------
# CREATE VARIABLES

# initialize pygame
pygame.init()
print()

# create the screen
screen = pygame.display.set_mode((1000, 800))

# give the pygame window a title
pygame.display.set_caption("Peg Game")

# create board
boardImage = pygame.image.load('images/pegBoard.png')
boardX = 200
boardY = 100

# load peg and peg place holder images
pegImage = pygame.image.load('images/redPeg.png')
holderImage = pygame.image.load('images/blackCircle.png')

# create arrays of peg hole locations
# centers of peg holes
pegHoleCenterX = [501, 446, 555, 388, 502, 614, 330, 445, 552, 673, 275, 386, 500, 609, 733]
pegHoleCenterY = [186, 277, 275, 372, 375, 373, 469, 469, 469, 468, 565, 565, 565, 565, 565]
# where to place pegs and peg place holders
pegHoleX = [x - 17.5 for x in pegHoleCenterX]
pegHoleY = [y - 17.5 for y in pegHoleCenterY]

# create arrays that hold true and false values for holes that have pegs and holes that have no pegs
pegs = []


# -----------------------------------------------
# FUNCTION DEFINITIONS


# define board to be drawn
def board():
    screen.blit(boardImage, (boardX, boardY))


# place black peg place holder at x and y coordinates
def placeHolder(x, y):
    screen.blit(holderImage, (x, y))


# place peg at x and y coordinates
def placePeg(x, y):
    screen.blit(pegImage, (x, y))


# create starting board positions
# this function takes emptyLoc which is the location of the peg hole that will start empty
# peg hole numbering starts at 0 and goes to 14 from top to bottom, left to right (see attached reference image)
def setBoard(emptyLoc):
    pegsArray = [False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                 False]

    # if invalid emptyLoc throw error
    if min(emptyLoc) < 0 or max(emptyLoc) > 15:
        print("Something is wrong.")
        print("Please enter a location for startingBoard() between 1 and 15!")
        print("See attached reference image for clarification.")
        print("Exiting...")
        sys.exit(1)

    # if valid location then continue
    else:
        i = 0
        while i < 15:

            # if it is the position that needs to be empty
            if i in emptyLoc:
                placeHolder(pegHoleX[i], pegHoleY[i])
                pegsArray[i] = False
            else:
                placePeg(pegHoleX[i], pegHoleY[i])
                pegsArray[i] = True
            i = i + 1

    return pegsArray


# check what peg was clicked and if the click was valid, return if valid and what peg
def checkClick(clickX, clickY):

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


# check if move was valid
def checkMove(peg1, peg2, peg3, pegList):

    moveValid = False
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
        7: [7, 8, 9],
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

    # check if move is in valid moves list
    i = 0
    while i < len(possibleMoves):
        if possibleMoves[i] == move:
            print('Got One! Move:', i)
            moveValid = True
        else:
            moveValid = False
        i = i + 1

    # check if holes are correctly empty or filled
    if pegList[peg1] and pegList[peg2] and not pegList[peg3]:
        holesValid = True
    else:
        holesValid = False

    # check if the move is valid and the holes are open
    if moveValid and holesValid:
        valid = True
    else:
        valid = False

    # return if move was valid and can be completed
    return valid


# complete the move, set peg locations, set board
def doMove(peg1, peg2, peg3, oldPegs):
    newPegs = []

    return newPegs


# -----------------------------------------------
# GAME LOOP

# set location that will start empty, 0 to 14
emptyLocations = [5]

# clicked pegs
clicks = []

# loop to run game
running = True
print("Game is running!\n")
while running:

    # change background color to sky blue
    screen.fill((45, 130, 155))

    # draw board
    board()

    # set board
    pegs = setBoard(emptyLocations)

    # check user events
    for event in pygame.event.get():

        # check if user quits
        if event.type == pygame.QUIT:
            print("\nGame is quitting...")
            running = False

        # check if user clicks pegs
        elif event.type == pygame.MOUSEBUTTONDOWN:
            clickPosX, clickPosY = pygame.mouse.get_pos()
            pegValid, pegClicked = checkClick(clickPosX, clickPosY)
            if pegValid:
                print(pegClicked)
                clicks.append(pegClicked)
                print(clicks)

                # check if the user has clicked 3 pegs for a move
                if len(clicks) == 3:
                    # check if the move is valid
                    # validMove = True
                    validMove = checkMove(clicks[0], clicks[1], clicks[2], pegs)
                    if validMove:
                        print("\nValid Move!\n")
                        doMove(clicks[0], clicks[1], clicks[2], pegs)
                        clicks.clear()
                    else:
                        print("\nInvalid Move.\n")
                        clicks.clear()

    """
    # check if the pegs chosen result in a valid move
    validMove = checkMove(pegClicked1, pegClicked2, pegClicked3)

    # if move is valid then create new list of empty peg holes
    if validMove:
        pegs[pegClicked1] = False
        pegs[pegClicked2] = False
        pegs[pegClicked3] = True
        for i in pegs:
            if not pegs[i]:
                emptyLocations.append(i)
    """

    # update screen
    pygame.display.update()
