import sys
sys.stdin = open('sample_input.txt','r')
from collections import deque

def find(pizza):
    result = [0 * N] # 고정된 길이를 가지는 화덕

    while pizza:
        for i in range(N): # 화덕의 크기 만큼 반복
            result[i] = pizza[i]
            pizza.popleft()

        result[:][1] //= 2 # 치즈의 양은 절반이 줄어들어

        if 0 in result[:][1]:
            
        return result
    
    
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    pizza = deque() # 피자 번호, 치즈 함께 담을 리스트
    for i in range(1, M+1):
        pizza.append((i, lst[i-1]))

    print(find(pizza))