import sys
sys.stdin = open("input.txt")

def dfs(idx, total): # 현재 탐색 중 점원의 인덱스, 지금까지 선택한 점원들의 키
    global min_height

    if total >= min_height: # 아직 점원이 남았어도 넘으면 다음을 더할 필요성이 없음 > 시간 최적화
        return 
    
    if idx == N: # idx가 얼마가 되면 종료 조건(n이 될때까지)
        if total >= B:
            min_height = min(min_height, total)
        return  
    
    # 아직 모든 점원에 대해 탐색 안함
    dfs(idx+1, total +  arr[idx])
    dfs(idx+1, total) # 이번 점원의 키는 더하지 않아 

T = int(input())
for tc in range(1, T + 1):
    # N: 사람 수, B: 목표 높이
    N, B = map(int, input().split())
    # 각 사람의 키를 입력 받아 리스트로 저장
    arr = list(map(int, input().split()))

    # 직원당 키는 최대 10000이므로, 최대 높이는 10000 * N
    min_height = 10000 * N 

    dfs(0, 0)

    # 목표 높이 B를 빼서 실제로 초과된 부분만 출력
    print(f"#{tc} {min_height - B}")

