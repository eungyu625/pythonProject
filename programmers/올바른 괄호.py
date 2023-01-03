def solution(s):
    left = 0

    for i in range(len(s)):
        now = s[i]
        if now == "(":
            left += 1
        else:
            if left == 0:
                return False
            left -= 1
    if left > 0:
        return False
    return True
