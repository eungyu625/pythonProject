dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

N = int(input())
classroom = [[0] * N for _ in range(N)]
students = [[] for _ in range(pow(N, 2) + 1)]


def find_seat(now, favorite):
    candidate = []
    for i in range(N):
        for j in range(N):
            if classroom[i][j] != 0:
                continue
            like = 0
            empty = 0
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if classroom[nx][ny] in favorite:
                        like += 1
                    if classroom[nx][ny] == 0:
                        empty += 1
            candidate.append([like, empty, i, j])
    candidate.sort(key=lambda l: (-l[0], -l[1], l[2], l[3]))
    classroom[candidate[0][2]][candidate[0][3]] = now


def solve():
    answer = 0
    for i in range(N):
        for j in range(N):
            result = 0
            now = classroom[i][j]
            for k in range(4):
                nx, ny = i + dx[k], j + dy[k]
                if 0 <= nx < N and 0 <= ny < N:
                    if classroom[nx][ny] in students[now][0]:
                        result += 1
            if result > 0:
                answer += pow(10, result - 1)
    return answer


for _ in range(pow(N, 2)):
    student, fav_1, fav_2, fav_3, fav_4 = map(int, input().split())
    students[student].append([fav_1, fav_2, fav_3, fav_4])
    find_seat(student, [fav_1, fav_2, fav_3, fav_4])

print(solve())
