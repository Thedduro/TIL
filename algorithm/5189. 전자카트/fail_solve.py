import sys
sys.stdin = open("sample_input.txt", "r")

def findinganswertobacktracking(start,  current_value): # 백트래킹을 활용한 DFS 구현
    global min_value, cnt
    
    # if cnt == N: # 만약 반복횟수를 넘으면 > 중단
    #     return min_value

    if current_value > min_value: # promissing이 아닌것 같으면? 부모 노드로 돌아감
        return # 더 이상의 조사 의미 x
    
    print('사실상 min_value 죠>', current_value)
    
    for child in range(N):
        num = operation[start][child]

        if num != 0:
            current_value += num
            min_value = min(current_value, min_value)
            print(start, child, min_value)
            findinganswertobacktracking(child, min_value) # 자식 노드 탐색 후 더해
    cnt += 1

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 수행해야하는 연산 횟수
    operation = [list(map(int, input().split())) for _ in range(N)] # 연산 정보
    
    cnt = 1
    min_value = float('inf')

    print(f'#{tc} {findinganswertobacktracking(start = 1,  current_value = 0)}')