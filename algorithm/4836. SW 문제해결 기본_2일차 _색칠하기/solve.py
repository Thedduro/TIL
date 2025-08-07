import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())

def find(paint):
    # 같은 색이 여러번 나올 경우 인덱스의 중복을 저장할 필요 없음 > set
    red = set() 
    blue = set()

    for row in paint: # 각 영역의 색칠 정보 가져오기
        start = row[0:2] # 시작인덱스
        end = row[2:4] # 끝인데스
        color = row[4] # 컬러 정보 1:red, 2:blue

        for i in range(start[0], end[0] + 1): # row 인덱스
            for j in range(start[1], end[1] + 1): # col 인덱스
                if color == 1:
                    red.add((i,j)) 
                else:
                    blue.add((i,j))
    return red, blue

for tc in range(1, T+1):
    N = int(input()) # 색칠할 영역 개수

    paint  = [list(map(int, input().split())) for _ in range(N)]
    red, blue = find(paint) # 각 색깔의 색칠 영역

    pupple = [] # 보라색 영역을 저장
    
    # 교집합 찾기 > 어차피 하나만 반복하면서 다른 집합에 있는 것들만 저장하면 됨
    for r in red:
        if r in blue: # 다른 집합에 들어있으면? > 추가
            pupple.append(r)

    print(f'#{tc} {len(pupple)}')
