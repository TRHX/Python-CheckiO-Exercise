# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【08】Probably Dice.py
# =====================================


def probability(dice_number, sides, target):
    dic = {}

    def calculation(dice_number, sides, target):
        if dice_number > target or dice_number * sides < target:
            return 0
        if dice_number == 1:
            return 1
        if (dice_number, sides, target) in dic:
            return dic[(dice_number, sides, target)]
        else:
            dic[(dice_number, sides, target)] = sum(
                calculation(dice_number - 1, sides, target - i) for i in range(1, sides + 1))
        return dic[(dice_number, sides, target)]

    return calculation(dice_number, sides, target) / sides ** dice_number


if __name__ == '__main__':
    # These are only used for self-checking and are not necessary for auto-testing
    def almost_equal(checked, correct, significant_digits=4):
        precision = 0.1 ** significant_digits
        return correct - precision < checked < correct + precision


    assert (almost_equal(probability(2, 6, 3), 0.0556)), "Basic example"
    assert (almost_equal(probability(2, 6, 4), 0.0833)), "More points"
    assert (almost_equal(probability(2, 6, 7), 0.1667)), "Maximum for two 6-sided dice"
    assert (almost_equal(probability(2, 3, 5), 0.2222)), "Small dice"
    assert (almost_equal(probability(2, 3, 7), 0.0000)), "Never!"
    assert (almost_equal(probability(3, 6, 7), 0.0694)), "Three dice"
    assert (almost_equal(probability(10, 10, 50), 0.0375)), "Many dice, many sides"
