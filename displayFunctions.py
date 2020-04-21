import pygame

# -----------------------------------------------
# -----------------------------------------------

"""
Justin Andrews
Spring 2020
CS455 - Artificial Intelligence
Peg Game - Final Project

File Description:
This file contains functions needed to display the game.

Function Declarations:
    board(screen)
    
    placeHolder(screen, x, y)
    
    placePeg(screen, x, y)
    
    setBoard(pegs, screen)
"""

# -----------------------------------------------
# -----------------------------------------------
# DISPLAY VARIABLES


# load image to be used for the board
boardImage = pygame.image.load('images/pegBoard.png')

# set board x location
boardX = 200

# set board y location
boardY = 100

# load peg and peg place holder images
pegImage = pygame.image.load('images/redPeg.png')
holderImage = pygame.image.load('images/blackCircle.png')

# centers of peg holes for reference
pegHoleCenterX = [501, 446, 555, 388, 502, 614, 330, 445, 552, 673, 275, 386, 500, 609, 733]
pegHoleCenterY = [186, 277, 275, 372, 375, 373, 469, 469, 469, 468, 565, 565, 565, 565, 565]

# where to actually place pegs and peg place holders
pegHoleX = [x - 17.5 for x in pegHoleCenterX]
pegHoleY = [y - 17.5 for y in pegHoleCenterY]


# -----------------------------------------------
# -----------------------------------------------


def board(screen):

    """
    Function Description:
    here

    :param screen:
    :return:
    """

    # place board at x,y
    screen.blit(boardImage, (boardX, boardY))


# -----------------------------------------------


def placeHolder(screen, x, y):

    """
    Function Description:
    here

    :param screen:
    :param x:
    :param y:
    :return:
    """

    # place empty hole at x,y
    screen.blit(holderImage, (x, y))


# -----------------------------------------------


def placePeg(screen, x, y):

    """
    Function Description:
    here

    :param screen:
    :param x:
    :param y:
    :return:
    """

    # place peg on screen at x,y
    screen.blit(pegImage, (x, y))


# -----------------------------------------------


# create starting board positions
# this function takes emptyLoc which is the location of the peg hole that will start empty
# peg hole numbering starts at 0 and goes to 14 from top to bottom, left to right (see attached reference image)
def setBoard(pegs, screen):

    """
    Function Description:
    here

    :param pegs:
    :param screen:
    :return:
    """

    # arrange True and False to correspond with correct peg locations
    for i in range(len(pegs)):

        # if peg not in hole
        if not pegs[i]:
            placeHolder(screen, pegHoleX[i], pegHoleY[i])

        # if peg in hole
        else:
            placePeg(screen, pegHoleX[i], pegHoleY[i])

    return pegs
