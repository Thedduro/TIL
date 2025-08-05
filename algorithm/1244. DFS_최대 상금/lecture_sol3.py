import sys
sys.stdin = open('input.txt')

def swap(depth):
    global result
    val = int(''.join(numbers))
    if val in memo[depth]:
        return
    memo[depth].add(val)

    if depth == K:
        result = max(result, val)
    else:
        for i in range(N-1):
            for j in range(i + 1, N):
                numbers[i], numbers[j] = numbers[j], numbers[i]
                swap(depth + 1)
                numbers[i], numbers[j] = numbers[j], numbers[i]


T = int(input())
# 최대 6자리 수에 대한 모든 경우의 수 순열 6! -> 720
for tc in range(1, T + 1):
    data = input().split()
    numbers, K = list(data[0]), int(data[1])
    memo = [set() for _ in range(11)]
    N = len(numbers)
    result = 0  # 최종 결괏값
    swap(0)
    print(f'#{tc} {result}')

