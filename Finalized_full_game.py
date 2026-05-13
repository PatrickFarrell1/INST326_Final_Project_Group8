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
        self.num_dice = num_dice
        self.colors = ["red", "blue", "white"]
        self.dice = []

    def roll_all(self):
        self.dice = []

        color_pool = [
            "red", "red",
            "blue", "blue",
            "white", "white"
        ]

        random.shuffle(color_pool)

        for color in color_pool:
            value = random.randint(1, 6)
            self.dice.append((color, value))

        return self.dice

    def roll_specific_colors(self, colors):
        self.dice = []

        for color in colors:
            value = random.randint(1, 6)
            self.dice.append((color, value))

        return self.dice

    def display_die(self, color, value):
        color_codes = {
            "red": "\033[31m",
            "blue": "\033[34m",
            "white": "\033[37m"
        }

        reset = "\033[0m"
        code = color_codes[color]

        print(f"{code}[{color.upper()} DIE] value: {value}{reset}")

    def display(self):
        color_codes = {
            "red": "\033[31m",
            "blue": "\033[34m",
            "white": "\033[37m"
        }

        reset = "\033[0m"

        print("Current Dice:")

        for color, value in self.dice:
            code = color_codes[color]
            print(f"{code}[{color.upper()} DIE] rolled a {value}{reset}")

    def get_values(self):
        return self.dice



class GameConditions:
    
    """
    Game conditions class with methods for calculating scores, even/odd rule,
    blistering and sixes rule.
    
    Author: Terry Thompson
    
    """

    def __init__(self, current_dice, set_aside_dice):
        self.current_dice = current_dice
        self.set_aside_dice = set_aside_dice

    def score_group(self, value, colors):
        score = 0
        color_counts = {}

        for color in colors:
            if color not in color_counts:
                color_counts[color] = 0

            color_counts[color] += 1

        matching_color = False

        for color in color_counts:
            if color_counts[color] >= 2:
                score += value * 10
                color_counts[color] -= 2
                matching_color = True

        remaining_count = 0

        for color in color_counts:
            remaining_count += color_counts[color]

        if matching_color and remaining_count > 0:
            score += remaining_count * value

        elif not matching_color:
            score += value * len(colors)

        return score

    def calculate_matches(self):
        
        """
        Calculates how many matches are present in a given roll, and then applies 
        the multiplier rules based on which color/value matches are present.

        Returns: the user's score followed by number of matches and whether they 
        rolled an even amount of matches, odd, or got blistered.

        Author: Patrick Farrell
        
        """
        all_dice = self.set_aside_dice + self.current_dice

        dictionary = {}

        for die in all_dice:
            color = die[0]
            value = die[1]

            if value not in dictionary:
                dictionary[value] = []

            dictionary[value].append(color)

        if len(all_dice) == 6:
            six_count = 0

            for die in all_dice:
                if die[1] == 6:
                    six_count += 1

            if six_count == 6:
                return 0, 6, "game over", [], self.current_dice

        matching_values = []

        for value in dictionary:
            if len(dictionary[value]) >= 2:
                matching_values.append(value)

        newly_matched = []
        remaining_dice = []

        for die in self.current_dice:
            if die[1] in matching_values:
                newly_matched.append(die)
            else:
                remaining_dice.append(die)

        if len(newly_matched) == 0:
            total_scoring_dice = len(self.set_aside_dice)
            return 0, total_scoring_dice, "blistered", newly_matched, remaining_dice

        score = 0

        for value in matching_values:
            old_colors = []
            new_colors = []

            for die in self.set_aside_dice:
                if die[1] == value:
                    old_colors.append(die[0])

            for die in all_dice:
                if die[1] == value:
                    new_colors.append(die[0])

            old_score = 0

            if len(old_colors) >= 2:
                old_score = self.score_group(value, old_colors)

            new_score = self.score_group(value, new_colors)

            score += new_score - old_score

        total_scoring_dice = len(self.set_aside_dice) + len(newly_matched)

        if total_scoring_dice % 2 == 0:
            outcome = "even"
        else:
            outcome = "odd"

        return score, total_scoring_dice, outcome, newly_matched, remaining_dice

    def check_even_odd(self):
        return self.calculate_matches()[2]

    def check_blister(self):
        return self.calculate_matches()[2] == "blistered"

    def check_all_sixes(self):
        return self.calculate_matches()[2] == "game over"



