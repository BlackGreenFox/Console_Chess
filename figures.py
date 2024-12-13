class Figure:
    def __init__(self, team, pos, name, health = 1, selectable = True):
        self.selectable = selectable
        self.alive = True
        self.pos = pos
        self.team = team

        self.name = name
        self.health = health
        self.inventory = []

    def set_items(self, items):
        self.inventory = items
 


class Baricade(Figure):
    def __init__(self, team, pos, name, health = 1):  
        super().__init__(team, pos, name, health)  
        self.icon = ["|ooo|", "|XXX|", "|XXX|"]
          


class Pawn(Figure):
    def __init__(self, team, pos, name, health = 1):
        super().__init__(team, pos, name, health)
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

        directions_white = [(1,0), (1,-1), (1,1), (2, 0)]
        directions_black = [(-1,0), (-1, -1), (-1,1), (-2, 0)]
        directions = directions_white if self.team == "White" else directions_black
        
        if not self.first_turn:
            directions.pop()

        for dx, dy in directions: 
            x = pos_x + dx
            y = pos_y + dy

            if 0 <= x < game.board_size_x and 0 <= y + game.board_size_y:
                if game.board[x][y] is None:
                    if dy == 0:
                        possible_moves.append([x,y])
                elif game.board[x][y].team != self.team and dy != 0:
                    possible_moves.append([x,y])

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

        directions = [(-1,0), (1, 0), (0,-1), (0,1)]

        for dx, dy in directions:
            x = pos_x
            y = pos_y
            while 0 <= x + dx < game.board_size_x and 0 <= y + dy < game.board_size_y:
                x += dx
                y += dy

                if game.board[x][y] is None:
                    possible_moves.append([x,y])
                elif game.board[x][y].team != self.team:
                    possible_moves.append([x,y])
                    break
                else:
                    break

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

        directions = [(-2,-1), (-2, 1), (2,-1), (2,1),(-1,-2), (-1, 2), (1,-2), (1,2)]

        for dx, dy in directions:
            x = pos_x + dx
            y = pos_y + dy

            if 0 <= x < game.board_size_x and 0 <= y + game.board_size_y:
                if game.board[x][y] is None:
                    possible_moves.append([x,y])
                elif game.board[x][y].team != self.team:
                    possible_moves.append([x,y])

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
        pos_x = self.pos[0]
        pos_y = self.pos[1]

        possible_moves = []

        directions = [(-1,-1), (-1, 1), (1,-1), (1,1)]

        for dx, dy in directions:
            x = pos_x
            y = pos_y
            while 0 <= x + dx < game.board_size_x and 0 <= y + dy < game.board_size_y:
                x += dx
                y += dy

                if game.board[x][y] is None:
                    possible_moves.append([x,y])
                elif game.board[x][y].team != self.team:
                    possible_moves.append([x,y])
                    break
                else:
                    break

        return possible_moves



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
        pos_x = self.pos[0]
        pos_y = self.pos[1]

        possible_moves = []

        directions_diagonale = [(-1,-1), (-1, 1), (1,-1), (1,1)]
        directions_line = [(-1,0), (1, 0), (0,-1), (0,1)]

        for dx, dy in directions_diagonale:
            x = pos_x
            y = pos_y
            while 0 <= x + dx < game.board_size_x and 0 <= y + dy < game.board_size_y:
                x += dx
                y += dy

                if game.board[x][y] is None:
                    possible_moves.append([x,y])
                elif game.board[x][y].team != self.team:
                    possible_moves.append([x,y])
                    break
                else:
                    break

        for dx, dy in directions_line:
            x = pos_x
            y = pos_y
            while 0 <= x + dx < game.board_size_x and 0 <= y + dy < game.board_size_y:
                x += dx
                y += dy

                if game.board[x][y] is None:
                    possible_moves.append([x,y])
                elif game.board[x][y].team != self.team:
                    possible_moves.append([x,y])
                    break
                else:
                    break
        

        return possible_moves


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
        pos_x = self.pos[0]
        pos_y = self.pos[1]

        possible_moves = []
    
        directions = [(-1,-1), (-1, 1), (1,-1), (1,1),(-1,0), (1, 0), (0,-1), (0,1)]

        for dx, dy in directions:
            x = pos_x + dx
            y = pos_y + dy

            if 0 <= x < game.board_size_x and 0 <= y + game.board_size_y:
                if game.board[x][y] is None:
                    possible_moves.append([x,y])
                elif game.board[x][y].team != self.team:
                    possible_moves.append([x,y])

        return possible_moves