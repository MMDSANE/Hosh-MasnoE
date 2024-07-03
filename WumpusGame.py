import random

class WumpusGame :     
    def __init__(self, size): 
        self.size = size 
        self.player_position= (0 ,0)          
        self.wumpus_position = self.generate_random_position() 
        self.gold_position = self.generate_random_position()        
        self.pit_positions = [self.generate_random_position() for _ in range(3)]
         
 
    def generate_random_position(self) : 
        return random.randint(0, self.size - 1), random.randint(0, self.size - 1) 
    
    def check_encounter(self, position): 
        if position == self.wumpus_position: 
            return "You encountered the Wumpus! Game Over " 
        elif position == self.gold_position : 
            return "You found the gold! You win "
        elif position in self.pit_positions :             
            return "You fell into a pit! Game Over "         
        else:             
             return "You're safe" 
 
    def move(self, direction):         
        x, y = self.player_position         
        if direction == "up" and y < self.size - 1 : 
            y += 1         
        elif direction == "down" and y > 0:             
            y -= 1         
        elif direction == "right" and x < self.size - 1 : 
            x += 1 
        elif direction == "left" and x > 0: 
            x -= 1 
 
        self.player_position = (x, y)         
        return self.check_encounter(self.player_position) 
 
 # مثال استفاده از کد:
game = WumpusGame(4) 
print("Welcome to Wumpus Game!") 
while True : 
    print(f"Player Position: {game.player_position}") 
    direction = input("Enter your move (up, down, right, left): ")     
    result = game.move(direction)     
    print(result)     
    if "Game Over" in result or "You win" in result: 
        break 
