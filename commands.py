import time, os, random
from config import *
from figures import *

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

class InventoryCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/inv - Looks in inventory\n"

    def execute(self, arg):
        text = ""

        if arg.selected_figure == None:
            text += "Please select figure first"
            return text
    
        for item in arg.selected_figure.inventory:
            text += ("     > " + item.name)
        return text


class BuildCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/build - Use buildkit for buildings\n"

    def execute(self, game):
        text = ""

        if game.selected_figure == None:
            text += "Please select figure first"
            return text
        
        x = game.selected_figure.pos[0]
        y = game.selected_figure.pos[1]
    
        for item in game.selected_figure.inventory:
            if item.name == "BuildKit":
                if game.board[x+1][y] == None and game.selected_figure.team == "White":
                   game.board[x+1][y] = Baricade("Build", (x+1, y), "Wall",4)
                elif game.board[x-1][y] == None and game.selected_figure.team == "Black":
                   game.board[x-1][y] = Baricade("Build", (x-1, y), "Wall",4)
                
                text += "Builded"
                return text
        
        text += "No Building Kit"
        return text

class SelectCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/select <cordinate> - A1 to select figure\n"

    def execute(self, game, arg):
        text = "     >" 

        if len(arg) < 2 or arg[0].isnumeric() or not arg[1].isnumeric() :
            text += "Wrong argument"
            return text

        x = ord(arg[0].upper()) - ord('A')
        y = SIZE_Y - int(arg[1]) 
        

        #if game.turn % 2 == 0 and game.board[y][x].team == "White":
        #    game.selected_figure = game.board[y][x]
        #elif game.turn % 2 == 1 and game.board[y][x].team == "Black":
        #    game.selected_figure = game.board[y][x]
        game.selected_figure = game.board[y][x]
        #else:
        #    text += "Error Not Select Figure" 
        #    return text
            

        if game.selected_figure != None:
            text += f"Figure selected from {y} \ {x} or {arg[0]}{arg[1]}\n" 
            text += "     >"
            text += f"Figure name {game.selected_figure.name}" 


        return text
    

class InfoCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/info - Info about Figure\n"

    def execute(self, arg):
        text = "     >"

        if arg.selected_figure == None:
            text += "Please select figure first"
            return text
        figure = arg.selected_figure
        text += f"{figure.team} {figure.name}, HP = {figure.health}, Pos = {figure.pos[0]}/{figure.pos[1]}"
        return text

        

class MoveCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/move <arf> - Move selected figure\n"

    def execute(self, game, arg):
        text = "     >"

        if len(arg) < 2 or arg[0].isnumeric() or not arg[1].isnumeric() :
            text += "Wrong argument"
            return text
        
        x = ord(arg[0].upper()) - ord('A')
        y = SIZE_Y - int(arg[1]) 

        if game.selected_figure == None:
            text += "Please select figure first"
            return text
        

        posibale_moves = game.selected_figure.moves(game)
    
        for move in posibale_moves:
            if y == move[0] and x == move[1]:
                
                if game.board[y][x] != None:
                    game.board[y][x].health -=1
                    if game.destroy_figure([y,x]):
                        text += f"Figure attack {arg[0]}{arg[1]} - {game.board[y][x].name}"
                    

                if game.board[y][x] == None:
                    game.board[y][x] = game.selected_figure
                    game.board[game.selected_figure.pos[0]][game.selected_figure.pos[1]] = None
                    text += f"Figure moved to {game.selected_figure.pos[0]}, {game.selected_figure.pos[1]}"
                    game.selected_figure.pos = (y,x)

                    if isinstance(game.selected_figure, Pawn):
                        game.selected_figure.first_turn = False

                return text
            else:
                text += "Cant move"

       
        return text





















WIDTH, HEIGHT = 75, 40
gradient = ".:!/r(l1Z4H9W8$@"
grid = [[' ' for _ in range(WIDTH)] for _ in range(HEIGHT)]

class SandCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/particles - Simulate particles falling like sand using the current board state.\n"

    def execute(self, game, *args):
        # Create a new array of symbols using the drawn board
        board_symbols = []
        board_symbols.append("        A       B       C       D       E       F       G       H")
        for y in range(8):
            board_symbols.append("     ------- ------- ------- ------- ------- ------- ------- -------")
            for row in range(3):
                row_symbols = []
                for x in range(8):
                    figure = game.board[y][x]
                    if figure is None:
                        if (x + y) % 2 == 0:
                            cell = "     "
                        else:
                            cell = ". . ."
                    else:
                        cell = figure.icon[row]
                    row_symbols.append((x, y * 3 + row, cell))
                board_symbols.append(row_symbols)  # Only row_symbols is a list of tuples
        board_symbols.append("     ------- ------- ------- ------- ------- ------- ------- -------")
        board_symbols.append("        A       B       C       D       E       F       G       H")

        # Extract individual symbols for the falling animation
        particles = []
        for item in board_symbols:
            if isinstance(item, list):  # Only process rows that contain tuples
                for x, y, cell in item:
                    for i, symbol in enumerate(cell):
                        if symbol != ' ':
                            particles.append((x * 7 + i, y, symbol))

        def update_particles():
            nonlocal particles
            new_particles = []
            for x, y, symbol in particles:
                if y < HEIGHT - 1 and (x, y + 1, symbol) not in particles:
                    new_particles.append((x, y + 1, symbol))
                else:
                    new_particles.append((x, y, symbol))
            particles[:] = new_particles

        def render():
            os.system('cls' if os.name == 'nt' else 'clear')
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    grid[y][x] = ' '
            for x, y, symbol in particles:
                if 0 <= y < HEIGHT and 0 <= x < WIDTH:
                    grid[y][x] = symbol
            for row in grid:
                print(''.join(row))

        # Run the particle simulation
        for _ in range(60):
            update_particles()
            render()
            time.sleep(0.1)
        return "Particle simulation completed.\n"

