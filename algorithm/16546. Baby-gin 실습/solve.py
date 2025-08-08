import sys
sys.stdin = open("input.txt", "r")

def baby_gin(numbers):
    numbers.sort()

    for num in numbers: # 중복 숫자 제거
        if numbers.count(num) >= 3: # 3개 이상 중복 숫자 있으면 3번만 그 숫자 제거
            for _ in range(3):
                numbers.remove(num) 
    if len(numbers) == 0: # 그랬는데, 빈 리스트면 true
        return 'true'
    
    for _ in range(len(numbers)//3): # 연속된 숫자열 제거, 3개면 1번 6개 있으면 2번 실행
        v = min(numbers) # 일단 최솟값을 구하고
        if v+1 in numbers and v+2 in numbers: # 만약 +1, +2 값이 있으면 > 제거
            numbers.remove(v)
            numbers.remove(v+1)
            numbers.remove(v+2)
    
    if len(numbers) == 0: # 했는데 빈 리스트면 true
        return 'true'
    
    return 'false' # 다 실행했는데도 값을 반환을 못했어? > 그럼 baby gin 아님


T = int(input())

for tc in range(1, T+1):
    numbers = list(map(int, input().strip())) # strip < 이거 때문에 fail 5번 뜸......
    
    print(f'#{tc} {baby_gin(numbers)}')