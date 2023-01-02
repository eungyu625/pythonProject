N = int(input())
applicants = list(map(int, input().split()))
b, c = map(int, input().split())
answer = 0

for i in range(len(applicants)):
    applicants[i] -= b
    answer += 1

for i in range(len(applicants)):
    if applicants[i] <= 0:
        continue
    if applicants[i] % c == 0:
        now = applicants[i] // c
    else:
        now = applicants[i] // c + 1
    answer += now

print(answer)
