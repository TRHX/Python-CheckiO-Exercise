# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【21】Between Markers.py
# =====================================


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    start = text.find(begin)
    finish = text.find(end)

    if start != -1 and finish != -1:
        start += len(begin)
        return text[start:finish]
    elif start == -1 and finish == -1:
        return text
    elif start != -1 and finish == -1:
        start += len(begin)
        return text[start:]
    elif start == -1 and finish != -1:
        start = 0
        return text[start:finish]


if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
