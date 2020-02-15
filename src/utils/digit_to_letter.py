abc = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_-'


def digit_to_letter(digit: int) -> str:
    abc_len = len(abc)
    result = ''

    delta = digit

    while delta > 0:
        index = delta % abc_len
        result = abc[index] + result

        delta = delta - index
        delta = delta // abc_len

    return result
