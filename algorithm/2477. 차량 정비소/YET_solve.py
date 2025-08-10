import sys
sys.stdin = open('sample_input.txt', 'r')

def solve(lst):
    result = 0 # 고객번호의 합을 담을

    for _ in range(K):
        customer = lst.pop(0)

        n, value = reception_time.pop(0) 
        customer[1] = n # 접수창고 번호 저장
        customer[3] += value # 접수창고 시간 증가
        reception_time.append([n, value])

        m, value = repair_time.pop(0) 
        customer[2] = m # 수리창고 번호 저장
        customer[3] += value # 수리창고 시간 증가
        repair_time.append([m, value])

        lst.append(customer)

    return lst



T = int(input())

for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())

    reception_time = list(map(int, input().split())) 
    repair_time = list(map(int, input().split()))

    in_time = list(map(int, input().split()))

    reception_time = [[n, r] for n, r in zip(range(1, N+1), reception_time)] # 접수 창고 번호와 시간
    repair_time = [[m, r] for m, r in zip(range(1, M+1), repair_time)] # 수리 창고 번호와 시간
    lst = [[k, 0, 0, t] for k, t in zip(range(1, K+1), in_time)] # 고객번호, 접수창고, 수리창고, time 담을 리스트 
    

    
    print(f'#{tc}', solve(lst))