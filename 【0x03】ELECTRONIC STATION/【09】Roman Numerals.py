# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【09】Roman Numerals.py
# =====================================


def checkio(data):
    roman_list1 = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
    roman_list2 = ['X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
    roman_list3 = ['C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
    if 0 < data < 10:
        roman = roman_list1[data - 1]
        return roman
    elif 10 <= data < 100:
        if data % 10 == 0:
            roman = roman_list2[data // 10 - 1]
        else:
            roman = roman_list2[data // 10 - 1] + checkio(data % 10)
        return roman
    elif 100 <= data < 1000:
        if data % 100 == 0:
            roman = roman_list3[data // 100 - 1]
        else:
            roman = roman_list3[data // 100 - 1] + checkio(data % 100)
        return roman
    elif 1000 <= data < 9999:
        if data % 1000 == 0:
            roman = 'M' * (data // 1000)
        else:
            roman = 'M' * (data // 1000) + checkio(data % 1000)
        return roman


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(6) == 'VI', '6'
    assert checkio(76) == 'LXXVI', '76'
    assert checkio(499) == 'CDXCIX', '499'
    assert checkio(3888) == 'MMMDCCCLXXXVIII', '3888'
    print('Done! Go Check!')
