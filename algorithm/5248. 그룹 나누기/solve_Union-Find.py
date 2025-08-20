import sys
sys.stdin =  open('sample_input.txt', 'r')

def find_set(arr, i):
    if arr[i] != i: # 자기 자신이 아니야
        arr[i] = find_set(arr, arr[i]) # 더 상위의 부모를 찾아
    return arr[i] # 최상단 루트 노드를 찾음

def union(arr, x, y):
    root_x = find_set(arr, x)
    root_y = find_set(arr, y)

    if root_x < root_y:
        arr[root_y] = root_x # 그룹에 속하게
    else:
        arr[root_x] = root_y

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    arr = [i for i in range(N+1)]

    for i in range(0, len(lst), 2):
        x = lst[i]
        y = lst[i+1]

        union(arr, x, y)

    groups = set(find_set(arr, i) for i in range(1, N+1)) # 최상단 노드를 찾음 ex) 2,2,2,2 > 중복 제거 되니까 하나의 그룹으로 
    print(f"#{tc} {len(groups)}")