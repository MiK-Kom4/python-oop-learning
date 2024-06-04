from game import Game
from pokemon import Pikachu, Hitokage

game = Game()
pikachu = Pikachu()
hitokage = Hitokage()
pikachu.hp = 10000
game.battle(pikachu, hitokage)