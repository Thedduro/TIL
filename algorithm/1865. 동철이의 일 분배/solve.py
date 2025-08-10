import sys
sys.stdin = open('input.txt', 'r')

def solve(idx, answer):
    global max_value

    if answer <= max_value: 
        return
    if idx >= N:
        max_value = answer
        return
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            solve(idx+1, answer * job[idx][i])
            visited[i] = False

T = int(input())

for tc in range(1, T+1):
    N = int(input())

    job = [list(map(lambda x: int(x)/100, input().split())) for _ in range(N)]

    visited = [False] * N
    max_value = 0
    answer = 100

    solve(0, answer)

    print('#{} {:6f}'.format(tc, max_value))