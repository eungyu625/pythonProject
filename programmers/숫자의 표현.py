def solution(n):
    answer = 0

    for i in range(1, n + 1):
        found = False
        max_count = n // i
        result = 0
        num = i
        iter_count = 0
        while True:
            if iter_count == max_count:
                break
            result += num

            if result == n:
                found = True
                break
            num += 1
            iter_count += 1
        if found:
            answer += 1
    return answer
