# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【13】The Warriors.py
# =====================================


class Warrior:
   health = 50
   is_alive = True
   attack = 5


class Knight(Warrior):
    attack = 7


def fight(unit_1, unit_2):
    while unit_1.health > 0:
        unit_2.health -= unit_1.attack
        unit_1.health -= unit_2.attack
    if unit_2.health > unit_1.health:
        unit_1.is_alive = False
        return False
    else:
        unit_2.is_alive = False
        return True


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
