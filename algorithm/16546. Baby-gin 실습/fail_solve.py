import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def baby_gin(numbers):
    result = [0, 0]
    numbers.sort()

    for i in range(1, 5):
        if numbers[i] == numbers[i-1] + 1 and numbers[i] == numbers[i+1] - 1: # run으로 구성되면
            result[0] += 1

    for num in numbers:
        if numbers.count(num) >= 3: # 동일한 카드가 3장 이상이면
            result[1] += 1
    
    if result[0] >= 1 and result[1] >= 1: # 두 조건 모두 만족 시 true
        return True
    
    if result[0] == 2 or result[1]==2:
        return True
    return False

for tc in range(1, T+1):
    numbers = list(map(int, input()))
    
    print(f'#{tc} {baby_gin(numbers)}')
