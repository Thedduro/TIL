import sys
sys.stdin =  open('sample_input.txt', 'r')
'''
     - 1-N번 까지의 출석번호가 있음
     - M장의 신청서
     - 일단, N중에 신청서를 내지 않은 사람은 혼자 단독 조 구성
'''
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))

    cnt = 0
    for i in range(1, N+1): # 1-N 까지 돌면서 만약에, 신청서 쌍에 없다면, 단독 팀 구성
        if i not in lst:
            cnt += 1
    
    result = []
    
    for i in range(0, len(lst), 2):
        x = lst[i]
        y = lst[i+1]
        
        found = []
        
        for idx, r in enumerate(result): # 팀 신청서 중에 한명이라도 result에 잇다면 같은조로 묶임
            if x in r or y in r: 
                r.extend([x,y])
                found.append(idx)

        if not found:
            result.append([x,y])
        
        else:
            # 여러 그룹에 속해버리면 -> 합쳐줘야 함
            base = found[0]
            for idx in found[1:][::-1]:  # 뒤에서부터 pop
                result[base].extend(result[idx])
                result.pop(idx)
    
    cnt += len(result)
    
    print(f'#{tc}', cnt)