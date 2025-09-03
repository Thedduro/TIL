import sys
sys.stdin = open('input.txt')


def saerch(acc):
    global result

    # 다 터트리면 갱신
    if not data:
        result = max(result, acc)
        return

    # 남은 풍선으로 모든 상황 계산
    for i in range(len(data)):
        score = 0
        if 0 < i < len(data) - 1:
            score = data[i - 1] * data[i + 1]
        elif i > 0:
            score = data[i - 1]
        elif len(data) > 1:
            score = data[i + 1]
        else:
            score = data[i]

        # 1. i 번째 터트린다? -> i 번째 없앤다.
        balloon = data.pop(i)
        # 2. 더해보고
        saerch(acc + score)
        # 3. 다시 i 번째에 원상복구
        data.insert(i, balloon)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))
    result = 0
    saerch(0)
    print(f'#{tc} {result}')
