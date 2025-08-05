import sys
sys.stdin = open('input.txt')

def combination(arr, r):
    result = []
    if r == 1: # 선택할 요소가 1개만 남은 경우 리턴
        return [[i] for i in arr] # 남아 있는 arr의 모든 값들을 배열로 조합
    
    for idx in range(len(arr)):
        elem = arr[idx]
        for rest in combination(arr[idx + 1], r-1):
            result.append([elem] + rest)

    return result

T = int(input())

for tc in range(1, T+1):
    N, B = map(int,input()) # N=점원의 수, B=목표탑의 높이
    data = list(map(int, input().split))

    # 직원당 최대 키 10000 * 최대 직원수 20
    min_height = 10000 * N

    for r in range(1, N+1):
        for comb in combination(data, r):
            total =  sum(comb)

            if total >= B: # 최종 조검: 선반보다는 키의 합이 커야함
                min_height = min(min_height, total)

    print(f'#{tc} {min_height - B}') 