from items import *
from figures import *
from commands import *
from settings import *

AVIABLE_COMMANDS = {
    "help" : HelpCommand(),
    'start' : StartCommand(),
    "settings" : SettingsCommand(),
    "set" : SettingsCommand(),
    "select" : SelectCommand(),
    "move" : MoveCommand(),
    "inv" : InventoryCommand(),
    "build" : BuildCommand(),
    "info" : InfoCommand(),
    "use" : UseCommand(),
    "look" : LookCommand(),
    "test" : TestCommand(),
    "explode": ExplodeCommand(),
}

AVIABLE_BUILDINGS = {
    "Baricade" : Baricade("Build", (0, 0), "Wall",4),
    "Baricade2" : Baricade("Build", (0, 0), "Baricade",4),
}

AVIABLE_ITEMS = {
    Medkit("Small Medkit", "Classic medkit regen 1 hp", 1),
    Medkit("Medium Medkit", "Classic medkit regen 2 hp", 2),
    Medkit("Large Medkit", "Classic medkit regen 3 hp", 3),
    BuildKit("BuildKit", "Kit for build", AVIABLE_BUILDINGS)
}

AVIABLE_FIGURES = {
    "Pawn": Pawn,
    "Rook": Rook,
    "Knight": Knight,
    "Bishop": Bishop,
    "Queen": Queen,
    "King": King,
}

 
