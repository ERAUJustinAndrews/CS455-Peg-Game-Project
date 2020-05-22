# CS455 Peg Game Project by Justin Andrews
Introduction:
 This is my final project for CS455. For this project I created a Peg Game solver using search algorithms.
 This game can be played by the user or the game can be played with search algorithms solving the game.
 
How to Play:
 The Peg Game is played by completing jumps with the pegs like in the game "Checkers" and removing pegs that are jumped from the board.
 Pegs can only jump linearly and over pegs directly beside the starting peg.
 The game is over when no more jumps or moves can be made.
 The goal of the game is to leave as few pegs standing at the end of game.
 Peg holes are numbered from 0 to 14, starting at the top and then going row by row down and left to right.
 See attached "pegBoard_grid_references" in the "images" folder as it illustrates the numbering schema of the board.

File Setup:
 To run this game PegGame.py, searchFunctions.py, gameFunctions.py, and displayFunctions.py must all be downloaded and in the same folder.
 In the same folder as these files should be a folder named "images".
 This folder shall contain all images used in the game.
 
To Play the Game:
 To play the game run the PegGame.py file.
 This will create the game screen. From here users can click pegs in the sequence of the move they want to complete.
 The first peg shall be the peg they wish to jump another peg. The second peg shall be the peg they wish to jump.
 The third peg shall be the landing location of the first peg. If 3 pegs are clicked it will create a move which will be checked if it
 is valid or not.
 If the user miss clicks a peg they did not wish to select they can click the text box at the bottom of the screen to clear their clicks.
 The user can then re-do the move sequence they wished to select.
 The user can repeat the process of selecting moves until no more moves are possible and the game ends.
 
To Run the Search Algorithms:
 To run the search algorithms, either the Breadth First Search algorithm or Depth First Search algorithm, run the PegGame.py file.
 To run the Breadth First Search algorithm click the text box in the top left of the screen.
 To run the Depth First Search algorithm click the text box in the top right of the screen.
 After running either algorithm the console will display the moves done and the fitness of all branches of the search algorithm.
 Fitness is based on how many pegs are left standing on the board at the end of the game.
 
 
The Github repository for this project is located at:
 https://github.com/JustinAndrewsCS/CS455-Peg-Game-Project
