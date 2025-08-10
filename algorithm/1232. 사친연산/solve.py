import sys
sys.stdin = open('input.txt', 'r')

def dfs(node):
    value = tree[node][0]

    if value in ['+', '-', '/', '*']: # 부모 노드라면
        left = dfs(tree[node][1]) # 왼쪽 자식 재귀
        right = dfs(tree[node][2]) # 오른쪽 자식 재귀

        if value == '+':
            return left + right
        if value == '-':
            return left - right
        if value == '/':
            return left / right
        if value == '*':
            return left * right
    else: # 리프 노드라면
        return int(value) # 값을 반환


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)

    for _ in range(N):
        data = input().split()
        idx = int(data[0])
        if data[1] in '+-*/':  # 연산자 노드
            tree[idx] = [data[1], int(data[2]), int(data[3])]
        else:  # 숫자 노드
            tree[idx] = [data[1]]

    print(f'#{tc}', int(dfs(1)))