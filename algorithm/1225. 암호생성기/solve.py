import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def solve(lst):
    while True:
        for decrease in range(1, 6): # -1,-2....-5까지 반복 > 1 cycle
            value = lst.popleft() - decrease # 감소 후 뒤에 저장될 값
            
            if value <= 0: # 0 이하가 되면 > 0을 저장하고 종료
                lst.append(0)
                return lst
            else: # 0 이하가 아니면 계속 
                lst.append(value)


for tc in range(1, 11): # 10개의 테스트케이스
    tc = int(input())
    lst = deque(map(int, input().split()))

    result = list(solve(lst))
    print(f'#{tc}', *result)
