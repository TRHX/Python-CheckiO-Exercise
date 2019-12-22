# ================================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【05】Time Converter (12h to 24h).py
# ================================================


import time


def time_converter(init_time):
    init_time = init_time.replace('a.m.', 'AM').replace('p.m.', 'PM')
    init_time = time.strptime(init_time, '%I:%M %p')
    init_time = time.strftime('%H:%M', init_time)
    return init_time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30 p.m.'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30 p.m.') == '12:30'
    assert time_converter('9:00 a.m.') == '09:00'
    assert time_converter('11:15 p.m.') == '23:15'
    print("Coding complete? Click 'Check' to earn cool rewards!")
