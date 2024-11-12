from items import *

SIZE_X = 8
SIZE_Y = 8
MIN_SIZE_X = 8
MIN_SIZE_Y = 8
MAX_SIZE_X = 16
MAX_SIZE_Y = 16

AVIABLE_ITEMS = [
    Medkit("Small Medkit", "Classic medkit regen 1 hp", 1),
    Medkit("Medium Medkit", "Classic medkit regen 2 hp", 2),
    Medkit("Large Medkit", "Classic medkit regen 3 hp", 3),
    BuildKit("BuildKit", "Kit for build")
]

AVIABLE_GAMEMODES = [
    "Classic",
    "War"
]

GAMEMODE = AVIABLE_GAMEMODES[1]
