class turn_manager:
    
    """
    Turn manager class that includes methods for determining which player's
    turn it is and when the game ends.
    
    Author: Sheila Matumla
    
    """
    def __init__(self, player1, player2, player_index = 0):
        self.players = [player1, player2]
        self.player_index = player_index
        self.game_over = False
    
    def next_turn(self):
        if self.game_over:
            print (f"Game has already ended.")
            
        self.player_index = 1 - self.player_index 
        return self.players[self.player_index]     
    
    def reset_turn(self):
        self.player_index = 0
        print(f"Turn reset to Player 1")
    
    def end_game(self):
        self.game_over = True
        print(f"Game Over")
        
tm = turn_manager("Zoey", "Chloe")
print("Current Turn:", tm.players[tm.player_index])

print("Next Turn:", tm.next_turn())
print("Next Turn:", tm.next_turn())

tm.reset_turn()

print("Current turn upon reset:", tm.players[tm.player_index])

tm.end_game()

tm.next_turn()