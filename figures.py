

class Figure:
    def __init__(self, team, pos, name):
        self.name = name
        self.pos = pos
        self.team = team
        self.alive = True


class Pawn(Figure):
    def __init__(self, team, pos, name):
        super().__init__(team, pos, name)
        

        if team == "White":
            self.icon = ["  _  ", " (@) ", " d@b "]
        elif team == "Black":
            self.icon = ["  _  ", " ( ) ", " /_\\ "]
        else:
            self.icon = "E"

    def moves(self):
        pass

class Rook(Figure):
    def __init__(self, team, pos, name):
        super().__init__(team, pos, name)
        if team == "White":
            self.icon = ["@___@", " @@@ ", "d@@@b"]
        elif team == "Black":
            self.icon = ["[___]", " [ ] ", "/___\\"]
        else:
            self.icon = "E"


class Knight(Figure):
    def __init__(self, team, pos, name):
        super().__init__(team, pos, name)
        if team == "White":
            self.icon = [" %~b ", "`'dX ", " d@@b"]
        elif team == "Black":
            self.icon = [" %~\\ ", "`')( ", " <__>"]
        else :
            self.icon = "E"


class Bishop(Figure):
    def __init__(self, team, pos, name):
        super().__init__(team, pos, name)
        if team == "White":
            self.icon = [" .@. ", " @@@ ", "./A\\."]
        elif team == "Black":
            self.icon = [" .O. ", " \\ / ", " /_\\ "]
        else:
            self.icon = "E"


class Queen(Figure):
    def __init__(self, team, pos, name):
        super().__init__(team, pos, name)
        if team == "White":
            self.icon = ["\\o*o/", " @@@ ", "d@@@b"]
        elif team == "Black":
            self.icon = ["\\o^o/", " [ ] ", "/___\\"]
        else:
            self.icon = "E"


class King(Figure):
    def __init__(self, team, pos, name):
        super().__init__(team, pos, name)
        if team == "White":
            self.icon = ["__+__", "`@@@'", "d@@@b"]
        elif team == "Black":
            self.icon = ["__+__", "`. .'", "/___\\"]
        else:
            self.icon = "E"