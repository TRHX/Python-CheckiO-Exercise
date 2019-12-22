# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【15】Remove Accents.py
# =====================================


import unicodedata


def checkio(in_string):
    # remove accents
    return ''.join(i for i in unicodedata.normalize('NFD', in_string) if not unicodedata.combining(i))


# These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
