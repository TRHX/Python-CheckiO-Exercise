# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【03】Speech Module.py
# =====================================


FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    if 0 <= number < 10:
        english = FIRST_TEN[number - 1]
        return english
    elif 10 <= number < 20:
        english = SECOND_TEN[number - 10]
        return english
    elif 20 <= number < 100:
        if number % 10 == 0:
            english = OTHER_TENS[number // 10 - 2]
            return english
        else:
            english = OTHER_TENS[number // 10 - 2] + ' ' + FIRST_TEN[number % 10 - 1]
            return english
    else:
        if number % 100 == 0:
            english = FIRST_TEN[number // 100 - 1] + ' ' + HUNDRED
            return english
        else:
            english = FIRST_TEN[number // 100 - 1] + ' ' + HUNDRED + ' ' + checkio(number % 100)
            return english


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')
