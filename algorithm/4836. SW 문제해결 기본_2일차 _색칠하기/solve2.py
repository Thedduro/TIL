import sys
sys.stdin = open('sample_input.txt','r')
# 일단 각 시작 위치와 끝 위치의 모든 좌표 리스트를 반환한 후
# 그 좌표의 겹치는 부분을 보라색으로 간주한 후 계산한다

def find(paint):
    red = []
    blue =[]

    for p in paint:
        start_i, start_j, end_i, end_j, color = p[0], p[1], p[2], p[3], p[4]
        for i in range(start_i, end_i+1):
            for j in range(start_j, end_j+1):
                if color == 1:
                    red.append((i,j))
                elif color == 2:
                    blue.append((i,j))
    return red, blue



T = int(input())

for tc in range(1, T+1):
    N = int(input()) # 색칠할 영역 개수

    paint  = [list(map(int, input().split())) for _ in range(N)]

    red_lst, blue_lst = find(paint)

    pupple = []
    for r in red_lst:
        if r in blue_lst:
            pupple.append(r)

    print(len(pupple))