class turn_manager:
    
    """
    Turn manager class that includes methods for determining which player's
    turn it is and when the game ends.
    
    Author: Sheila Matumla
    
    """

    def __init__(self, player1, player2, player_index=0):
        self.players = [player1, player2]
        self.player_index = player_index
        self.game_over = False

    def next_turn(self):
        if self.game_over:
            print("Game has already ended.")
            return None

        self.player_index = 1 - self.player_index
        return self.players[self.player_index]

    def reset_turn(self):
        self.player_index = 0
        print("Turn reset to Player 1")

    def end_game(self):
        self.game_over = True
        print("Game Over")


def play_game():
    
    """
    Final function to execute full playable game.
    
    Author: Everyone
    
    """

    player1 = input("Enter Player 1 name: ")
    player2 = input("Enter Player 2 name: ")
    winning_score = int(input("Set a winning score: "))

    scores = {
        player1: 0,
        player2: 0
    }

    manager = turn_manager(player1, player2)

    print("\nWelcome to Blisters!")
    print("First player to reach", winning_score, "points wins.")

    while not manager.game_over:
        current_player = manager.players[manager.player_index]

        print("\n")
        print(current_player + "'s turn")
        print("\n")
        
        dice_set = DiceSet()
        current_dice = dice_set.roll_all()

        dice_set_aside = []
        turn_score = 0
        continue_turn = True

        while continue_turn and not manager.game_over:
            dice_set.dice = current_dice
            dice_set.display()

            if len(dice_set_aside) > 0:
                print("\nDice that were set aside from previous roll (matches):")

                for color, value in dice_set_aside:
                    dice_set.display_die(color, value)

            conditions = GameConditions(current_dice, dice_set_aside)

            score, match_count, outcome, newly_matched, remaining_dice = conditions.calculate_matches()

            print("\nTurn score total:", turn_score + score)
            print("Total matches this turn:", match_count)

            if outcome == "game over":
                print(current_player, "rolled six sixes.")
                print("Automatic game over!")
                manager.end_game()
                break
            elif outcome == "blistered":
                print("You got blistered, 0 points this turn.")
                turn_score = 0
                continue_turn = False
            else:
                turn_score += score

                for die in newly_matched:
                    dice_set_aside.append(die)

                current_dice = remaining_dice

                if len(current_dice) == 0:
                    print("All dice have been matched. Turn ends.")
                    continue_turn = False

                elif outcome == "odd":
                    print("Odd number of total matches. You must roll the remaining", len(current_dice), "dice.")

                    input("Press Enter to roll again:")
                    print()

                    colors_to_roll = []

                    for die in current_dice:
                        colors_to_roll.append(die[0])

                    current_dice = dice_set.roll_specific_colors(colors_to_roll)

                elif outcome == "even":
                    choice = input("Even number of total matches. Would you like to roll the remaining dice? (y/n): ")

                    if choice.lower() == "y":
                        print()

                        colors_to_roll = []

                        for die in current_dice:
                            colors_to_roll.append(die[0])

                        current_dice = dice_set.roll_specific_colors(colors_to_roll)

                    else:
                        print("Turn ended.")
                        continue_turn = False

        scores[current_player] += turn_score

        print("\n" + current_player + " earned",
              str(turn_score), "points this turn.")

        print("\nCurrent Scores:")
        print(player1 + ":", scores[player1])
        print(player2 + ":", scores[player2])

        if scores[current_player] >= winning_score:
            print("\n" + current_player + " wins the game!")
            manager.end_game()

        else:
            choice = input("\nContinue to next turn? (y/n): ")

            if choice.lower() == "y":
                manager.next_turn()
            else:
                print("Game stopped.")
                manager.end_game()



if __name__ == "__main__":
    play_game()