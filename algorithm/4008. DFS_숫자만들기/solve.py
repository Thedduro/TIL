import sys
sys.stdin = open('sample_input.txt')


def get_value(pre, next, op): # 연산자의 종류에 따른 값 계산
    if op == 0:
        return pre + next
    if op == 1:
        return pre - next    
    if op == 2:
        return pre * next
    else:
        return int(pre / next) # 나눗셈할때 소수점 이하는 버린다
    
def dfs(value, operator, idx):
    global max_value, min_value # 전역변수로 설정
 
    if idx == N: # idx가 마지막 원소일때 > 다음 dfs를 실행하지 않음
        max_value = max(value, max_value)
        min_value = min(value, min_value)
        return 

    for op in range(4):
        if operator[op] > 0: # 0이 아닐때만, 해당 연산자 실행
            operator[op] -= 1 # 해당 연산자를 사용했으니까 > 한번 줄여주기

            new_value = get_value(value, number[idx], op) # 지금 값이랑 다음 값을 계산
            dfs(new_value, operator, idx+1) # 재귀함수 >

            operator[op] += 1 # 백트래킹 구현 > 다음 인덱스의 연산자 먼저 시작하는 로직

T = int(input())

for tc in range(1,T+1):
    N =  int(input())
    operator = list(map(int, input().split())) # 연산자의 개수를 담은 리스트
    number = list(map(int, input().split())) # 수식에 사용되는 숫자

    max_value, min_value = -100000000, 100000000 # 수의 최대최소 제약사항

    dfs(number[0], operator, 1)
    print(f'#{tc} {max_value-min_value}')