import sys
sys.stdin = open('sample_input.txt','r')

def find(pizza):
    fire = pizza[:N]
    res = pizza[N:]

    while len(fire) > 1: # 2개 이상 남아있을 때 까지 반복
        cheese = fire.pop(0) # 1번 위치에 있는 피자 일단 꺼내
        if cheese[1]//2 != 0: # 치즈가 녹아ㅏ > 0이 아니면
            fire.append((cheese[0],cheese[1]//2))
        else: # 치즈가 0이 됐어?
            if res: # 남아있는 피자가 있으면
                fire.append((res.pop(0)))
    return fire 


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    pizza = [] # 피자 번호, 치즈 함께 담을 리스트
    for i in range(1, M+1):
        pizza.append((i, lst[i-1]))

    result = find(pizza)
    print(f'#{tc} {result[0][0]}')