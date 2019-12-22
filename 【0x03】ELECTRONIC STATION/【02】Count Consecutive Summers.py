# ==============================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【02】Count Consecutive Summers.py
# ==============================================


def count_consecutive_summers(num):
    n = 0
    for i in range(1,num+1):
        m = i
        while m < num:
            i,m = i+1,m+i+1
        if m == num:
            n += 1
    return n


if __name__ == '__main__':
    print("Example:")
    print(count_consecutive_summers(42))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_consecutive_summers(42) == 4
    assert count_consecutive_summers(99) == 6
    assert count_consecutive_summers(1) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")
