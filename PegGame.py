import pygame
import time
import displayFunctions
import gameFunctions
import searchFunctions

# -----------------------------------------------
# -----------------------------------------------

"""
Justin Andrews
Spring 2020
CS455 - Artificial Intelligence
Final Project - Peg Game

File Description:
This is the main file that calls the functions to run the game and search algorithm.

Link to Github repository for this project:
https://github.com/ERAUJustinAndrews/CS455-Peg-Game-Project
"""


# -----------------------------------------------
# -----------------------------------------------
# CREATE VARIABLES


# initialize pygame
pygame.init()
print()

# create the screen for the game to be played on
screen = pygame.display.set_mode((1000, 800))

# give the pygame window a title
pygame.display.set_caption("Peg Game")

# create array that hold true and false values for holes that have pegs and holes that have no pegs
pegs = [True, True, True, True, True, False, True, True, True, True, True, True, True, True, True]


# -----------------------------------------------
# -----------------------------------------------
# GAME LOOP


# clicked pegs
clicks = []

# loop to run game
running = True

print("Game is running!\n")

# while the user has not hit exit
while running:

    # change background color to sky blue
    screen.fill((45, 130, 155))

    # draw board
    displayFunctions.board(screen)

    # set board to the starting position
    pegs = displayFunctions.setBoard(pegs, screen)

    # check user events
    for event in pygame.event.get():

        # check if user quits
        if event.type == pygame.QUIT:

            print("\nGame is quitting...")

            # tell the game to stop running
            running = False

        # check if user clicks the mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:

            # get the coordinate position of the click
            clickPosX, clickPosY = pygame.mouse.get_pos()

            # check if user clicked search algorithm text button
            if 2 < clickPosX < 464 and 10 < clickPosY < 52:

                print("\nRunning BFS search algorithms! ... \n")

                # run BFS
                print("Breadth First Search\n\n")
                searchFunctions.searchBFS(pegs)

                # pause game for user to see
                time.sleep(3)

                # quit game
                running = False

            # check if user clicked dfs search text button
            elif 520 < clickPosX < 994 and 10 < clickPosY < 54:

                print("\nRunning DFS search algorithms! ... \n")

                # run DFS
                print("Depth First Search\n\n")
                searchFunctions.searchDFS(pegs)

                # pause game for user to see
                time.sleep(3)

                # exit game
                running = False

            # check if user clicked to clear clicks
            elif 373 < clickPosX < 629 and 676 < clickPosY < 719:

                # clear list of clicks
                clicks.clear()

                print("\nCleared list of clicks!\n")

            # check if the user clicked on a peg or valid location
            pegValid, pegClicked = gameFunctions.checkClick(clickPosX, clickPosY)

            # if the click was a valid location
            if pegValid:

                # print the peg that was clicked
                print(pegClicked)

                # add the peg that was clicked to the list of locations clicked that are part of the game move
                clicks.append(pegClicked)

                # print the list of locations picked to form the game move
                print(clicks)

                # check if the user has clicked 3 pegs then a move has been completed
                if len(clicks) == 3:

                    # check if the move is valid based on the game state
                    validMove = gameFunctions.checkMove(clicks[0], clicks[1], clicks[2], pegs)

                    # if the move is valid
                    if validMove:

                        print("\nValid Move!\n")

                        # complete the move, alter the peg states and change the board
                        pegs = gameFunctions.doMove(clicks[0], clicks[1], clicks[2], pegs, screen)

                        # clear the array of clicks, the move has been completed and applied
                        clicks.clear()

                        # check if there are any possible moves
                        if not gameFunctions.anyMoves(pegs):

                            print("No more possible moves.\n")

                            print("GAME OVER")

                            print("...\n")

                            # count how many pegs are left on the board
                            countPegs = 0

                            # check how many pegs are left
                            for i in range(len(pegs)):

                                # if peg is true
                                if pegs[i]:
                                    # increment peg counter
                                    countPegs = countPegs + 1

                            # print how many pegs were left on the board
                            print("You left", countPegs, "pegs on the board!")

                            # pause screen for user to see the final board
                            time.sleep(3)

                            # if no more moves then game is over
                            running = False

                    # if the move is not valid
                    else:

                        print("\nInvalid Move.\n")

                        # clear the array of clicks to begin a new move
                        clicks.clear()

    # update screen
    pygame.display.update()
