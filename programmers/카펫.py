def solution(brown, yellow):
    answer = []
    if yellow == 1:
        return [3, 3]
    for i in range(1, yellow // 2 + 1):
        if yellow % i != 0:
            continue
        yellow_width = yellow / i
        yellow_length = i
        res = 2 * yellow_length + 2 * (yellow_width + 2)
        if int(res) == brown:
            answer = [int(yellow_width + 2), int(yellow_length + 2)]
            break
    return answer
