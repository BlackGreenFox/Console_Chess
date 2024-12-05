

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def Use(self, figure):
        pass
        # Realization in others


class Medkit(Item):
    def __init__(self, name, description, health):
        super().__init__(name, description)
        self.health = health

    def Use(self, figure, target = None):
        if target == None:
            figure.health += self.health
        else:
            target.health += self.health

class BuildKit(Item):
    def __init__(self, name, description, builds):
        super().__init__(name, description)
        self.builds = builds  # Будівлі, які може побудувати BuildKit
        self.description += f" | Can build: {', '.join(self.builds.keys())}"

    def Use(self, game, pos=None):
        # Якщо позиція не вказана
        if pos is None:
            x = game.selected_figure.pos[0]
            y = game.selected_figure.pos[1]
            if game.board[x + 1][y] is None and game.selected_figure.team == "White":
                game.board[x + 1][y] = self.builds["Baricade"]
            elif game.board[x - 1][y] is None and game.selected_figure.team == "Black":
                game.board[x - 1][y] = self.builds["Baricade"]
        else:
            # Перевіряємо тип pos - якщо це рядок, а не ціле число
            if isinstance(pos, str):
                target_x = ord(pos[0].upper()) - ord('A')  # Перший символ - літера
                target_y = 8 - int(pos[1])  # Другий символ - цифра (від 1 до 8)
            elif isinstance(pos, tuple) and len(pos) == 2:
                target_x, target_y = pos  # Якщо це кортеж з чисел (x, y)
            else:
                raise ValueError("Invalid position format. Expected a string like 'A1' or a tuple of coordinates.")
            
            if game.board[target_x][target_y] is None:
                game.board[target_x][target_y] = self.builds["Baricade"]
        
        return


        
        

