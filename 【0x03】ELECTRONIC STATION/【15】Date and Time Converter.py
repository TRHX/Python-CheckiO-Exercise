# ============================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【15】Date and Time Converter.py
# ============================================


def date_time(time: str) -> str:
    month = ['January', 'February', 'March', 'April', 'May',
             'June', 'July', 'August', 'September', 'October',
             'November', 'December']
    time = time.replace('.', ' ').replace(':', ' ').split()
    time[0] = str(int(time[0]))
    time[1] = month[int(time[1])-1]
    time[2] = time[2] + ' year'
    if time[3] == '01':
        time[3] = '1 hour'
    else:
        time[3] = str(int(time[3])) + ' hours'
    if time[4] == '01':
        time[4] = '1 minute'
    else:
        time[4] = str(int(time[4])) + ' minutes'
    time = ' '.join(time)
    return time


if __name__ == '__main__':
    print("Example:")
    print(date_time('01.01.2000 00:00'))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert date_time("01.01.2000 00:00") == "1 January 2000 year 0 hours 0 minutes", "Millenium"
    assert date_time("09.05.1945 06:30") == "9 May 1945 year 6 hours 30 minutes", "Victory"
    assert date_time("20.11.1990 03:55") == "20 November 1990 year 3 hours 55 minutes", "Somebody was born"
    print("Coding complete? Click 'Check' to earn cool rewards!")
