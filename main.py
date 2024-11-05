from figures import *
from commands import *
from config import *
import os, ctypes


class Game:
    def __init__(self):   
        # Varibles
        self.processes = []
        self.turn = 1
        self.board = self.make_board()
        self.text_print = ""
        self.selected_figure = None
        self.commands ={
            "help" : HelpCommand(),
            "select" : SelectCommand(),
            "move" : MoveCommand(),
            "sand": SandCommand(),
            "inv" : InventoryCommand()
        }

    def make_board(self):
        board = [[None for _ in range(SIZE_Y)] for _ in range(SIZE_X)]

        if GAMEMODE == "Classic":
            for i in range(8):
                board[1][i] = Pawn("White", (1, i), "Pawn")
                board[6][i] = Pawn("Black", (6, i), "Pawn")

            board[0][0] = Rook("White", (0, 0), "Rook")
            board[0][7] = Rook("White", (0, 7), "Rook")
            board[7][0] = Rook("Black", (7, 0), "Rook")
            board[7][7] = Rook("Black", (7, 7), "Rook")

            board[0][1] = Knight("White", (0, 1), "Knight")
            board[0][6] = Knight("White", (0, 6), "Knight")
            board[7][1] = Knight("Black", (7, 1), "Knight")
            board[7][6] = Knight("Black", (7, 6), "Knight")

            board[0][2] = Bishop("White", (0, 2), "Bishop")
            board[0][5] = Bishop("White", (0, 5), "Bishop")
            board[7][2] = Bishop("Black", (7, 2), "Bishop")
            board[7][5] = Bishop("Black", (7, 5), "Bishop")

            board[0][3] = Queen("White", (0, 3), "Queen")
            board[0][4] = King("White", (0, 4), "King")
            board[7][3] = Queen("Black", (7, 3), "Queen")
            board[7][4] = King("Black", (7, 4), "King")
        elif GAMEMODE == "War":
            for i in range(8):
                board[1][i] = Pawn("White", (1, i), "Pawn", 3)
                board[6][i] = Pawn("Black", (6, i), "Pawn", 3)

            board[0][0] = Rook("White", (0, 0), "Rook", 10)
            board[0][7] = Rook("White", (0, 7), "Rook", 10)
            board[7][0] = Rook("Black", (7, 0), "Rook", 10)
            board[7][7] = Rook("Black", (7, 7), "Rook", 10)

            board[0][1] = Knight("White", (0, 1), "Knight",5)
            board[0][6] = Knight("White", (0, 6), "Knight",5)
            board[7][1] = Knight("Black", (7, 1), "Knight",5)
            board[7][6] = Knight("Black", (7, 6), "Knight",5)

            board[0][2] = Bishop("White", (0, 2), "Bishop",4)
            board[0][5] = Bishop("White", (0, 5), "Bishop",4)
            board[7][2] = Bishop("Black", (7, 2), "Bishop",4)
            board[7][5] = Bishop("Black", (7, 5), "Bishop",4)

            board[0][3] = Queen("White", (0, 3), "Queen", 2)
            board[0][4] = King("White", (0, 4), "King", 1)
            board[7][3] = Queen("Black", (7, 3), "Queen", 2)
            board[7][4] = King("Black", (7, 4), "King", 1)
        return board

    def event(self):
       if self.text_print != "":
            print(self.text_print) 
            self.text_print = ""

       str_command = input("     /")
       str_command = str_command.split()

       if str_command[0] in self.commands:
          command_instance = self.commands[str_command[0]]

          if len(str_command) > 1:
            self.text_print += command_instance.execute(self, str_command[1])
          else:
            self.text_print += command_instance.execute(self)
       else:
          self.text_print += (f"Unknown command: {str_command[0]}")
               
 
  
    def draw(self):
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
                        cell = figure.icon[row]
                    row_str += f"{cell} | "
                if row == 1:
                    row_str += f"{SIZE_X - x}"
                print(row_str)
        # ------------- 
        border_str_y2 = "    "
        for _ in range(SIZE_X):
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




    def run(self):
        while True:
            clear()
            self.draw()
            self.event()



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

    game = Game()
    game.run()