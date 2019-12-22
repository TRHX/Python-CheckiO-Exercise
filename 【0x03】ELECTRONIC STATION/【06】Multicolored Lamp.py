# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【06】Multicolored Lamp.py
# =====================================


colors = ['Green', 'Red', 'Blue', 'Yellow']


class Lamp:
    def __init__(self):
        self.count = 0

    def light(self):
        if self.count == 4:
            self.count = 0
            color = colors[self.count]
        else:
            color = colors[self.count]
            self.count += 1
        return color


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing

    lamp_1 = Lamp()
    lamp_2 = Lamp()

    lamp_1.light()  # Green
    lamp_1.light()  # Red
    lamp_2.light()  # Green

    assert lamp_1.light() == "Blue"
    assert lamp_1.light() == "Yellow"
    assert lamp_1.light() == "Green"
    assert lamp_2.light() == "Red"
    assert lamp_2.light() == "Blue"
    print("Coding complete? Let's try tests!")
