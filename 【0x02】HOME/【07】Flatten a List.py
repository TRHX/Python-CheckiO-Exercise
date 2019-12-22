# =====================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【07】Flatten a List.py
# =====================================


import re


def flat_list(array):
    array = re.findall(r'-?\d+', str(array))
    list = []
    for i in array:
        i = int(i)
        list.append(i)
    return list

'''
解法二：此方法有缺陷，如果给定的列表为空就会报错，只适合非空列表

def flat_list(array):
    array = str(array)
    array = array.replace('[','').replace(']','')
    return list(eval(array))
'''

if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
