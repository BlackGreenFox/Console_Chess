

class Command:
    def __init__(self):
        self.description = "Empty"

    def execute(self, arg):
        pass # Implement in Other


class HelpCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/help <page> - Command print info aboiut all comands\n"

    def execute(self, arg):
        text = ""
        for command in arg.commands.values():
            text += ("     > " + command.description)
        return text


class SelectCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/select <cordinate> - A1 to select figure\n"

    def execute(self, game, arg):
        x =  ord(arg[0].upper()) - ord('A')
        y = 8 - int(arg[1]) 
        
        text = "     >" 


        if game.turn % 2 == 0 and game.board[y][x].team == "White":
            game.selected_figure = game.board[y][x]
        elif game.turn % 2 == 1 and game.board[y][x].team == "Black":
            game.selected_figure = game.board[y][x]
        else:
            text += "Error Not Select Figure" 

        if game.selected_figure != None:
            text += f"Figure selected from {y} \ {x} or {arg[0]}{arg[1]}\n" 
            text += f"     >Figure name {game.selected_figure.name}" 


        return text
    

class MoveCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/move <arf> - Move selected figure\n"

    def execute(self, game, arg):
        text = "     >"
        x =  ord(arg[0].upper()) - ord('A')
        y = 8 - int(arg[1]) 

        if game.selected_figure == None:
            text += "Please select figure first"
            return text
        
        game.board[y][x] = game.selected_figure
        game.board[game.selected_figure.pos[0]][game.selected_figure.pos[1]] = None
        text += f"Figure moved to {game.selected_figure.pos[0]}, {game.selected_figure.pos[1]}"
        game.selected_figure.pos = (y,x)

       
        return text
