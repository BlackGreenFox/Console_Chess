
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

    def Use(self, figure):
        figure.health += self.health

