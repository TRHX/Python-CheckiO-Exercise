# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【09】Sun Angle.py
# =====================================


def sun_angle(time):
    time = time.split(':')
    if int(time[0]) == 18 and int(time[1]) == 0:
        return int(180)
    elif 6 <= int(time[0]) < 18:
        if int(time[1]) > 0:
            return (int(time[0])-6)*15 + int(time[1])*0.25
        else:
            return (int(time[0])-6)*15
    else:
        return "I don't see the sun!"


if __name__ == '__main__':
    print("Example:")
    print(sun_angle("07:00"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert sun_angle("07:00") == 15
    assert sun_angle("01:23") == "I don't see the sun!"
    print("Coding complete? Click 'Check' to earn cool rewards!")
