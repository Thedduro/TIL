import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    # 각 사람의 키를 입력 받아 리스트로 저장
    arr = list(map(int, input().split()))

    # 직원당 키는 최대 10000이므로, 최대 높이는 10000 * N
    min_height = 10000 * N 

    subset_cnt = 2 ** N # 부분 집합의 모든 경우의 수
    for i in range(1, subset_cnt):
        h_sum = 0
        for j in range(N): # j번째 요소가 선택되었는지 확인
            # 각 부분 집합
            if i & (1 << j): # i번째 경우의 수에 j요소 선택 확인
                h_sum += arr[j]

        if h_sum >= B:
            min_height = min(min_height, h_sum)

    # 목표 높이 B를 빼서 실제로 초과된 부분만 출력
    print(f"#{tc} {min_height - B}")

    # 조합을 직접 구한거 보다 빨라짐 > 왜? > comb는 조합에 대해 계속 재귀를 구함
    # 이진탐색 방식으로 비트 방식으로 처리, 다 해봤자 2의n승 밖에 안함