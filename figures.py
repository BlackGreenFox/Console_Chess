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
            for _ in range(random.randint(1, 5)):
                rand_item = random.choice(AVIABLE_ITEMS)
                self.inventory.append(rand_item)



class Baricade(Figure):
    def __init__(self, team, pos, name,  health = 1):  
        super().__init__(team, pos, name,  health)  
        
        
        self.icon = ["|ooo|", "|XXX|", "|XXX|"]
          


class Pawn(Figure):
    def __init__(self, team, pos, name,  health = 1):
        super().__init__(team, pos, name,  health)
        self.first_turn = True
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
            if game.board[pos_x+2][pos_y] == None and self.first_turn:
                possible_moves.append([pos_x+2, pos_y])
            if game.board[pos_x+1][pos_y+1] != None:
                if game.board[pos_x+1][pos_y+1].team == "Black":
                    possible_moves.append([pos_x+1, pos_y+1])
            if game.board[pos_x+1][pos_y-1] != None:
                if game.board[pos_x+1][pos_y-1].team == "Black":
                    possible_moves.append([pos_x+1, pos_y-1])

        elif self.team == "Black" and pos_x - 1 >= 0:
            if game.board[pos_x-1][pos_y] == None:
                possible_moves.append([pos_x-1, pos_y])
            if game.board[pos_x-2][pos_y] == None and self.first_turn:
                possible_moves.append([pos_x-2, pos_y])
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
        pos_x = self.pos[0]
        pos_y = self.pos[1]

        possible_moves = []

        for x in range(pos_x+1, SIZE_X):
            if game.board[x][pos_y] != None:
                if self.team != game.board[x][pos_y].team:
                    possible_moves.append([x, pos_y])
                break
            else:
                possible_moves.append([x, pos_y])
                

        for x in range(pos_x-1, -1, -1):
            if game.board[x][pos_y] != None:
                if self.team != game.board[x][pos_y].team:
                    possible_moves.append([x, pos_y])
                break
            else:
                possible_moves.append([x, pos_y])
#
        for y in range(pos_y+1, SIZE_Y):
            if game.board[pos_x][y] != None:
                if self.team != game.board[pos_x][y].team:
                    possible_moves.append([pos_x, y])
                break
            else:
                possible_moves.append([pos_x, y])
        for y in range(pos_y-1, -1, -1):
            if game.board[pos_x][y] != None:
                if self.team != game.board[pos_x][y].team:
                    possible_moves.append([pos_x, y])
                break
            else:
                possible_moves.append([pos_x, y])


        return possible_moves


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
        pos_x = self.pos[0]
        pos_y = self.pos[1]

        possible_moves = []

        
        if pos_x - 1 >= 0 and pos_y - 2 >= 0:
            if game.board[pos_x-1][pos_y-2] == None:
                possible_moves.append([pos_x-1, pos_y-2])
            elif game.board[pos_x-1][pos_y-2].team != self.team:
                possible_moves.append([pos_x-1, pos_y-2])

        if pos_x - 2 >= 0 and pos_y - 1 >= 0:
            if game.board[pos_x-2][pos_y-1] == None:
                possible_moves.append([pos_x-2, pos_y-1]) 
            elif game.board[pos_x-2][pos_y-1].team != self.team:
                possible_moves.append([pos_x-2, pos_y-1]) 
        
        if pos_x - 2 >= 0 and pos_y + 1 < SIZE_Y:
            if game.board[pos_x-2][pos_y+1] == None:
                possible_moves.append([pos_x-2, pos_y+1]) 
            elif game.board[pos_x-2][pos_y+1].team != self.team:
                possible_moves.append([pos_x-2, pos_y+1])

        if pos_x - 1 >= 0 and pos_y + 2 < SIZE_Y:
            if game.board[pos_x-1][pos_y+2] == None:
                possible_moves.append([pos_x-1, pos_y+2]) 
            elif game.board[pos_x-1][pos_y+2].team != self.team:
                possible_moves.append([pos_x-1, pos_y+2]) 

        if pos_x + 1 < SIZE_X and pos_y -2 >= 0:
            if game.board[pos_x+1][pos_y-2] == None:
                possible_moves.append([pos_x+1, pos_y-2])
            elif game.board[pos_x+1][pos_y-2].team != self.team:
                possible_moves.append([pos_x+1, pos_y-2])

        if pos_x + 2 < SIZE_X and pos_y -1 >= 0:
            if game.board[pos_x+2][pos_y-1] == None:
                possible_moves.append([pos_x+2, pos_y-1]) 
            elif game.board[pos_x+2][pos_y-1].team != self.team:
                possible_moves.append([pos_x+2, pos_y-1]) 
        
        if pos_x + 2 < SIZE_X and pos_y + 1 < SIZE_Y:
            if game.board[pos_x+2][pos_y+1] == None:
                possible_moves.append([pos_x+2, pos_y+1]) 
            elif game.board[pos_x+2][pos_y+1].team != self.team:
                possible_moves.append([pos_x+2, pos_y+1]) 

        if pos_x + 1 < SIZE_X and pos_y + 2 < SIZE_Y:
            if game.board[pos_x+1][pos_y+2] == None:
                possible_moves.append([pos_x+1, pos_y+2]) 
            elif game.board[pos_x+1][pos_y+2].team != self.team:
                possible_moves.append([pos_x+1, pos_y+2]) 


        return possible_moves


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