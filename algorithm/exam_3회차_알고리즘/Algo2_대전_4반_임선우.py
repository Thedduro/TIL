'''
    시간을 매개 변수로 bfs문제로 풀어보자!
    1. 알파벳을 순서대로 돌면서 가능한 인덱스 위치를 모두 저장
    2. 인덱스를 순회하면서 세균 증식
    3. 그 다음 알파벳 순회
    + 만약 순회 횟수가 최대 증식 값을 넘는다면 해당 알파벳은 순회 종료
'''

direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def bfs(v, time, max):
     # BASE_CASE 설정
    if time >= max: # 최대 배양 횟수 넘으면 리턴
        return
    
    # 현재의 증식하려는 알파벳의 인덱스를 넘겨줘야해
    idx = []
    for x in range(M):
        for y in range(N):
            if board[x][y] == v:
                idx.append((x,y)) # 현재 해당 알파벳의 인덱스를 다 저장
   
    for x, y in idx:
        for dx, dy  in direction:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= M or ny < 0 or ny >= N: # 보드판 넘어가면 무시
                continue
            if board[nx][ny] != '.': # 증식이 불가한 경우
                continue
            board[nx][ny] = v # 증식했다.


T = int(input())
alpha = ['A', 'B', 'C', 'D','E','F','G','H','I','J','K','L','M','N'
        ,'O','P','Q','R','S','T','U','V','W','X','Y','Z']

for tc in range(1, T+1):
    N, M = map(int, input().split())
    K = int(input())
    expend = list(map(int, input().split()))
    board = [list(input().split()) for _ in range(M)]

    time = 0
    for _ in range(max(expend)):
        for k in range(K):
            v = alpha[k]
            bfs(v, time, expend[k])
        time += 1    

    print(f'#{tc}')
    # 출력형식 맞추기
    for row in board:
        v = ''
        for i, r in enumerate(row):
            if i == N-1:
                v += r
            else:
                v += r
                v += ' '
        print(v)



        