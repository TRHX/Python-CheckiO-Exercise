# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【12】Xs and Os Referee.py
# =====================================


from typing import List


def checkio(game_result: List[str]) -> str:
    list2 = []
    for i in game_result:
        list2.extend(list(i))
    if list2[0] != '.' and (list2[0] == list2[3] == list2[6] or list2[0] == list2[4] == list2[8] or list2[0] == list2[1] == list2[2]):
        return list2[0]
    elif list2[1] != '.' and (list2[1] == list2[4] == list2[7]):
        return list2[1]
    elif list2[2] != '.' and (list2[2] == list2[4] == list2[6] or list2[2] == list2[5] == list2[8]):
        return list2[2]
    elif list2[3] != '.' and (list2[3] == list2[4] == list2[5]):
        return list2[3]
    elif list2[6] != '.' and (list2[6] == list2[7] == list2[8]):
        return list2[6]
    else:
        return 'D'


if __name__ == '__main__':
    print("Example:")
    print(checkio(["X.O",
                   "XX.",
                   "XOO"]))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
