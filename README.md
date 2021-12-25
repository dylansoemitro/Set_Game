
# Set Card Game #

Fall 2019

Created by: Xiaorong Wang, Mujie Wang, Dylan Soemitro

## Background:
We decided to make an implementation of SET, American's most popular card game, in Python. Each deck contains 81 unique cards, shown below.
![Alt text](/Card_Images/set-game-cards.png?raw=true "Set Cards")

Each card has four features: number, color, shape and shade. A set of cards is a group of three cards such that, within each feature, they either are
all different or all the same. In our implementation, the game starts with a cardboard
of 16 or 20 random cards from the deck, depending on whether the player chooses
the easy or hard mode (easy = 20 cards, hard = 16 cards). The player then is able to
select three cards. The program will verify if the three cards make a set. If so, the
program will replace the old cards with three random new cards that have not been
used yet. If there is no set on the board, the program will automatically fill in 3 cards,
until there is a set on the board. When stuck, the player can click on the “hint” button. The
program will highlight one card that appears in the most amount of sets on the board.

The rules of SET are linked here: https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20ENGLISH.pdf


## Methodology:
### Finding the third card:
Recall that in order to be a set, three cards, for each feature, need to be all
the same or all different. “All the same” is easier to implement, while “all different” is
a bit trickier. We took advantage of the cycle structure of Z mod 4 and modified it a
little bit. First, we label the choices of each feature with integers 1, 2, 3. Observe that
if we add two together, it will give the third number or 0, which we redirected it to 2.
The structure of this game is a graph, as shown in Figure 2. Each card is a
node. There is an edge connecting each pair of nodes. And each edge can be
represented as the third card.
![Alt text](/Card_Images/GraphCard.PNG?raw=true "Graph Cards")
### Encoding a 4-tuple into an integer:
Since each card has four features and each feature has 3 choices, we label
each card uniquely with a 4-tuple with entries 1, 2, or 3. For the fairness and fun of
the game, we want the cards shuffled, but it is harder to shuffle tuples than to shuffle
integers. So, we use the idea of ternary to encode the tuple into an integer in
decimal. So if we have a tuple (a, b, c, d), we first delete 1 from each entry and turn it
into (a*, b*, c*, d*), and the corresponding integer will be a* x 3^3 + b* x 3^2 + c* x 3 + d*. We can also reverse the procedure to convert an integer from 0 to 80 uniquely
to a card.
### Using a stack to stored shuffled cards:
After a deck is shuffled (81 random integers without replacement), we put the
shuffled cards into a stack and pop the first one when needed.

## Future Improvements:
### Score Calculation:
We could determine some sort of score using various factors, include the
number of hints used, time taken etc. 

### High Score:
We can save the user’s last score and
high score for reference.

### Two-Player Mode:
We can make a two-player mode where
two players need to claim “set” before
they choose cards, and see which
player finds more sets. This mode can
be offline or online.

## Getting started: ##
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites: ###
Install pygame package before running the program

Installation can be achieved by using the following code in terminal

$pip3 install pygame

### Run: ###
After implementing the pygame package, run the main.py file in the project

### Testing/running the program: ###
While entering the program, user will face the introduction screen, where there are two modes that they can choose -- "hard" or "easy". The difference between hard mode and easy mode is that hard mode has 20 cards in each game setting while easy only has 16.

After the starting of the game, the user can find sets in the board. There are 81 cards in total that the user can play. User will finish the game when all 81 cards have been used, which means that the user needs to find at least 26 sets.

While playing the game, user will be able to use the hint only when there are no cards selected. After pressing the "hint" button, the program will automatically select the card that is mostly used in the deck of cards on the screen. User can also choose to exit by the "Quit" button.

After finishing all 81 cards, the user will be brought to the ending screen where they can see the time they use for finishing a deck of cards. User can choose to play hard or easy mode again or they can simply quit the game.

### Ending the program: ###
User can end the program by pressing the "Quit" buttons.

### Packages used: ###
#### pygame 
Used mainly to create the user interface of the game. It is the base of
all other implementations

#### time
To time the time user uses while playing

#### random
The random package is used to shuffle the stack of 81 cards each time
the program starts. This is to make sure each time when the user
plays the game, the cardboard given is completely random and will
change in different games.


### Authors: ###
Xiaorong Wang, Mujie Wang, Dylan Soemitro
