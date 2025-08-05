import sys
sys.stdin = open('input.txt')

from itertools import combinations

T = int(input())

def get_value(lst): # 리스트를 연결해서 정수형으로 만들어줌
    return int(''.join(map(str, lst)))

def exchange_dfs(arr, idx): # 한번만 교환해서 최대값을 찾자
    visited = [False] * len(arr)
    current_value = get_value(arr[idx] + arr[idx+1:])

    for i in range():
        exchange_dfs( ,idx+1)

        



for tc in range(1,T+1):
    number_map, cnt = map(int, input().split())
    number_map = list(map(int, str(number_map))) # 각 요소를 담은 리스트로 변환

    for _ in range(cnt): # 반복 횟수
        value = exchange_dfs(number_map, 0) # 현재의 arr로 찾은 최대값
        if max_value < value:
            max_value = value
        


