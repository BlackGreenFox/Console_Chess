class Figure:
    def __init__(self, pos, team):
        self.pos = pos
        self.team = team
        self.alive = True


class Rook(Figure):
    def __init__(self, pos, team):
        super().__init__(pos, team)
        if team:
            self.draw = ["@___@", " @@@ ", "d@@@b"]
        else:
            self.draw = ["[___]", " [ ] ", "/___\\"]


class Knight(Figure):
    def __init__(self, pos, team):
        super().__init__(pos, team)
        if team:
            self.draw = [" %~b ", "`'dX ", " d@@b"]
        else:
            self.draw = [" %~\\ ", "`')( ", " <__>"]


class Bishop(Figure):
    def __init__(self, pos, team):
        super().__init__(pos, team)
        if team:
            self.draw = [" .@. ", " @@@ ", "./A\\."]
        else:
            self.draw = [" .O. ", " \\ / ", " /_\\ "]


class Queen(Figure):
    def __init__(self, pos, team):
        super().__init__(pos, team)
        if team:
            self.draw = ["\\o*o/", " @@@ ", "d@@@b"]
        else:
            self.draw = ["\\o^o/", " [ ] ", "/___\\"]


class King(Figure):
    def __init__(self, pos, team):
        super().__init__(pos, team)
        if team:
            self.draw = ["__+__", "`@@@'", "d@@@b"]
        else:
            self.draw = ["__+__", "`. .'", "/___\\"]


class Pawn(Figure):
    def __init__(self, pos, team):
        super().__init__(pos, team)
        if team:
            self.draw = ["  _  ", " (@) ", " d@b "]
        else:
            self.draw = ["  _  ", " ( ) ", " /_\\ "]