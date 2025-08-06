import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    field = [list(map(int, input())) for _ in range(N)] # N줄의 숫자를 받아 2차원 리스트 행렬 생성

    result_sum = 0

    for i in range(N): # 모든 행 탐색

        if i <= N//2: # 위의 상단 부분 & 중간 부분
                # i가 증가할수록 더해지는 범위가 넓어짐
                # 예: N=5일 때, i=0 → 가운데 하나만 (2), i=1 → 1~3 (3개), i=2 → 0~4 (5개)
                start = (N//2) - i               # 가운데에서 i만큼 왼쪽으로
                end = (N//2) + i + 1             # 가운데에서 i만큼 오른쪽까지 포함 (슬라이싱은 끝 인덱스 +1)
                
                result_sum += sum(field[i][start:end])
        
        if i > N//2: # 하단 부분
                # i가 증가할수록 더해지는 범위가 다시 좁아짐
                # 예: N=5일 때, i=3 → 1~3 (3개), i=4 → 2~2 (1개)
                start =  (N//2) + i - (N+1)
                end = (N//2) - (i-N)
                result_sum += sum(field[i][start:end])

    print(f'#{tc} {result_sum}')

    # for i in range(N): # 모든 행 탐색
    #     if i <= N//2: # 위의 절반의 행 > 
    #         for z in range(0, N, 2): # 열: 끝점 > 시작점에서 얼마나? > 1, 3, 5......
    #             for j in range(N//2, 0, -1): # 열: 시작점 > 중간~첫번째 거꾸로 탐색
    #                 print(i, j+z)
    #                 sum += field[i][j+z]
        
    #     if i >  N//2: # 아래 절반 행 
    #         for j in range(0, N//2, -1): # 열에 대해서는 중간~첫번째 까지 시작점 거꾸로 탐색
    #             sum += field[i][j]