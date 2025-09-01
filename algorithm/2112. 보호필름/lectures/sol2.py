import sys
sys.stdin = open('input.txt')

from itertools import combinations, product

def check(current_data):
    """
    주어진 보호필름(current_data)이 성능 검사를 통과하는지 확인하는 함수
    """
    # W: 가로 크기, K: 합격 기준
    for c in range(W):
        # 각 열을 순회하며 합격 기준을 만족하는지 검사
        cnt = 1
        is_passed = False
        for r in range(1, D):
            if current_data[r][c] == current_data[r - 1][c]:
                cnt += 1
            else:
                cnt = 1

            if cnt >= K:
                is_passed = True
                break

        # 한 열이라도 통과하지 못하면 즉시 False 반환
        if not is_passed:
            return False

    # 모든 열이 검사를 통과한 경우 True 반환
    return True


def solve(injection_count):
    """
    injection_count 만큼의 약품을 투여하여 성능 검사를 통과할 수 있는지 확인하는 함수
    """
    # D: 필름의 두께(세로)
    # 약품을 투여할 행의 모든 조합을 생성
    row_combinations = combinations(range(D), injection_count)

    for rows_to_inject in row_combinations:
        # 약품 종류(A:0, B:1)의 모든 중복 순열을 생성
        drug_combinations = product([0, 1], repeat=injection_count)

        for drugs in drug_combinations:
            # 원본 데이터는 유지하고, 테스트를 위한 임시 필름 생성
            temp_data = [row[:] for row in data]

            # 선택된 행에 약품 투여
            for i in range(injection_count):
                row_idx = rows_to_inject[i]
                drug_type = drugs[i]
                temp_data[row_idx] = [drug_type] * W

            # 약품 투여 후 성능 검사
            if check(temp_data):
                return True  # 통과하는 경우를 찾으면 즉시 True 반환

    # 모든 조합/순열을 시도해도 통과하지 못하면 False 반환
    return False


T = int(input())
for tc in range(1, T + 1):
    # D: 필름의 두께, W: 가로 크기, K: 합격 기준
    D, W, K = map(int, input().split())
    # data: 보호 필름의 초기 상태 정보
    data = [list(map(int, input().split())) for _ in range(D)]

    # 약품을 0번 투입하는 경우부터 K-1번까지 순차적으로 확인
    # K번 투입하면 무조건 통과 가능하므로 K는 답이 될 수 없음
    for result in range(K + 1):
        # result 만큼의 약품을 투여해서 통과가 가능한지 확인
        if result == 0:
            # 약품을 투여하지 않은 원본 상태에서 먼저 확인
            if check(data):
                print(f'#{tc} {result}')
                break
        elif solve(result):
            print(f'#{tc} {result}')
            break