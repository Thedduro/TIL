import sys
sys.stdin = open('sample_input.txt', 'r')

def dfs(node):
    global value 
     
    if node * 2 <= N:
        dfs(node * 2) # 왼쪽 자식
    
    tree[node] = value
    value += 1

    if node * 2 + 1 <= N:
        dfs(node * 2 + 1)


T = int(input())

for tc in range(1, T+1):
    N = int(input())

    tree = [0] * (N+1)
    value = 1

    dfs(1)
    print(f'#{tc}', tree[1], tree[N//2])