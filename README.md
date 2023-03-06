# Text Adventure
## Background
This project is a text adventure game that is ran via the command line and built using OOP. There are two classes to choose from (soldier and mage) and a variety of enemies. The game carries on running until the player dies.

## Set Up
1. Cloning

First, clone this repository in the directory that you would like to store this project by running:

`git clone git@github.com:BBarkworth/text_adventure.git`

2. Install dependencies

Install the following library using the command below:

`pip install art`

3. Run the program

Run the program by entering `python main.py` in the command line within the project directory.

## Classes
There are two playable classes that each have two attack methods to choose from, as well as a number of other methods that include returning relevant information, applying damage from enemies and levelling up.

The enemy classes are built on similar principles with each having at least one type of attack and some of the attacks are based on certain conditional checks being met.

## Python Functions
The helpers file consists of various functions that are used in the main file. These include:
- `player_choice`: provides an input for the player to choose their class and creates the necessary object
- `enemy_spawn`: creates enemies for the start of a level. The first parameter dictates how many enemies are created each time the function is called and the random selection is weighted to provide the right mix of enemies
- `dice_roll`: a simple function to simulate a dice roll that can be passed in as an argument for a variety of methods

## Minimum Version Requirements
- Python 3.9