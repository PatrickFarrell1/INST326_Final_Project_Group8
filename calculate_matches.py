def calculate_matches(self):

    """
    Calculates how many matches are present in a given roll, and then applies 
    the multiplier rules based on which color/value matches are present.

    Returns: the user's score followed by number of matches and whether they 
    rolled an even amount of matches, odd, or got blistered.

    Author: Patrick Farrell
    
    """

    score = 0
    match_count = 0
    dictionary = {}

    for die in self.dice:
        if die[1] not in dictionary:
            dictionary[die[1]] = []
        dictionary[die[1]].append(die[0])
        
    if 6 in dictionary and len(dictionary[6]) == 6:
        return 0, 6, "game over"

    for value in dictionary:
        colors = dictionary[value]

        if len(colors) >= 2:
            match_count += len(colors)

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
            if (matching_color and remaining_count > 0):
                score += remaining_count * value
            elif not matching_color:
                score += value * len(colors)

    if match_count == 0:
        outcome = "blistered"
    elif match_count % 2 == 0:
        outcome = "even"
    elif match_count % 2 != 0:
        outcome = "odd"

    return score, match_count, outcome