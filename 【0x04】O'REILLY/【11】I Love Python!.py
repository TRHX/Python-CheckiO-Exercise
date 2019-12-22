# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【11】I Love Python!.py
# =====================================


def i_love_python():
    """
        Let's explain why do we love Python.
    """
    return "I love Python!"


'''
# Select your language in which you want to say "I Love Python!"
# By default it answers in english.
def i_love_python(language="English"):    
    if language == "Binary": return "01000010011001010010000001110011011101010111001001100101001000000111010001101111001000000110010001110010011010010110111001101011001000000111100101101111011101010111001000100000010011110111011001100001011011000111010001101001011011100110010100101110"
    if language == "Deutsch": return "Ich liebe Python!"
    if language == "English": return "I love Python!"
    if language == "Español": return "Me Encanta Python!"
    if language == "Espéranto": return "Αγαπώ Python!"
    if language == "Elf": return "Amin mela Python!"
    if language == "Ελληνική": return "Αγαπώ Python!"
    if language == "Français": return "J'aime Python !"
    if language == "Italiano": return"Adoro Python!"
    if language == "русский": return "Я люблю Python !"
    if language == "L337 Speak": return "1 L0\/3 p'/7|-|0|\|!"
    if language == "코리안": return "나는 파이썬 Python!"
    if language == "中國": return "我愛Python的 !"
    if language == "日本の": return "私はPythonのが大好き !"
    if language == "हिन्दी": return "मैं अजगर प्यार!"
'''


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert i_love_python() == "I love Python!"
