import sys
sys.stdin = open('sample_input.txt')

def find(current_idx):
    global result 
    
    while current_idx < N: # 현재 위치가 종점보다 작을 때
        next_idx = current_idx + K

        if next_idx >= N:
            break
        
        
        found = False
        for i in range(next_idx, current_idx, -1):
            if i in charge_stations:
                next_idx = i
                result += 1
                found = True
                break

        if not found:
            return 0
        
        current_idx = next_idx

    return result 

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())

    charge_stations = list(map(int, input().split()))

    result = 0
    current_idx = 0
 
  
    print(f'#{tc}', find(current_idx))