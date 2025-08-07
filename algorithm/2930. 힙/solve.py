import sys
import heapq
sys.stdin = open("sample_input.txt", "r")

def make_max_heap(heap, item):
    parts = item.split(' ')

    if parts[0] == '1':
        heapq.heappush(heap, - int(parts[1])) # x를 삽입
        return None
    
    if len(heap) > 0 and parts[0] == '2':
        return - heapq.heappop(heap) # 최대 힙의 루트 출력 및 삭제
    
    if len(heap) == 0: # 힙이 비어있으면 -1 출력
        return -1
    

T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 수행해야하는 연산 횟수
    operation = [input() for _ in range(N)] # 연산 정보

    heap = [] # heap

    result = []
    for i in operation:
        res = make_max_heap(heap, i)
        if res is not None: # 삽입한 경우 none을 리턴, 연산 2의 경우에만 리스트 추가
            result.append(res)
    
    print(f'#{tc}', *result) # 리스트의 각 요소를 꺼내서 공백 구분 출력
