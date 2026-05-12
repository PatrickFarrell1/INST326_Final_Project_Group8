import random

class DiceSet:
    '''
    The game always contains:
    - 2 red dice
    - 2 blue dice
    - 2 white dice

    Each die has:
    - a color (red, blue, white)
    - a value between 1-6
    
    Author: Rachel Galloway
    
    '''

    def __init__(self, num_dice=6):
        '''
        Parameters:
        num_dice (int): total number of dice in a set
        '''

        self.num_dice = num_dice
        self.colors = ["red", "blue", "white"]
        self.dice = []  # stores tuples of (color, value)

    def roll_all(self):
        '''
        Roll all 6 dice at the beginning of the turn

        Returns:
        list: list of tuples containing (color, value)
        '''

        self.dice = []

        # exactly 2 of each color
        color_pool = [
            "red", "red",
            "blue", "blue",
            "white", "white"
        ]

        # randomize the order
        random.shuffle(color_pool)

        # assign random values
        for color in color_pool:
            value = random.randint(1, 6)
            self.dice.append((color, value))

        return self.dice

    def roll_remaining(self, num_dice):
        '''
        Roll the remaining dice after the first turn

        Parameters:
        num_dice (int): number of dice to reroll

        Returns:
        list: updated list of rerolled dice
        '''

        new_dice = []

        # maintain 2 of each color
        color_pool = [
            "red", "red",
            "blue", "blue",
            "white", "white"
        ]

        # randomize colors
        random.shuffle(color_pool)

        # reroll only requested number of dice
        for i in range(num_dice):
            color = color_pool[i]
            value = random.randint(1, 6)

            new_dice.append((color, value))

        self.dice = new_dice

        return self.dice

    def display(self):
        '''
        Display the current dice with colored output
        '''

        # ANSI color codes
        color_codes = {
            "red": "\033[31m",
            "blue": "\033[34m",
            "white": "\033[37m"
        }

        reset = "\033[0m"

        print("Current Dice:")

        for color, value in self.dice:

            code = color_codes[color]

            print(
                f"{code}[{color.upper()} DIE] "
                f"rolled a {value}{reset}"
            )

    def get_values(self):
        '''
        Return the dice values

        Returns:
        list: list of tuples containing (color, value)
        '''

        return self.dice


# PLAYER TURN

player_dice = DiceSet()

player_dice.roll_all()

print("PLAYER ROLLED:")

player_dice.display()