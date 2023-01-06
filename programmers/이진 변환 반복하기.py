def solution(s):
    answer = []
    number, zero = 0, 0
    while True:
        if s == "1":
            answer = [number, zero]
            break
        res = 0
        for i in range(len(s)):
            if s[i] == "0":
                res += 1
        length = len(s) - res
        s = bin(length)[2:]
        number += 1
        zero += res
    return answer
