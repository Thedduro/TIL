import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M, K = map(int, input().split())

    # 최종 결괏값
    min_score = float('inf')

    # 만들 수 있는 최대 연속된 수
    max_combos = M // K

    '''
        최소점수를 만들려면?
        최대한 연속된 수를 없애도록 쪼개야 한다.
        그럼 최소한 만들어야 하는 연속된 수의 개수를 구하고,
        틀린 문제 개수를 사용해서, 남은 문제들을 쪼갤 수 있도록한다.
    '''

    # c : 초반에 연속으로 만들 연속된 수의 개수
    for c in range(max_combos + 1):
        # c개의 연속된 수를 만들고 남은 맞힌 문제의 수
        m_rem = M - c * K       # K번 연속된 만큼 c * K
        # 사용할 수 있는 틀린 문제의 수
        incorrect = N - M
        separators = 0
        if m_rem > 0:
            # 남은 문제들을 K-1개 이하의 묶음으로 나누려면
            # 몇 개의 칸막이가 필요한지 계산
            num_groups = (m_rem + (K - 1) - 1) // (K - 1)
            separators = num_groups - 1

        # 가진 칸막이로 나눌 수 있는지 확인
        if incorrect >= separators:
            # c번 연속되었을 때 얻는 점수 계산
            score = 0
            for _ in range(c):
                # 연속될 때마다 점수 (1점씩 K번 더하고) * 2
                score = (score + K) * 2
            total_score = score + m_rem

            # 최솟값 갱신
            min_score = min(min_score, total_score)

    print(f'#{tc} {min_score}')