# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【08】Long Repeat.py
# =====================================


def long_repeat(line: str) -> int:
    new_string = ''
    num = 0
    max_num = 0
    for string in line:
        if string != new_string:
            new_string = string
            num = 1
        else:
            num += 1
        max_num = max(max_num, num)
    return max_num


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert long_repeat('sdsffffse') == 4, "First"
    assert long_repeat('ddvvrwwwrggg') == 3, "Second"
    assert long_repeat('abababaab') == 2, "Third"
    assert long_repeat('') == 0, "Empty"
    print('"Run" is good. How is "Check"?')
