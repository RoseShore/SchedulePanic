import random
import _tkinter
class Player:
    def __init__ (self, name):
        #deck of cards, 2 of each type
        self.cards = [1, 1, 0, 0, -1, -1]
        #relationship level
        self.status = 10
        #character name
        self.name = name

you = Player("Lucy")
stevie = Player("Stevie")
marrow = Player("Marrow")
thorn = Player("Thorn")