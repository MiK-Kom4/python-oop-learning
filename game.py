class Game:
    def battle(self, pokemon1, pokemon2):
        print(f'{pokemon1.name}が現れた！{pokemon1.name}のHPは{pokemon1.hp}だ！')
        print(f'{pokemon2.name}が現れた！{pokemon2.name}のHPは{pokemon2.hp}だ！')
        pokemon1.attack()
        pokemon2.attack()