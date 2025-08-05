def dfs(origin, ch_num):
    global max_num

    if ch_num == change: # 교환횟수가 최종과 동일한 경우 교환 더이상 진행하지 않음
        max_num = max(int(origin), max_num)
        return 
    
    if (origin, ch_num) in visited: # 이미 교환 했던 값이 바꿔본적 있으면 pass > 교환횟수, 숫자가 동일하면
        return
    
    visited.add((origin, ch_num))

    origin = list(origin)

    for i in range(len(origin)):
        for j in range(i+1, len(origin)):
            origin[i], origin[j] = origin[j], origin[i]
            dfs(''.join, ch_num + 1)
            origin[i], origin[j] = origin[j], origin[i] 
            # dfs에 깂을 전달한 후에도 중첩 for문으로 남은 값 교환 해야 함 > 원상복귀
        

T = int(input())

for tc in range(1, T+1):
    origin, change = input().split()

    change = int(change)

    max_num = 0 
    visited = set()
    dfs(origin, 0)


