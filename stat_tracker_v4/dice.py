import random

class Dice():
    def __init__(self, sides):
        self.text = f'D{sides}'
        self.number = sides
        
    def roll(self):
        min = 1
        max = self.number
        rolled_dice = random.randint(min, max)
        
        return rolled_dice