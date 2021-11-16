Course: CS 107, Fall 2019, Haverford College
Created by: Xiaorong Wang, Mujie Wang, Dylan Soemitro


## Set Card Game ##


## Getting started ##
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites ###
Install pygame package before running the program
Installation can be achieved by using the following code in terminal
$pip3 install pygame

### Run ###
After implementing the pygame package, run the main.py file in the project

### Testing/running the program ###
While entering the program, user will face the introduction screen, where there are two modes that they can choose -- "hard" or "easy". The difference between hard mode and easy mode is that hard mode has 20 cards in each game setting while easy only has 16.
After the starting of the game, the user can find sets in the board. There are 81 cards in total that the user can play. User will finish the game when all 81 cards have been used, which means that the user needs to find at least 26 sets.
While playing the game, user will be able to use the hint only when there are no cards selected. After pressing the "hint" button, the program will automatically select the card that is mostly used in the deck of cards on the screen. User can also choose to exit by the "Quit" button
After finishing all 81 cards, the user will be brought to the ending screen where they can see the time they use for finishing a deck of cards. User can choose to play hard or easy mode again or they can simply quit the game.

### Ending the program ###
User can end the program by pressing the "Quit" buttons.


## Built with ##

### Packages used ###
pygame -- for the user interface and the running of the game
time -- to time the time user uses while playing
random -- to shuffle the 81 cards each time user play

### Authors ###
Xiaorng Wang, Mujie Wang, Dylan Soemitro
