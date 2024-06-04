class Pokemon:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self):
        print(f'{self.name}の攻撃！', end='')
        self.attack_message()

    def attack_message(self):
        pass

class Pikachu(Pokemon):
    def __init__(self):
        super().__init__('ピカチュウ', 20, 10)

    def attack_message(self):
        print('10万ボルト！')


class Hitokage(Pokemon):
    def __init__(self):
        super().__init__('ヒトカゲ', 18, 5)

    def attack_message(self):
        print('ひのこ！')