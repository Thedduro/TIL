import sys
sys.stdin = open('input.txt', 'r')

def find(j):
    stack =[] # 1줄의 교착 상태 자석을 담을 스택
    cnt = 0 

    arr = [table[i][j] for i in range(N) if table[i][j] != 0]

    for magnetic in arr:
        if magnetic == 1: # 붉은색
            stack.append(magnetic)
        elif magnetic == 2: # 푸른색
            if stack: # 스택에 붉은색이 있을 때만
                stack = [] # 스택 초기화
                cnt += 1

    return cnt

    # while arr and arr[0] == 2: # 맨 위에 B가 있으면, 어차피 위로 빠짐
    #     arr = arr[1:]
    # while arr and arr[-1] == 1: # 맨 아래에 R이 있으면, 어차피 아래로 빠짐
    #     arr = arr[:-1]
    # return len(arr)


for tc in range(1, 11):
    N = int(input()) # 100을 입력받음 > 100*100 행렬

    table = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0

    for j in range(N):
        result += find(j) # 1줄씩 교착상태 개수 구하기

    print(f'#{tc}', result)