import sys
sys.stdin = open('sample_input.txt','r')

direction = [(-1,0),(1,0),(0,-1),(0,1)]
reverse_dir = {1: 2, 2: 1, 3: 4, 4: 3}

def merge(lst): 
    merged = {}

    for x, y, cnt, dir in lst:
        if (x,y) not in merged:
            merged[(x,y)] = [(cnt,dir)]
        else:
            merged[(x,y)].append((cnt,dir))
    
    next_lst = []
    
    for (x, y), value in merged.items():
        if len(value) == 1:
            next_lst.append([x, y, value[0][0], value[0][1]])
        else:
            cnt = sum(v[0] for v in value)
            max_cnt, max_dir = max(value, key=lambda v: v[0])
            next_lst.append([x,y,cnt,max_dir])
    
    return next_lst

def solve(time, lst):
    while time <= M:
        for i, micro in enumerate(lst):
            x, y = micro[0],micro[1]
            cnt, dir = micro[2],micro[3]
            nx , ny = x + direction[dir-1][0], y + direction[dir-1][1]
            if nx == 0 or nx == N-1 or ny == 0 or ny == N-1: # 격리 구간에 닿으면,
                cnt = cnt // 2
                dir = reverse_dir[dir]
            lst[i] = [nx, ny, cnt, dir]

        lst = [micro for micro in lst if micro[2] > 0] # 미생물 수가 0일때, 제거
        time += 1
        lst = merge(lst)
    return lst        

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(K)] # 세로 위치, 가로 위치, 미생물 수, 이동 방향
    
    result_lst = solve(1,lst)
    result = sum(x[2] for x in result_lst)
    
    print(f'#{tc}', result)