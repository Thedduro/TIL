import sys
sys.stdin = open('sample_input.txt', 'r')
"""
    - 공격받으면, 메일밤 지정된 수의 소를 잃음
    - 수리는 다 끝날때까지 1개만 가능
    - 어떤 순서로 외양간을 고쳐야 피해 최소?
    idea 1. 그냥 조합 쓰면 되는거 아님?
        -  
    idea 2. 그리디하게 풀어보자.
        - 
"""

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    demage = [list(map(int, input().split())) for _ in range(N)]
    attacked = [int(input()) for _ in range(M)]

    print(demage) # [[10, 2], [8, 1], [5, 1]]
    print(attacked) # [2, 1, 3]