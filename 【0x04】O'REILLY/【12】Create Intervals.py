# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【12】Create Intervals.py
# =====================================


def create_intervals(data):
    start, end = [], []
    for i in data:
        if i-1 not in data:
            start.append(i)
        if i+1 not in data:
            end.append(i)
    return list(zip(sorted(start), sorted(end)))


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert create_intervals({1, 2, 3, 4, 5, 7, 8, 12}) == [(1, 5), (7, 8), (12, 12)], "First"
    assert create_intervals({1, 2, 3, 6, 7, 8, 4, 5}) == [(1, 8)], "Second"
    print('Almost done! The only thing left to do is to Check it!')
