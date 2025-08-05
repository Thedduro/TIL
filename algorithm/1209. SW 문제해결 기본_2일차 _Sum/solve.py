import sys

sys.stdin = open("input.txt", "r")

for _ in range(10): # 10개의 테스트케이스 반복
    test_case = input()
    map_lst = [list(map(int, input().split())) for _ in range(100)] # 100x100 배열 생성

    # 각 행의 합 구하기
    max_sum_row = 0 # 각 행의 합 중에 가장 큰 값 저장 변수
    for row in map_lst:
        sum_row = sum(row)
        if max_sum_row < sum_row: # 해당 행의 합이 더 크면 max 값을 바꿔줌
            max_sum_row = sum_row 
    
    # 각 열의 합 구하기
    max_sum_col = 0
    for i in range(100): 
        sum_col = 0
        for j in range(100):
            sum_col += map_lst[j][i] # [0~99][0], [0~99][1]... > 열의 합
        if sum_col > max_sum_col: # 해당 열의 합이 더 크면 max 값을 바꿔줌
            max_sum_col = sum_col

    # 대각선의 합 구하기
    sum_dia_r = 0
    sum_dia_l = 0
    for dia in range(100):
        sum_dia_r += map_lst[dia][dia] # 오른쪽 대각선

        temp_idx = -dia -1 # -1, -2, -3 .... > 인덱스 구현
        sum_dia_l += map_lst[dia][temp_idx] # 왼쪽 대각선
    
    max_dia = max(sum_dia_r,sum_dia_l)
        

    print(f'#{test_case} {max(max_sum_row, max_sum_col, max_dia)}')
