class DiceSet:
    
    """
    Dice set class that includes methods for rolling the dice and displaying
    values.
    
    Author: Rachel Galloway
    
    """
    def __init__(self, num_dice=6):
        self.num_dice = num_dice
        self.colors = ["red", "blue", "white"]
        self.dice = [] # stores tuples for color and value
    
    def roll_all(self):
        # rolls all the dice to start the turn
        pass

    def roll_remaining(self, num_dice):
        # rolling the remaining dice after the first turn
        pass

    def display(self):
        # display the players dice values
        pass

    def get_values(self):
        # return the values on the dice
        pass