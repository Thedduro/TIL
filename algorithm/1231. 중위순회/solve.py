import sys
sys.stdin = open('input.txt', 'r')

def dfs(node):
    global word

    alpha = tree[node][0]

    if len(tree[node]) == 3: # 부모노드라면(왼, 오)
        left = tree[node][1]
        right = tree[node][2]

        dfs(left)
        word += alpha
        dfs(right)

    elif len(tree[node]) == 2: # 부모노드인데 > 왼쪽 자식 ㄱ밖에 없음
        left = tree[node][1]
        dfs(left)
        word += alpha

    else: 
        word += alpha


for tc in range(1, 11):
    N = int(input())
    tree = [0] * (N+1)

    for _ in range(N):
        data = input().split()
        if len(data) == 4:
            tree[int(data[0])] = [data[1], int(data[2]), int(data[3])]
        elif len(data) == 3:
            tree[int(data[0])] = [data[1], int(data[2])]
        else:
            tree[int(data[0])] = [data[1]]

    word = ''
    dfs(1)

    print(f'#{tc}', word)