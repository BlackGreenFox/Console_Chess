import time, os, random
from figures import Pawn
from items import *

class Command:
    def __init__(self):
        self.description = "Empty"

    def execute(self, game, *args):
        pass  


class StartCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/start - Command for Start game or Restart"

    def execute(self, game, *args):
        if not game.game_process:
            game.restart_board()
            game.game_process = True
            return "     >Game started. For help type /help command\n     >Have a nice game"
        
        print("     >You sure about RESTART your game? Y/N")
        str_command = input("     /").upper()

        if str_command == 'Y' or str_command == 'YES':
            game.restart_board()
            return "     >NEW Game started. For help type /help command\n     >Better luck this time?"
        else:
            return "     >I abort all operations"

    

class HelpCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/help <page> - Command print info about all commands"

    def execute(self, game, *args):
        commands_per_page = 5
        page = 1

        if args:
            try:
                page = int(args[0])
                if page < 1:
                    page = 1
            except ValueError:
                return "     >Invalid page number. Please enter a valid integer."

        start_index = (page - 1) * commands_per_page
        end_index = start_index + commands_per_page

        command_list = list(game.commands.values())

        if start_index >= len(command_list):
            return f"     >Page {page} is out of range. There are only {((len(command_list) - 1) // commands_per_page) + 1} pages available."
        
        text = f"     >Rules asdasdasdasd \n     >sdasdasd \n     >Today is day\n\n"
        text += f"     >Commands - Page {page} of {((len(command_list) - 1) // commands_per_page) + 1}:\n\n"
        for command in command_list[start_index:end_index]:
            text += (f"     >{command.description}\n")
        return text


class SelectCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/select <coordinate> - Selects a figure at the given position"

    def execute(self, game, *args):
        if not game.game_process:
            return "     >Opppsi.. Game not start yet"

        if not args:
            return "     >No coordinate provided. Please provide a valid coordinate."

        coordinate = args[0]
        if len(coordinate) < 2 or not coordinate[0].isalpha() or not coordinate[1:].isdigit():
            return "     >Wrong argument. Please provide a valid coordinate like A1."

        y = ord(coordinate[0].upper()) - ord('A')
        x = game.board_size_x - int(coordinate[1:])

        if x < 0 or x >= game.board_size_x or y < 0 or y >= game.board_size_y:
            return "     >Invalid coordinate. Out of board range."

        
        selected_figure = None

        if game.turn % 2 and game.board[x][y].team == "White":
            selected_figure = game.board[x][y] 
        elif not game.turn % 2 and game.board[x][y].team == "Black":
            selected_figure = game.board[x][y] 
        else:
            return f"     >No... is {"White" if game.turn % 2 else "Black"} turn now."

        if selected_figure is None:
            return f"     >No figure found at {coordinate}."

        game.selected_figure = selected_figure
        return f"     >Figure selected: {selected_figure.name} at {coordinate}"


class MoveCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/move <arf> - Move selected figure"

    def execute(self, game, *args):
        if not game.game_process:
            return "     >Opppsi.. Game not start yet"

        if not args:
            return "     >No target provided. Please provide a valid target."

        target = args[0]
        if len(target) < 2 or not target[0].isalpha() or not target[1:].isdigit():
            return "     >Wrong argument. Please provide a valid target like A1."

        y = ord(target[0].upper()) - ord('A')
        x = game.board_size_x - int(target[1:])

        if x < 0 or x >= game.board_size_x or y < 0 or y >= game.board_size_y:
            return "     >Invalid target. Out of board range."

        if game.selected_figure is None:
            return "     >Please select a figure first."

        possible_moves = game.selected_figure.moves(game)

        for move in possible_moves:
            if x == move[0] and y == move[1]:
                target_cell = game.board[x][y]
                if target_cell is not None:
                    target_cell.health -= 1
                    if target_cell.health <= 0:
                        game.destroy_figure((x, y))
                        game.board[y][x] = None

                        game.board[game.selected_figure.pos[0]][game.selected_figure.pos[1]] = None
                        game.board[x][y] = game.selected_figure
                        game.selected_figure.pos = (x, y)
                        game.end_turn()
                        return f"     >Figure attacked and destroyed at {target}"
                    else:
                        return f"     >Figure attacked at {target} - {target_cell.name}"

                game.board[x][y] = game.selected_figure
                game.board[game.selected_figure.pos[0]][game.selected_figure.pos[1]] = None
                game.selected_figure.pos = (x, y)

                if isinstance(game.selected_figure, Pawn):
                    game.selected_figure.first_turn = False

                game.end_turn()
                return f"     >Figure moved to {target}"
        
        available_moves = " | ".join([f"{chr(move[1] + ord('A'))}{game.board_size_x - move[0]}" for move in possible_moves])
        return f"     >Cannot move to {target}. Available moves: {available_moves}"


class InfoCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/info - Info about Figure"

    def execute(self, game, *args):
        if not game.game_process:
            return "     >Opppsi.. Game not start yet"
        
        if game.selected_figure == None:
            return f"     >Please select figure first"
        
        figure = game.selected_figure
        return f"     >{figure.team} {figure.name}, HP = {figure.health}, Pos = {figure.pos[0]}/{figure.pos[1]}"
 
    

class InventoryCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/inv - Looks in inventory"

    def execute(self,  game, *args):
        if not game.game_process:
            return "     >Opppsi.. Game not start yet"
        
        text = "     >Inventory:"
    
        if game.selected_figure == None:
            return f"     >Please select figure first"
    
        for item in game.selected_figure.inventory:
            text += (" " + item.name + ",")
        return text

    

class LookCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/look - Looks in inventory"

    def execute(self, game, *args):
        if not game.game_process:
            return "     >Opppsi.. Game not start yet"
        
        if game.selected_figure == None:
            return f"     >Please select figure first"
 
    
        for item in game.selected_figure.inventory:
            if item.name == args[0]:
                return f"     >{item.name} - {item.description}"
            
        return f"     >No such Item"
    



class UseCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/use - Use any Item"

    def execute(self, game, *args):
        if not game.game_process:
            return "     >Opppsi.. Game not start yet"
        
        text = ""

        if game.selected_figure is None:
            return "     >Please select figure first"

        # Перевіряємо чи є предмет в інвентарі
        for item in game.selected_figure.inventory:
            if item.name == args[0]:
                # Перевірка на наявність будівлі, якщо аргумент переданий
                if len(args) < 2 or args[1] not in game.buildings:
                    return f"     >Building {args[1]} is not available." if len(args) > 1 else "     >Please specify the building to use the item on."
                
                building_type = args[1]  # Тип будівлі
                target_building = game.buildings.get(building_type)

                # Якщо координати не вказані, використовуємо (x+1, y+1)
                if len(args) < 3:
                    target_coords = None
                else:
                    target_coords = tuple(map(int, args[2].split(',')))  # Вказуємо координати через "x,y"
                
                # Використовуємо BuildKit для побудови
                if isinstance(item, BuildKit):
                    item.Use(game, target_coords)
                    game.selected_figure.inventory.remove(item)
                    return f"{game.selected_figure.name} used item '{args[0]}' to build {building_type} at {target_coords}"

                # Якщо предмет не є BuildKit, використовується як звичайний предмет
                item.Use(game.selected_figure, target_coords)
                game.selected_figure.inventory.remove(item)
                return f"{game.selected_figure.name} used item '{args[0]}' at coordinates {target_coords}"

        return f"     >Item {args[0]} is not in your inventory."


class BuildCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/build - Use buildkit for buildings"

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



    






class SizeCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = f"/size - Min {MIN_SIZE_X}/{MIN_SIZE_Y} | Max {MAX_SIZE_X}/{MAX_SIZE_Y}"

    def execute(self, arg):
        text = "     >"

        if arg.selected_figure == None:
            text += "Please select figure first"
            return text
        
        figure = arg.selected_figure
        text += f"{figure.team} {figure.name}, HP = {figure.health}, Pos = {figure.pos[0]}/{figure.pos[1]}"
        return text



class TestCommand(Command):
    def __init__(self):
        super().__init__()
        self.description = "/test - Test command that prints all arguments"

    def execute(self, game, *args):
        text = ""
        for i, arg in enumerate(args, start=1):
            text += f"Argument {i} = {arg}\n"
        return text



















