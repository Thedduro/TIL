import sys
sys.stdin = open('input.txt', 'r')

def find_common(node):
    result = []

    while True:
        if node == 1:
            break

        parent_node = parent[node] # 저장되어있는 부모 노드 번호를 더함
        result.append(parent_node)

        node = parent_node # 그 부모 노드를 현재 node로 바꿔 > 조상 노드 찾음

    return result

def find_child(node):
    global cnt

    child_node = child[node]
    
    if not child_node: # 자식 노드가 없으면
        return
    
    for i in range(len(child_node)):
        cnt += 1 # 자식 노드 개수만큼 증가
        find_child(child_node[i]) # 재귀 함수 호출


T = int(input())

for tc in range(1, T+1):
    V, E, node1, node2 = map(int, input().split())
    data = list(map(int, input().split()))
    
    parent = [None] * (V+1)
    child = {i: [] for i in range(1, V+1)}

    # 각 노드의 부모 노드를 저장
    for i in range(0, len(data), 2):
        parent[data[i+1]] = data[i] # 자식 노드 인덱스에 부모 노드의 정보를 저장
        child[data[i]].append(data[i+1]) # 부모노드 key에 자식노드 번호를 저장
        
    node1_parent, node2_parent = find_common(node1), find_common(node2) # 각각의 부모 노드 추출
    for x in node1_parent:
        if x in node2_parent:
            common_parent = x
            break
    # common_parent = max([x for x in node1_parent if x in node2_parent]) # 공통 부모 중 번호가 가장 높은 것(가장 가까운)

    cnt = 1
    find_child(common_parent)

    print(f'#{tc}', common_parent, cnt)