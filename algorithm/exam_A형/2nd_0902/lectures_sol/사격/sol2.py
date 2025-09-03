import sys
sys.stdin = open('input.txt')

'''사고 검증
    1. 느린 이유가 원본에서 pop(i) 번째, insert(i)번째 때문일까?
    2. 그럼 원본에서 0으로 바꾸고, 0이 아닌 경우들을 찾으러 보내면 어떨까?
    
    -> 결론: 어차피 왼쪽, 오른쪽 탐사하러 가는 과정이 느리다.
'''

def saerch(acc):
    global result
    # 다 터트리면 갱신
    if not any(data):
        result = max(result, acc)
        return

    # 남은 풍선으로 모든 상황 계산
    for i in range(N):
        # 여기 이미 터졌으면 무시
        if data[i] == 0: continue
        score = 0
        l = i - 1   # 왼쪽
        r = i + 1   # 오른쪽
        # 왼쪽 범위를 벗어나지 않았고, 풍선 없으면
        while l >= 0 and data[l] == 0:
            l -= 1  # 계속 왼쪽으로

        # 오른쪽 범위를 벗어나지 않았고, 풍선 없으면
        while r < N and data[r] == 0:
            r += 1  # 계속 오른쪽으로

        # 조사 끝나고
        if l == -1:         # 범위 벗어났으면
            left = 1        # 1
        else:               # 범위 내였으면
            left = data[l]  # 해당 위치 점수가 왼쪽

        # 오른쪽도 똑같이
        if r == N:
            right = 1
        else:
            right = data[r]

        score = left * right    # 점수는 왼쪽 * 오른쪽

        # 근데 둘다 범위 벗어났으면??
        if l == -1 and r == N:
            score = data[i] # 현재 위치가 점수

        # 1. i 번째 터트린다? -> i 번째를 0으로한다.
        # 1-1. 대신 원본 별도 소지
        origin_balloon = data[i]
        data[i] = 0
        # 2. 더해보고
        saerch(acc + score)
        # 3. 다시 i 번째에 원상복구
        data[i] = origin_balloon

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = list(map(int, input().split()))
    result = 0
    saerch(0)
    print(f'#{tc} {result}')
