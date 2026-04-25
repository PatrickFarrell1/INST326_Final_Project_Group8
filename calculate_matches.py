def calculate_matches(self):

    """
    Calculates how many matches are present in a given roll, and then applies 
    multiplier rule based on which color/value matches are present.

    Returns: the user's score followed by number of matches which will be referenced
    later for even/odd rule

    Author: Patrick Farrell
    
    """
    score = 0
    match_count = 0

    dictionary = {}

    for die in self.dice:
        if die[1] not in dictionary:
            dictionary[die[1]] = []

        dictionary[die[1]].append(die[0])

    for item in dictionary:
        colors = dictionary[item]

        if len(colors) >= 2:
            match_count += len(colors)

            if colors[0] == colors[1]:
                score += item * 10
            elif colors[0] != colors[1]:
                score += item * 2

    return score, match_count