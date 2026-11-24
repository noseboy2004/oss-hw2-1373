def digit_sum(n):
    total = 0
    for ch in str(n):
        total += int(ch)
    return total


def lucky_number(n):
    while n > 10:
        n = digit_sum(n)
    return n
