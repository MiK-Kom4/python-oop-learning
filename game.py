class Game:
    def battle(self, pokemon):
        print(f'{pokemon.name}が現れた！{pokemon.name}のHPは{pokemon.hp}だ！')
        pokemon.attack()