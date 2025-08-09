import sys
sys.stdin = open('sample_input.txt', 'r')
from itertools import combinations

# 식재료들을 조합하여 나오는 합
def find(food):
    sum = 0

    # 음식의 식재료 배열에서 두개만 고르는 조합 만들어서 합을 구함
    for i, j in combinations(food, 2):
        sum += S[i][j] + S[j][i] 

    return sum

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    S = [list(map(int, input().split())) for _ in range(N)]

    result = float('inf')
    arr = [n for n in range(N)]

    for case in combinations(arr, N//2): # 우선 하나의 음식 식재료 조합을 만들어
        remain = list(set(arr) - set(case)) # set을 이용해서 나머지 음식 조합을 구함
        temp_value = abs(find(case) - find(remain)) # 두 음식의 맛의 차이를 구함
        
        if result > temp_value:
            result = temp_value
    
    print(f'#{tc} {result}')


# #  음식 조합의 순열 구하기
# for i in range(N):ç
#     for j in range(i+1, N+1):
#         comb.append([i,j])

    