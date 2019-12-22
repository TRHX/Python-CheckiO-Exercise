# ====================================================
# --*-- coding: utf-8 --*--
# @Author  : TRHX
# @Blog    : www.itrhx.com
# @CSDN    : itrhx.blog.csdn.net
# @FileName: 【12】Largest Rectangle in a Histogram.py
# ====================================================


def largest_histogram(histogram):
    i = 0
    max_value = 0
    stack = []
    histogram.append(0)
    while i < len(histogram):
        if len(stack) == 0 or histogram[stack[-1]] <= histogram[i]:
            stack.append(i)
            i += 1
        else:
            now_idx = stack.pop()
            if len(stack) == 0:
                max_value = max(max_value,i * histogram[now_idx])
            else:
                max_value = max(max_value,(i- stack[-1] -1) * histogram[now_idx])
    return max_value


if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")
