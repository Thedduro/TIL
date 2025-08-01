def process():
    for test_case in range(1, T + 1):
        N, M = map(int, input().split())

        num_list = [] # 암호코드 리스트
        count = 0
        found = False

        for _ in range(N): 
            val = input() 
            if count == 0 and '1' in val: # 모든 줄이 0이 아닐때만 그리고 첫번째 줄만 판단하는거지> 같은 문자열 반복
                count += 1

                for i in range(M):
                    num = val[i:i+7] # 7개씩 잘라

                    if num in binary_dict.keys(): # 만약에 딕셔너리에 있으면 해당 인덱스 부터 반복문
                        for idx in range(i, M-6 ,7):
                            code = val[idx:idx+7]
                            if code in binary_dict.keys():
                                num_list.append(binary_dict[code])
                        return num_list
                    
import sys

sys.stdin = open("input.txt", "r")
binary_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
            '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

T = int(input())

for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    # 암호코드 올바른지 검증
    sum_e = 0 # 짝수
    sum_o = 0 # 홀수
    num_list = process()

    for i in range(0, len(num_list)):

        if i % 2 == 0: # 짝수 자리의 경우 더함
            sum_e += num_list[i]
        else:
            sum_o += num_list[i] 
    total = sum_o*3 + sum_e

    if total % 10 == 0: # 10배수면 
         print(f'#{test_case}', sum(num_list)) # 리스트의 총합
    else:
        print(f'#{test_case}', 0)