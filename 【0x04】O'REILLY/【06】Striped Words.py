# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【06】Striped Words.py
# =====================================


VOWELS = "AEIOUY"
CONSONANTS = "BCDFGHJKLMNPQRSTVWXZ"


def checkio(text):
    text = text.replace(',', ' ').replace('.', ' ').split()
    num = 0
    n = 0
    for i in text:
        if len(i) < 2:
            n = 0
        for j in range(len(i)-1):
            if (i[j].upper() in CONSONANTS and i[j+1].upper() in CONSONANTS) or (i[j].upper() in VOWELS and i[j+1].upper() in VOWELS) or i[j].isdigit():
                n = 0
                break
            else:
                n = 1
        num += n
    return num


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio("My name is ...") == 3, "All words are striped"
    assert checkio("Hello world") == 0, "No one"
    assert checkio("A quantity of striped words.") == 1, "Only of"
    assert checkio("Dog,cat,mouse,bird.Human.") == 3, "Dog, cat and human"
