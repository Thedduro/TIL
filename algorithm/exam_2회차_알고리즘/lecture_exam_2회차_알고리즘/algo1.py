import sys
sys.stdin = open('algo1_sample_in.txt')

T = int(input())

for tc in range(1, T+1):
    # 물품의 종류
    N = int(input())
    # 물건개수, 시간, 가치
    data = [list(map(int, input().split())) for _ in range(N)]
    # 물품의 개수
    I = int(input())
    # 재료별 시간
    items = list(map(int, input().split()))
    # print(data, J)
    result = 0      # 최종 결괏값
    # 모든 경우에 대해
    for i in range(1 << I):
        cnt = 0     # 사용한 개수
        time = 0    # 소요된 시간
        for j in range(I):  # j번쨰 요소를 더한 부분집합
            if i & (1 << j):
                cnt += 1
                time += items[j]
        # 다 더한 결과를 토대로 모든 상품 탐색
        for product in data:
            if result < product[2]:  # 최대 상품 가치 업데이트
                # 사용한 개수와 시간이 일치하면
                if cnt == product[0] and time == product[1]:
                    result = product[2]
    print(f'#{tc} {result}')