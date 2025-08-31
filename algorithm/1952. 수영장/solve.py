import sys
sys.stdin = open('sample_input.txt', 'r')

def find(month, current):
    global min_value

    if current >= min_value:
        return
    if month > 12:
        min_value = min(current, min_value)
        return
    
    find(month+1, current + (plan[month]) * costs[0])
    find(month+1, current + costs[1])
    find(month+3, current + costs[2])
    find(month+12, current + costs[3])

T = int(input())
for tc in range(1, T+1):
    costs = list(map(int, input().split()))
    plan = list(map(int, input().split()))
    plan = [0] + plan
    min_value = float('inf')
    find(1, 0)
    print(f'#{tc}', min_value)