
from config import *
 

import os, ctypes, time
from colorama import Fore, Back, Style, init

class Game:
    def __init__(self):   
        # Static Varibles
        self.commands = AVIABLE_COMMANDS
        self.buildings = AVIABLE_BUILDINGS
        self.board_size_x = SIZE_X
        self.board_size_y = SIZE_Y
        self.gamemode = AVIABLE_GAMEMODES[1]

        self.board = None
        self.game_process = False

        # Varibles
        self.turn = 1
        self.selected_figure = None
        self.text_print = ""

        # For Prikols
        self.processes = []


    def make_board(self):
        board = [[None for _ in range(SIZE_Y)] for _ in range(SIZE_X)]

        piece_placement = {
            "Classic": [
                ("Pawn", [(1, i, "White") for i in range(8)] + [(6, i, "Black") for i in range(8)]),
                ("Rook", [(0, 0, "White"), (0, 7, "White"), (7, 0, "Black"), (7, 7, "Black")]),
                ("Knight", [(0, 1, "White"), (0, 6, "White"), (7, 1, "Black"), (7, 6, "Black")]),
                ("Bishop", [(0, 2, "White"), (0, 5, "White"), (7, 2, "Black"), (7, 5, "Black")]),
                ("Queen", [(0, 3, "White"), (7, 3, "Black")]),
                ("King", [(0, 4, "White"), (7, 4, "Black")])
            ],
            "War": [
                ("Pawn", [(1, i, "White", 3) for i in range(8)] + [(6, i, "Black", 3) for i in range(8)]),
                ("Rook", [(0, 0, "White", 10), (0, 7, "White", 10), (7, 0, "Black", 10), (7, 7, "Black", 10)]),
                ("Knight", [(0, 1, "White", 5), (0, 6, "White", 5), (7, 1, "Black", 5), (7, 6, "Black", 5)]),
                ("Bishop", [(0, 2, "White", 4), (0, 5, "White", 4), (7, 2, "Black", 4), (7, 5, "Black", 4)]),
                ("Queen", [(0, 3, "White", 2), (7, 3, "Black", 2)]),
                ("King", [(0, 4, "White", 1), (7, 4, "Black", 1)])
            ]
        }

        for figure, positions in piece_placement.get(self.gamemode, []):
            for position in positions:
                if len(position) == 3:
                    y, x, team = position
                    board[y][x] = AVIABLE_FIGURES[figure](team, (y, x), figure)
                elif len(position) == 4:
                    y, x, team, health = position
                    board[y][x] = AVIABLE_FIGURES[figure](team, (y, x), figure, health)

        if self.gamemode == "War":
            for x in board:
                for y in x:
                    if y is not None:
                        random_items = [random.choice(list(AVIABLE_ITEMS)) for _ in range(random.randint(1, 5))]
                        y.set_items(random_items)

        return board

    def restart_board(self):
        self.board = self.make_board()
        self.turn = 1
        self.selected_figure = None
    
    def end_board(self):
        clear()
        print('\n\n')                                                                                    
        print('                                     88      ')    
        print('                                     88      ')    
        print('                                     88      ')    
        print('      ,adPPYba, 8b,dPPYba,   ,adPPYb,88      ')    
        print('     a8P_____88 88P\'   `"8a a8"    `Y88     ')    
        print('     8PP""""""" 88       88 8b       88      ')    
        print('     "8b,   ,aa 88       88 "8a,   ,d88      ')    
        print('      `"Ybbd8"\' 88       88  `"8bbdP"Y8     ')    
        print('                                             ')    
        print('                                             ')   
        print('\n\n')
        print('     >Hello, For start game type /start. Settings now is default')
        print(f'     >Gamemode Selected: {Fore.LIGHTGREEN_EX}{self.gamemode}{Fore.WHITE}, Board size {Fore.LIGHTGREEN_EX}{self.board_size_x }{Fore.WHITE}/{Fore.LIGHTGREEN_EX}{self.board_size_y}{Fore.WHITE}')
        print('     >  ---  ---  PRESS ANY BOTTON  ---  ---  \n\n')
        input()

    def check_figure(self, team, type_figure):
        for row in self.board:
            for figure in row:
                if isinstance(figure, type_figure) and team == figure.team:
                    return figure
            
        return None

    def colorize_figure(self, text):
        result = ""
        for char in text:
            if random.choice([True, False]): 
                result += f"{Fore.RED}{char}{Style.RESET_ALL}"
            else:
                result += char
        return result

    def destroy_figure(self, arg):
        if self.board[arg[0]][arg[1]].health <= 0:
            if self.board[arg[0]][arg[1]].name == 'King':
                self.game_process = False
                self.end_board()
            self.board[arg[0]][arg[1]] = None
            return True
        return False

    def end_turn(self):
        if self.check_figure("White", King):
            print("King alive")
            input()
        #self.turn += 1
        #self.selected_figure = None
        pass

    def event(self):
        str_command = input("     /").strip()
        str_command_list = []
        current_arg = ""
        in_quotes = False
        skip_space = False

        for char in str_command:
            if char == '"':
                in_quotes = not in_quotes
                if not in_quotes:
                    str_command_list.append(current_arg)
                    current_arg = ""
                    skip_space = True
            elif char == ' ' and not in_quotes:
                if current_arg:
                    str_command_list.append(current_arg)
                    current_arg = ""
            else:
                current_arg += char

        if current_arg:
            str_command_list.append(current_arg)

        if not str_command_list:
            self.text_print += "No command entered"
            return

        command_key = str_command_list[0].lower()
        args = str_command_list[1:]

        command = self.commands.get(command_key, None)
        if command is not None:
            self.text_print += command.execute(self, *args)
        else:
            self.text_print += f"Unknown command: {command_key}"

        
            
  
    def draw_board(self):
        cord_y = "ABCDEFGHIJKLMNOP"
        # ------------- 
        border_str_y = " "
        for i in range(SIZE_Y):
                border_str_y += "       "
                border_str_y += cord_y[i]
        print(border_str_y)
        # ------------- 

         
        for x in range(SIZE_X):
            # ------------- 
            border_str_y2 = "    "
            for _ in range(SIZE_Y):
                border_str_y2 += " "
                border_str_y2 += "-------"
            print(border_str_y2)
           # ------------- 
            for row in range(3):
                row_str = ""
                if SIZE_X - x > 9:
                    row_str = " {} | ".format(SIZE_X - x) if row == 1 else "    | "
                else:
                    row_str = "  {} | ".format(SIZE_X - x) if row == 1 else "    | "
                
                for y in range(SIZE_Y):
                    figure = self.board[x][y]
                    if figure is None:
                        if (x + y) % 2 == 0:
                            cell = "     "
                        else:
                            cell = ". . ."
                    else:
                        if hasattr(figure, 'health') and figure.health == 1 and figure.name != "King":
                            cell = self.colorize_figure(figure.icon[row])
                        else:
                            cell = figure.icon[row]
                    row_str += f"{cell} | "
                if row == 1:
                    row_str += f"{SIZE_X - x}"
                print(row_str)
        
        
        # ------------- 
        border_str_y2 = "    "
        for _ in range(SIZE_Y):
            border_str_y2 += " "
            border_str_y2 += "-------"
        print(border_str_y2)
        # ------------- 
        # ------------- 
        border_str_y = " "
        for i in range(SIZE_Y):
                border_str_y += "       "
                border_str_y += cord_y[i]
        print(border_str_y)
        # ------------- 
        
        
    def draw_menu(self):
        print('\n\n')
        print('                88                                          ')
        print('                88                                          ')
        print('                88                                          ')
        print('      ,adPPYba, 88,dPPYba,   ,adPPYba, ,adPPYba, ,adPPYba,  ')
        print('     a8"     "" 88P\'    "8a a8P_____88 I8[    "" I8[    "" ')
        print('     8b         88       88 8PP"""""""  `"Y8ba,   `"Y8ba,   ')
        print('     "8a,   ,aa 88       88 "8b,   ,aa aa    ]8I aa    ]8I  ')
        print(f'      `"Ybbd8"\' 88       88  `"Ybbd8"\' `"YbbdP"\' `"YbbdP"\'    {Back.WHITE}{Fore.BLACK}By BGF{Style.RESET_ALL}')
        print('\n\n')
        print('     >Hello, For start game type /start. Settings now is default')
        print(f'     >Gamemode Selected: {Fore.LIGHTGREEN_EX}{self.gamemode}{Fore.WHITE}, Board size {Fore.LIGHTGREEN_EX}{self.board_size_x }{Fore.WHITE}/{Fore.LIGHTGREEN_EX}{self.board_size_y}{Fore.WHITE}')
        print('     >You can Change params in future, for all commands type /help \n\n')



    def draw(self):
        if self.game_process:
            self.draw_board()
        else:
            self.draw_menu()

        if self.text_print != "":
            print(self.text_print) 
            self.text_print = ""


    def proceess(self):
        pass
        # chess_event = []

        # for event in chess_event:
        #     time.sleep(0.1) 


    def run(self):
        while True:
            clear()
            self.draw()
            self.event()
            self.proceess()



def set_console_style():
    os.system(f'mode con: cols={8*SIZE_Y+ 9} lines={5*SIZE_X}')
    hwnd = ctypes.windll.kernel32.GetConsoleWindow()
    if hwnd != 0:
        GWL_STYLE = -16
        current_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)

        new_style = current_style & ~0x00040000
        
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, new_style)
        ctypes.windll.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0, 0x0002 | 0x0001)
def clear():
    os.system('cls')


if __name__ == "__main__":
    set_console_style()
     
    init(autoreset=True)
    game = Game()
    game.run()