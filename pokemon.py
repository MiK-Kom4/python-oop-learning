class Pokemon:
    def __init__(self, name, hp, atk):
        self._name = name
        self._hp = hp
        self._max_hp = hp * 2
        self._atk = atk

    def attack(self):
        print(f'{self._name}の攻撃！', end='')
        self.attack_message()

    def attack_message(self):
        pass

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def atk(self):
        return self._atk

    @hp.setter
    def hp(self, value):
        if value < 0:
            self._hp = 0
        elif value > self._max_hp:
            self._hp = self._max_hp
        else:
            self._hp = value

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