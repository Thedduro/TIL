import sys

sys.stdin = open("sample_input.txt", "r")

# 자식 노드 번호 : 현재 노드 번호 (*2, *2+1)
T = int(input()) 

# 부모 노드의 값 : 왼쪽 노드 /2, (오른쪽 자식 노드 -1)/2
for t in range(1, T+1):
    N, M, L = map(int, input().split())
    
    lst = [0] * (N+1) # 노드 번호 인덱스에 값을 저장할 리스트 생성

    for _ in range(M):
        node_num, value = map(int, input().split())
        lst[node_num] = value # 주어진 노드 번호 인덱스에 값 저장

    def get_node_value(target):
        if target >= len(lst): return 0 # base케이스 설정해주기 > target이 인덱스를 넘어가게 되면 0을 더하게

        if lst[target] == 0:
            return get_node_value(target*2) + get_node_value(target*2+1) # 왼쪽 노드 더하기 오른쪽노드
        
        else: # 타겟 값이 있으면 리턴
            return lst[target]
        
    print(f'#{t} {get_node_value(L)}')