import sys
sys.stdin = open('input.txt')

def check():
    '''
        오로지, 시험 통과 가능 여부만 본다.
        1. 세로로 순회 즉, 평소와 x, y가 순서가 바껴야한다.
        2. 이번 열을 조사하면서, 몇번 시험에 통과했는지 체크
        3. 시험 통과한 횟수가 K가면되면 다음 열로 넘어가야한다.
    '''
    for c in range(W):
        cnt = 1
        is_possible = False
        for r in range(1, D):
            # 내 값이 이전값이랑 같으면
            if data[r][c] == data[r-1][c]:
                cnt += 1    # 누적 1 증가
            else:           # 다르면
                cnt = 1     # 1로 초기화

            if cnt >= K:
                is_possible = True
                break
        # 이번 c에 대해서 모든 r을 조사했지만
        # 어젼히 is_possible 하지 못하면? 조사 의미없다.
        # if not is_possible:
        #     return False
            '''
                for ~else: 는
                for문 내부에서 break 된적 없이 종료되었을때
                실행
            '''
        else:
            return False
    return True



def search(row_idx, acc_count):
# def search(row_idx, acc_count, type):
    '''
        :param row_idx: 몇 번째 행에 약물 투여 여부
        :param acc_count: 지금까지 몇번 약물을 투약했는지를 센다.
    '''
    global result   # 최소 약물 투여 횟수
    # print(row_idx, type)
    # 그럼.. 내가 row_idx번째를 조사하고 있든 말든...
    # 남아 있는 두께가 있든 말든.... 더 조사하는 의미가 없다!
    # ---- 가지치기 ---- 유망성 없음.
    if acc_count >= result: return
    '''1. 규칙
        0번째 행에 약물을 `안넣기` `A넣기` `B넣기` 할 수 있음.
        이걸 최대 K번 할 수 있음.

        단, 모든 경우의수를 다 고려 해야함.
                안넣기 A 넣기 B넣기
            0     0      1      0
            1     0      0      1
            2
            3
            D
    '''

    # ---- 기저 조건 -------
    if row_idx == D:
        # 모든 경우 다 시도해본 뒤, 어쨋든 D까지 도달한 시점
        # 이번 회차.... 통과 가능합니까?
        # print(data)
        if check(): # 통과했다면 True 반환했을것
            result = min(result, acc_count)
        return

    # ---- 유도 조건 -----
    # 이번 회차는? 모르겠고 일단 다음 회차를 만드는법?
    # row_idx가 1증가한다 -> 다음 행에 대해 조사하러 가겠다.
    # 1. 약 안넣기
        # - acc_count가 안늘어나면된다.
    search(row_idx+1, acc_count)
    # 잠깐... 약 넣기 전에 원본좀 채취해 둘게요
    origin_row = data[row_idx][:]

    # 2. A 약 넣기
        # - acc_count가 늘어나면된다.
    data[row_idx] = [0] * W
    search(row_idx + 1, acc_count+1)
    # 2. B 약 넣기
        # - acc_count가 늘어나면된다.
    data[row_idx] = [1] * W
    search(row_idx + 1, acc_count + 1)

    # 여기까지 돌아올때까지 origin_row는
    # local 영역에 잘 살아있다.
    # 데이터 원복
    data[row_idx] = origin_row

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    data = [list(map(int, input().split())) for _ in range(D)]
    # 최종 결괏값을 초기에 세팅할때는 무엇으로 해야 할까?
    result = K  # 문제를 가장 바보같이 해결했을때의 결괏값
    # 아마 어떠한 함수를 통해서 문제 해결
    search(0, 0)
    # search(0, 0, None)    # 무슨 인자? 필요한지 아직 모르겠다.
    print(f'#{tc} {result}')
