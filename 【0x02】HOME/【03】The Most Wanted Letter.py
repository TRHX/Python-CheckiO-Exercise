# ===========================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【03】The Most Wanted Letter.py
# ===========================================


import re


def checkio(text: str) -> str:
    text = re.sub('[\W\d_]', '', text)
    text = text.lower()
    dicts = {}
    for i in set(text):
        dicts[i] = text.count(i)
    dicts = dict(sorted(dicts.items(),key=lambda x:x[0]))
    return max(dicts, key=dicts.get)


if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")
