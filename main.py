
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
        self.gamemode = AVIABLE_GAMEMODES[2]

        self.board = None
        self.game_process = False

        # Varibles
        self.turn = 1
        self.selected_figure = None
        self.text_print = ""

        # For Prikols
        self.processes = []

        self.set_console_style()


    def make_board(self):
        board = [[None for _ in range(self.board_size_y)] for _ in range(self.board_size_x)]

        piece_placement = {
            "Classic": [
                ("Pawn", [
                    (1, self.board_size_y // 2 - 4 + i, "White", 3) for i in range(8)
                ] + [
                    (self.board_size_x - 2, self.board_size_y // 2 - 4 + i + (1 if self.board_size_y % 2 != 0 else 0), "Black", 3) for i in range(8)
                ]),
                ("Rook", [
                    (0, self.board_size_y // 2 - 4, "White", 10), (0, self.board_size_y // 2 + 3, "White", 10), 
                    (self.board_size_x - 1, self.board_size_y // 2 - 4 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 10), 
                    (self.board_size_x - 1, self.board_size_y // 2 + 3 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 10)
                ]),
                ("Knight", [
                    (0, self.board_size_y // 2 - 3, "White", 5), (0, self.board_size_y // 2 + 2, "White", 5),
                    (self.board_size_x - 1, self.board_size_y // 2 - 3 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 5),
                    (self.board_size_x - 1, self.board_size_y // 2 + 2 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 5)
                    ]),
                ("Bishop", [
                    (0, self.board_size_y // 2 - 2, "White", 4), (0, self.board_size_y // 2 + 1, "White", 4), 
                    (self.board_size_x - 1, self.board_size_y // 2 - 2 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 4), 
                    (self.board_size_x - 1, self.board_size_y // 2 + 1 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 4)
                    ]),
                ("Queen", [
                    (0, self.board_size_y // 2 - 1, "White", 2), 
                    (self.board_size_x - 1, self.board_size_y // 2 - 1 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 2)
                    ]),
                ("King", [
                    (0,  self.board_size_y // 2, "White", 1), 
                    (self.board_size_x - 1, self.board_size_y // 2 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 1)
                    ])
            ],
            "War": [
                ("Pawn", [
                    (1, self.board_size_y // 2 - 4 + i, "White", 3) for i in range(8)
                ] + [
                    (self.board_size_x - 2, self.board_size_y // 2 - 4 + i + (1 if self.board_size_y % 2 != 0 else 0), "Black", 3) for i in range(8)
                ]),
                ("Rook", [
                    (0, self.board_size_y // 2 - 4, "White", 10), (0, self.board_size_y // 2 + 3, "White", 10), 
                    (self.board_size_x - 1, self.board_size_y // 2 - 4 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 10), 
                    (self.board_size_x - 1, self.board_size_y // 2 + 3 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 10)
                ]),
                ("Knight", [
                    (0, self.board_size_y // 2 - 3, "White", 5), (0, self.board_size_y // 2 + 2, "White", 5),
                    (self.board_size_x - 1, self.board_size_y // 2 - 3 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 5),
                    (self.board_size_x - 1, self.board_size_y // 2 + 2 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 5)
                    ]),
                ("Bishop", [
                    (0, self.board_size_y // 2 - 2, "White", 4), (0, self.board_size_y // 2 + 1, "White", 4), 
                    (self.board_size_x - 1, self.board_size_y // 2 - 2 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 4), 
                    (self.board_size_x - 1, self.board_size_y // 2 + 1 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 4)
                    ]),
                ("Queen", [
                    (0, self.board_size_y // 2 - 1, "White", 2), 
                    (self.board_size_x - 1, self.board_size_y // 2 - 1 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 2)
                    ]),
                ("King", [
                    (0,  self.board_size_y // 2, "White", 1), 
                    (self.board_size_x - 1, self.board_size_y // 2 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 1)
                    ])
            ],
            "Infinity": [
                ("Pawn", [
                    (1, i, "White", 3) for i in range(self.board_size_y)
                ] + [
                    (self.board_size_x - 2, i, "Black", 3) for i in range(self.board_size_y)
                ]),
                ("Rook", [
                    (0, self.board_size_y // 2 - 4, "White", 10), (0, self.board_size_y // 2 + 3, "White", 10), 
                    (self.board_size_x - 1, self.board_size_y // 2 - 4 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 10), 
                    (self.board_size_x - 1, self.board_size_y // 2 + 3 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 10)
                ]),
                ("Knight", [
                    (0, self.board_size_y // 2 - 3, "White", 5), (0, self.board_size_y // 2 + 2, "White", 5),
                    (self.board_size_x - 1, self.board_size_y // 2 - 3 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 5),
                    (self.board_size_x - 1, self.board_size_y // 2 + 2 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 5)
                    ]),
                ("Bishop", [
                    (0, self.board_size_y // 2 - 2, "White", 4), (0, self.board_size_y // 2 + 1, "White", 4), 
                    (self.board_size_x - 1, self.board_size_y // 2 - 2 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 4), 
                    (self.board_size_x - 1, self.board_size_y // 2 + 1 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 4)
                    ]),
                ("Queen", [
                    (0, self.board_size_y // 2 - 1, "White", 2), 
                    (self.board_size_x - 1, self.board_size_y // 2 - 1 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 2)
                    ]),
                ("King", [
                    (0,  self.board_size_y // 2, "White", 1), 
                    (self.board_size_x - 1, self.board_size_y // 2 + (1 if self.board_size_y % 2 != 0 else 0), "Black", 1)
                    ])
            ],
        }

        for figure, positions in piece_placement.get(self.gamemode, []):
            for position in positions:
                if len(position) == 3:
                    y, x, team = position
                    board[y][x] = AVIABLE_FIGURES[figure](team, (y, x), figure)
                elif len(position) == 4:
                    y, x, team, health = position
                    board[y][x] = AVIABLE_FIGURES[figure](team, (y, x), figure, health)

        if self.gamemode != "Classic":
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

        
            
    def generate_colums_label(self):
        labels = []
        size = len(ALPHABET)

        for lenght in range(1,4):
            for i in range(size ** lenght):
                label = ""
                temp = i

                for _ in range(lenght):
                    label = ALPHABET[temp % size] + label
                    temp //= size

                labels.append(label)
                if len(labels)>= self.board_size_y:
                    return labels
                
        return labels


    def draw_board(self):
        label_y = self.generate_colums_label()
        label_x_lenght = len(str(self.board_size_x))
        border_str_y = " " + " " * (label_x_lenght + 2)
       
        # ------------- 
        for label in label_y:
            label_y_lenght = len(label)
            if label_y_lenght == 1:
                padding_left = "   "
                padding_right = "    "
            elif label_y_lenght == 2:
                padding_left = "   "
                padding_right = "   "
            else:
                padding_left = "  "
                padding_right = "   "
            border_str_y += f"{padding_left}{label}{padding_right}"


        print(border_str_y)
        # ------------- 

         
        for x in range(self.board_size_x):
            # ------------- 
            border_str_y2 =  " " + " " * (label_x_lenght + 2) + "------- " * self.board_size_y
 
            
            print(border_str_y2)
           # ------------- 
            for row in range(3):
                row_label = str(self.board_size_x - x).rjust(label_x_lenght)
                if row == 1:
                    row_str = f" {row_label} | "
                else:
                    row_str = " " + " " * label_x_lenght + " | "
                
                for y in range(self.board_size_y):
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
                    row_str += f"{row_label}"

                print(row_str)
        
        
        # ------------- 
        print(border_str_y2)
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



    def set_console_style(self):
        window_size_x = min(self.board_size_x, 12)
        window_size_y = min(self.board_size_y, 12)

        label_x_lenght = len(str(self.board_size_x))

        cols = (8 * window_size_y + 9) + int(label_x_lenght* 1.5) if label_x_lenght >= 2 else (8 * window_size_y + 9) 
        lines = 3 * window_size_x + window_size_x + 12

        os.system(f'mode con: cols={cols} lines={lines}')
        hwnd = ctypes.windll.kernel32.GetConsoleWindow()
        if hwnd != 0:
            GWL_STYLE = -16
            current_style = ctypes.windll.user32.GetWindowLongW(hwnd, GWL_STYLE)

            new_style = current_style & ~0x00040000

            ctypes.windll.user32.SetWindowLongW(hwnd, GWL_STYLE, new_style)
            ctypes.windll.user32.SetWindowPos(hwnd, 0, 0, 0, 0, 0, 0x0002 | 0x0001)

            handle = ctypes.windll.kernel32.GetStdHandle(-11)
            buffer_info = ctypes.create_string_buffer(22)
            buffer_cols = (8 * self.board_size_y + 9) + int(label_x_lenght* 1.5) if label_x_lenght >= 2 else (8 * self.board_size_y + 9) 
            buffer_lines = 3 * self.board_size_x + self.board_size_x + 12
            
            ctypes.windll.kernel32.SetConsoleScreenBufferSize(handle, ctypes.wintypes._COORD(buffer_cols, buffer_lines))


def clear():
    os.system('cls')


if __name__ == "__main__":
    
     
    init(autoreset=True)
    game = Game()
    game.run()
