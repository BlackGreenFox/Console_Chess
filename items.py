from config import *
from figures import *


class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def Use(self, figure):
        pass
        # Realization in others


class Medkit(Item):
    def __init__(self, name, description, health):
        super().__init__(name, description)
        self.health = health

    def Use(self, figure, target = None):
        if target == None:
            figure.health += self.health
        else:
            target.health += self.health


class BuildKit(Item):
    def __init__(self, name, description):
        super().__init__(name, description)

    def Use(self, game, pos = None):

        x = game.selected_figure.pos[0]
        y = game.selected_figure.pos[1]
    
        target_x = ord(pos[0].upper()) - ord('A')
        target_y = SIZE_Y - int(pos[1])
 
        if pos == None:    
            if game.board[x+1][y] == None and game.selected_figure.team == "White":
               game.board[x+1][y] = Baricade("Build", (x+1, y), "Wall",4)
            elif game.board[x-1][y] == None and game.selected_figure.team == "Black":
               game.board[x-1][y] = Baricade("Build", (x-1, y), "Wall",4)
        else:
            if game.board[target_x][target_y] == None:
               game.board[target_x][target_y] = Baricade("Build", (target_x, target_y), "Wall",4)
        return 
        
        

