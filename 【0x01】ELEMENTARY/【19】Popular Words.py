# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【19】Popular Words.py
# =====================================


def popular_words(text: str, words: list) -> dict:
    text = text.lower().split()
    dic = {}
    for i in words:
       dic[i] = text.count(i)
    return dic


if __name__ == '__main__':
    print("Example:")
    print(popular_words('''
            When I was One
            I had just begun
            When I was Two
            I was nearly new
            ''', ['i', 'was', 'three', 'near']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert popular_words('''
            When I was One
            I had just begun
            When I was Two
            I was nearly new
            ''', ['i', 'was', 'three', 'near']) == {
                    'i': 4,
                    'was': 3,
                    'three': 0,
                    'near': 0
                }
    print("Coding complete? Click 'Check' to earn cool rewards!")
