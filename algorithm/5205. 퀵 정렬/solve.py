import sys
sys.stdin = open('sample_input.txt', 'r')
'''
    퀵 정렬이란? 기준 점을 중심으로 작으면 왼편, 큰건 오른편에 위치하여 정렬하는 알고리즘
'''

def quick_sort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)

        quick_sort(arr, start, pivot-1)
        quick_sort(arr, pivot+1, end)

def partition(arr, start, end):
    pivot = arr[start]
    left = start + 1
    right = end

    while True:
        while left <= end and arr[left] < pivot: # left는 왼쪽부터 오른쪽으로 가며 피벗보다 큰 값을 찾음
            left += 1
        while right > start and arr[right] >= pivot: # right는 오른쪽부터 왼쪽으로 가며 피벗보다 작은 값을 찾음
            right -= 1
        
        if left < right: # 교차 x > arr[left]가 피벗보다 크고, arr[right]가 피벗보다 작기 때문에 둘을 바꿔야 함
            arr[left], arr[right] = arr[right],arr[left]
        else: # 교차하면 중단하고, 아래 로직 수행
            break

    # left >= right이 되면, pivot 보다 값이 작은 right와 순서 바꿔줌
    arr[start], arr[right] = arr[right], arr[start]
    
    return right


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    quick_sort(arr, 0, N-1)
    print(f'#{tc}', arr[N//2])

