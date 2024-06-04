class Pokemon:
    def __init__(self, name, hp, atk, speed):
        self._name = name
        self._hp = hp
        self._max_hp = hp * 2
        self._atk = atk
        self._speed = speed

    def attack(self, target):
        target.hp -= self._atk
        print(f'{self._name}の攻撃！', end='')
        self.attack_message(target)

    def attack_message(self, target):
        pass

    def is_fainted(self):
        return self._hp <= 0

    @property
    def name(self):
        return self._name

    @property
    def hp(self):
        return self._hp

    @property
    def atk(self):
        return self._atk

    @property
    def speed(self):
        return self._speed

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
        super().__init__('ピカチュウ', 20, 10, 3)

    def attack_message(self, target):
        print(f'10万ボルト！{target.name}は{self._atk}ダメージをもらった！{target.name}のHPは{target.hp}だ！')


class Hitokage(Pokemon):
    def __init__(self):
        super().__init__('ヒトカゲ', 18, 5, 3)

    def attack_message(self, target):
        print(f'ひのこ！{target.name}は{self._atk}ダメージをもらった！{target.name}のHPは{target.hp}だ！')