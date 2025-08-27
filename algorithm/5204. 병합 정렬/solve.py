import sys
sys.stdin = open('sample_input.txt', 'r')

'''
    pop(0) -> O(n)의 시간 복잡도를 가짐
    ---제한시간 초과로 fail
    > 데크로 구현하여 popleft() -> O(1)의 시간복잡도
'''

from collections import deque

def merge_sort(arr):
    n = len(arr)

    if n <= 1:
        return arr
    
    mid = n//2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    global cnt 
    result = []

    if left[-1] > right[-1]:
        cnt += 1

    left, right = deque(left), deque(right)

    while left and right:
        if left[0] < right[0]:
            result.append(left.popleft())
        else:
            result.append(right.popleft())
    
    result.extend(left)
    result.extend(right)

    return result

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    cnt = 0
    result = merge_sort(arr)

    print(f'#{tc}', result[N//2], cnt)


