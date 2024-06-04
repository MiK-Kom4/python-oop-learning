from random import shuffle


class Game:
    def __init__(self, pokemon1, pokemon2):
        self._pokemon1 = pokemon1
        self._pokemon2 = pokemon2
    def battle(self):
        self._start()
        self._attack_order()
        winner, loser = self._attack()
        self._show_result(winner, loser)

    def _start(self):
        print(f'{self._pokemon1.name}が現れた！{self._pokemon1.name}のHPは{self._pokemon1.hp}だ！')
        print(f'{self._pokemon2.name}が現れた！{self._pokemon2.name}のHPは{self._pokemon2.hp}だ！')

    def _attack_order(self):
        if self._pokemon1.speed < self._pokemon2.speed:
            tmp = self._pokemon1
            self._pokemon1 = self._pokemon2
            self._pokemon2 = tmp
        elif self._pokemon1.speed == self._pokemon2.speed:
            order_list = [self._pokemon1, self._pokemon2]
            shuffle(order_list)
            self._pokemon1, self._pokemon2 = order_list[0], order_list[1]


    def _attack(self):
        while True:
            self._pokemon1.attack(self._pokemon2)
            if self._pokemon2.is_fainted():
                return (self._pokemon1, self._pokemon2)

            self._pokemon2.attack(self._pokemon1)
            if self._pokemon1.is_fainted():
                return (self._pokemon2, self._pokemon1)

    def _show_result(self, winner, loser):
        print(f'{loser.name}は倒れた。{winner.name}の勝ち！')
