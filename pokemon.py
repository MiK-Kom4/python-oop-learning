class Pokemon:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

    def attack(self):
        print(f'{self.name}の攻撃！10万ボルト')