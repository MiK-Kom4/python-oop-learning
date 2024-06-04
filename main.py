from game import Game
from pokemon import Pikachu, Hitokage

pikachu = Pikachu()
hitokage = Hitokage()
game = Game(pikachu, hitokage)
pikachu.hp = 10000
game.battle()