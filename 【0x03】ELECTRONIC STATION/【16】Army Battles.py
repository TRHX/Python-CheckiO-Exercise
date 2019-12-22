# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【16】Army Battles.py
# =====================================


class Army():
    def __init__(self):
        self.health = 0
        self.attack = 0
        self.num = 0

    def add_units(self, x, num):
        self.health = x().health
        self.attack = x().attack
        self.num = num


class Warrior:
    health = 50
    attack = 5
    is_alive = True


class Knight(Warrior):
    attack = 7


def fight(army1, army2):
    while army1.health > 0:
        army2.health -= army1.attack
        army1.health -= army2.attack
    if army2.health > army1.health:
        army1.is_alive = False
        return False
    else:
        army2.is_alive = False
        return True


class Battle:
    def fight(self, army1, army2):
        x2 = y2 = 0
        while army1.num > 0 and army2.num > 0:
            x1 = army1.health if x2 == 0 else x2
            y1 = army2.health if y2 == 0 else y2
            while True:
                y1 -= army1.attack
                if y1 <= 0:
                    x2 = x1
                    y2 = 0
                    army2.num -= 1
                    break
                x1 -= army2.attack
                if x1 <= 0:
                    y2 = y1
                    x2 = 0
                    army1.num -= 1
                    break
        if army1.num:
            return True
        else:
            return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    print("Coding complete? Let's try tests!")

if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    # fight tests
    chuck = Warrior()
    bruce = Warrior()
    carl = Knight()
    dave = Warrior()
    mark = Warrior()

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False

    # battle tests
    my_army = Army()
    my_army.add_units(Knight, 3)

    enemy_army = Army()
    enemy_army.add_units(Warrior, 3)

    army_3 = Army()
    army_3.add_units(Warrior, 20)
    army_3.add_units(Knight, 5)

    army_4 = Army()
    army_4.add_units(Warrior, 30)

    battle = Battle()

    assert battle.fight(my_army, enemy_army) == True
    assert battle.fight(army_3, army_4) == False
    print("Coding complete? Let's try tests!")
