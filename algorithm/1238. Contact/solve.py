import sys
sys.stdin = open('input.txt', 'r')
from collections import deque

def solve(start_node):
    visited = set()
    queue = deque()
    queue.append((start_node, 0))
    visited.add(start_node) # 연락 받은 노드 번호 저장

    max_depth = 0
    result_nodes = []

    while queue:
        node, depth = queue.popleft()
        child = contact.get(node)
        
        if depth > max_depth: # 딥스가 하나 더 깊어 졌을때
            max_depth = depth
            result_nodes = [node] # 초기화 한다
        if depth == max_depth: # 같은 부모에게서 연락을 받은 자식일때
            result_nodes.append(node) # 추가한다

        if child:
            for next in child: # 연락받을 수 있는 자식들
                if next not in visited: # 방문 안했을 때만
                    visited.add(next) 
                    queue.append((next, depth + 1))

    return max(result_nodes) # 가장 깊은 딥스 중 가장 큰 노드 번호 반환

for tc in range(1, 11):
    len_data, start_node = map(int, input().split())
    data = list(map(int, input().split()))

    contact = {data[i]: [] for i in range(0,len(data),2)}
    for i in range(0, len(data), 2):
        contact[data[i]].append(data[i+1])
        # {100: [17, 8, 7], 39: [22], 7: [100], 2: [7, 15], 15: [4], 6: [2], 11: [6], 4: [10, 2]}

    print(f'#{tc}', solve(start_node))