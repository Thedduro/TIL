import sys
sys.stdin = open('sample_input.txt','r')

# 약품에 닿으면, 절반 감소 > 방향 반대로 바뀜
# 수가 0이되면 군집이 사라짐
# 군집 두개가 한셀에 모이면 군집이 합쳐짐, 이동방향은 군집이 더 큰 군집꺼
# 시간이 지난 후 남아있는 미생물 수 총합

direction = [(1,0),(-1,0),(0,-1),(0,1)]

def merge(lst): 
    '''
    1시간마다 같은 셀에 있는 군집을 찾고 병합, 방향 수정해서 리턴한다.
    그러면 모든 군집의 리스트를 받고 처리 > 리스트 반환
    어떻게?
    for문으로 하나씩 돌면서 안에 같은 위치가 있으면 병합 후 그 군집과 병합
    '''
    next_lst = []

    for i in range(K-1):
        x1, y1, cnt1, dir1= lst[i][0], lst[i][1], lst[i][2], lst[i][3]
        for j in range(i+1, K):
            x2, y2, cnt2, dir2 = lst[j][0], lst[j][1], lst[j][2], lst[j][3]
            if x1==x2 and y1==y2:
                cnt = cnt
                if cnt1 < cnt2:
                    dir = dir2
                else:
                    dir = dir1
            next_lst.appned([x1, x2, cnt, dir])

def solve(time):
    while time < M:
        for i in range(K):
            x, y, cnt, dir = lst[i][0], lst[i][1], lst[i][2], lst[i][3]
            nx, ny = x + direction[dir-1][0], y + direction[dir-1][1]
            if nx == 
            print(nx, ny)

T = int(input())

for tc in range(1, 11):
    N, M, K = map(int, input().split())

    lst = [list(map(int, input().split())) for _ in range(K)] # 세로 위치, 가로 위치, 미생물 수, 이동 방향

    print(solve(1))