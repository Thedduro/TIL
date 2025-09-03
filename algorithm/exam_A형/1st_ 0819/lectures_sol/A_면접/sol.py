import sys
sys.stdin = open('input.txt')


'''
    완전 탐색 불가능 N <= 500
    2**500 ... 불가능!
'''

def search(arr, r, cnt, acc, visited):
    global result
    if acc > result:
        return

    if cnt == K:
        cnt = 0
        acc *= 2

    if r == M:
        result = min(result, acc)
    else:
        item = arr[r]
        if visited[item-1]:
            visited[item] = cnt + 1
            search(arr, r+1, cnt+1, acc+1, visited)
        else:
            cnt = 1
            visited[item] = cnt
            search(arr, r+1, cnt, acc+1, visited)



T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    # 최종 결괏값. 충분히 큰 값
    result = float('inf')
    data = list(range(N))
    power_set = []
    for i in range(1<<N):
        tmp = []
        tmp_len = 0
        for j in range(N):
            if i & (1<<j):
                tmp.append(data[j])
                tmp_len += 1
        if tmp_len == M:
            power_set.append(tmp)
    for items in power_set:
        visited = [0] * N
        visited[items[0]] = 1
        search(items, 1, 1, 1, visited)

    print(f'#{tc} {result}')