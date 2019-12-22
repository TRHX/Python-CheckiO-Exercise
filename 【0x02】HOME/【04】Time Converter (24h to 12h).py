# =================================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【04】Time Converter (24h to 12h).py
# =================================================


import time


def time_converter(init_time):
    init_time = time.strptime(init_time, '%H:%M')
    init_time = time.strftime('%I:%M %p', init_time)
    init_time = init_time.split(' ')
    if init_time[1] == 'PM':
        init_time[1] = 'p.m.'
    else:
        init_time[1] = 'a.m.'
    init_time = ' '.join(init_time)
    init_time = list(init_time)
    if init_time[0] == '0':
        init_time[0] = ''
    init_time = ''.join(init_time)
    return init_time


if __name__ == '__main__':
    print("Example:")
    print(time_converter('12:30'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert time_converter('12:30') == '12:30 p.m.'
    assert time_converter('09:00') == '9:00 a.m.'
    assert time_converter('23:15') == '11:15 p.m.'
    print("Coding complete? Click 'Check' to earn cool rewards!")
