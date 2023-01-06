def check(number):
    bin_num = bin(number)[2:]
    result = 0
    for i in range(len(bin_num)):
        if bin_num[i] == "1":
            result += 1
    return result


def solution(n):
    one_number = check(n)
    while True:
        n += 1
        if one_number == check(n):
            break
    return n