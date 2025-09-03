import sys
sys.stdin = open('sample_input.txt', 'r')
# from itertools import permutations

def solve(tree_lst, idx, day):
    global min_day

    current_lst = tree_lst[:]

    # BASE_CASE
    if idx >= len(tree_lst):
        return
    if min_day <= day:
        return

    if current_lst[idx] > target:
        return

    if day % 2 == 0 and day != 0: # 짝수 날
        current_lst[idx] += 2
    elif day % 2 == 1: # 홀수 날
        current_lst[idx] += 1

    if current_lst.count(target) == len(tree_lst): # 모든 트리가 최대 높이가 되면
        min_day = min(day, min_day)
        return

    if current_lst[idx] > target:
        return

    for i in range(len(tree_lst)):
        solve(current_lst, idx+i, day+1)
        solve(current_lst, idx+i, day+2)


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    tree = list(map(int, input().split()))
    target = max(tree)

    tree_lst = []
    for i in range(len(tree)): # 최대 키를 가진 트리 제거
        if tree[i] != target:
            tree_lst.append(tree[i])

    if len(tree_lst) == 0: # 모든 요소가 최대 높이면
        print(f'#{tc}', 0)
        continue

    min_day = float('INF')
    tree_lst.sort(reverse=True)
    solve(tree_lst, 0, 0)

    print(f'#{tc}', min_day)