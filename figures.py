from config import *
import random

class Figure:
    def __init__(self, team, pos, name, health = 1, selectable = True):
        self.selectable = selectable
        self.alive = True
        self.pos = pos
        self.team = team

        self.name = name
        self.health = health

        self.inventory = []

        if GAMEMODE == "War":
            for i in range(random.randint(1, 5)):
                rand_item = random.choice(AVIABLE_ITEMS)
                self.inventory.append(rand_item)



       


class Pawn(Figure):
    def __init__(self, team, pos, name,  health = 1):
        super().__init__(team, pos, name,  health)
        

        if team == "White":
            self.icon = ["  _  ", " (@) ", " d@b "]
        elif team == "Black":
            self.icon = ["  _  ", " ( ) ", " /_\\ "]
        else:
            self.icon = "E"

    def moves(self, game):
        pos_x = self.pos[0]
        pos_y = self.pos[1]

        possible_moves = []

        if self.team == "White" and pos_x + 1 < SIZE_Y:
            if game.board[pos_x+1][pos_y] == None:
                possible_moves.append([pos_x+1, pos_y])
            if game.board[pos_x+1][pos_y+1] != None:
                if game.board[pos_x+1][pos_y+1].team == "Black":
                    possible_moves.append([pos_x+1, pos_y+1])
            if game.board[pos_x+1][pos_y-1] != None:
                if game.board[pos_x+1][pos_y-1].team == "Black":
                    possible_moves.append([pos_x+1, pos_y-1])

        elif self.team == "Black" and pos_x - 1 >= 0:
            if game.board[pos_x-1][pos_y] == None:
                possible_moves.append([pos_x-1, pos_y])
            if game.board[pos_x-1][pos_y+1] != None:
                if game.board[pos_x-1][pos_y+1].team == "White":
                    possible_moves.append([pos_x-1, pos_y+1])
            if game.board[pos_x-1][pos_y-1] != None:
                if game.board[pos_x-1][pos_y-1].team == "White":
                    possible_moves.append([pos_x-1, pos_y-1])


        return possible_moves



class Rook(Figure):
    def __init__(self, team, pos, name,  health =1):
        super().__init__(team, pos, name,  health)
        if team == "White":
            self.icon = ["@___@", " @@@ ", "d@@@b"]
        elif team == "Black":
            self.icon = ["[___]", " [ ] ", "/___\\"]
        else:
            self.icon = "E"

    def moves(self, game):
        pass


class Knight(Figure):
    def __init__(self, team, pos, name,  health = 1):
        super().__init__(team, pos, name,  health)
        if team == "White":
            self.icon = [" %~b ", "`'dX ", " d@@b"]
        elif team == "Black":
            self.icon = [" %~\\ ", "`')( ", " <__>"]
        else :
            self.icon = "E"

    
    def moves(self, game):
        pass

class Bishop(Figure):
    def __init__(self, team, pos, name,  health = 1):
        super().__init__(team, pos, name,  health)
        if team == "White":
            self.icon = [" .@. ", " @@@ ", "./A\\."]
        elif team == "Black":
            self.icon = [" .O. ", " \\ / ", " /_\\ "]
        else:
            self.icon = "E"


    def moves(self, game):
        pass

class Queen(Figure):
    def __init__(self, team, pos, name,  health = 1):
        super().__init__(team, pos, name,  health)
        if team == "White":
            self.icon = ["\\o*o/", " @@@ ", "d@@@b"]
        elif team == "Black":
            self.icon = ["\\o^o/", " [ ] ", "/___\\"]
        else:
            self.icon = "E"


    def moves(self, game):
        pass

class King(Figure):
    def __init__(self, team, pos, name,  health = 1):
        super().__init__(team, pos, name,  health)
        if team == "White":
            self.icon = ["__+__", "`@@@'", "d@@@b"]
        elif team == "Black":
            self.icon = ["__+__", "`. .'", "/___\\"]
        else:
            self.icon = "E"


    def moves(self, game):
        pass