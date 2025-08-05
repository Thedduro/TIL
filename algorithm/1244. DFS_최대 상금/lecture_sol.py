import sys
sys.stdin = open('input.txt')

'''
주어진 숫자판들 중에         [1, 2, 3, 4, 5] 
두 개를 선택에서              0  1  2  3  4  <- start_index, end_index   
정해진 횟수만큼               ? 모르겠고 전부다
서로의 자리를 위치를 교환  start_index, end_index = end_index, start_index
                            0번 1번 자리바꾸기         0 1
                            0번 2번 자리바꾸기         0 2
                            0번 3번 자리바꾸기         0 3
                            0번 4번 자리바꾸기         0 4
                            0번 5번 자리바꾸기         0 5
                            1번 2번 자리바꾸기         1 2
                            1번 3번 자리바꾸기         1 3
                            1번 4번 자리바꾸기         1 4
                            1번 5번 자리바꾸기         1 5
                            ...
'''
'''
    1 단계
    
arr = [1, 2, 3, 4, 5, 6]
# 그러면 start_index는 5까지 아닌가요? -> 지금은 신경쓰지 말자.
for start_index in range(6):
    # start_index가 5가 되었을때, end_index에 대한 범위는?
    # range(5+1, 6) -> 순회 할 수 없음 -> 코드 실행 안됨.
    # for idx in []:
    #     print(idx)
    for end_index in range(start_index + 1, 6):
        print(start_index, end_index)
        # 이 arr은, 이 2중 for문에서 계속 바꿔 나가는데
        # 나는, arr의 원본은 그대로 둔 상테 [1, 2, 3, 4, 5, 6] 에서
        # 0 1, 0 2, 0 3, 0 4, 0 5 순으로 서로 스왑한 결과가 궁금 한것
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        print(arr, 'swap')  # 0과 1을 스왑한 결과를 출력 해보고 나서는
        # 다시, 1과 0번째 자리에 있는 값을 바꿔서
        # 원래 모양으로 복구 시킨다.
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        # print(arr, 'orin')
'''


'''
    2단계 
    1 2 3 4 5 6 -> 0번째와 1번째를 스왑한 상태
    결과: 2 1 3 4 5 6
    를 가지고, 다시... 0 1, 0 2, 0 3, 0 4, 0 5, 1 2, 1 3, 1 4
    번째를 스왑한 경우도 궁금한 거임!
    
    왜?
    최대 상금 문제가... 정해진 횟수 K번에 대해서,
    항상 숫자 2개를 스왑한 경우를 보고 싶은 거니까! 
    
    1. 재귀 함수가 이해가 된 상태이다 -> 다음단계로
    2. 아니다? 그럼 어떻게 해야 할까?
        그 0과 1을 swap한 결과를 나중에 또 쓸수 있도록 어딘가에 담아보자.
        
    그렇게 해서...
    first_swap_list 라는 곳에 [2, 1, 3, 4, 5, 6], [3, 2, 1, 4, 5, 6]
    이런 리스트 들을 담아두고,
    [2, 1, 3, 4, 5, 6] 을 가지고, 다시, 0 1, 0 2 .... swap
    [3, 2, 1, 4, 5, 6] 을 가지고, 다시, 0 1, 0 2 .... swap
    ...
    
    arr = [1, 2, 3, 4, 5, 6]
first_swap_list = []
for start_index in range(6):
    for end_index in range(start_index+1, 6):
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
        first_swap_list.append(list(arr))    # 복사 문제 조심
        arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
print(first_swap_list)  # 한 번 swap한 모든 경우의 수 들을 이곳에 담아두었다.
# 이번에는 first_swap_list에 있는 모든... 리스트들에 대해서
# 1단계에서 했던 작업 똑같이 다시하기.

for temp_arr in first_swap_list:    # [2, 1, 3, 4, 5, 6] / [3, 2, 1, 4, 5, 6]
    print(f'======={temp_arr}========')
    for start_index in range(6):
        for end_index in range(start_index+1, 6):
            temp_arr[start_index], temp_arr[end_index] = temp_arr[end_index], temp_arr[start_index]
            print(temp_arr, start_index, end_index)
            temp_arr[start_index], temp_arr[end_index] = temp_arr[end_index], temp_arr[start_index]
        print('='*30)

# 여기까지 했더니.... 이제 2번 swap 한게 된다...
# second_swap_list도 필요하지 않을까?
    [1, 2, 3, 4, 5, 6] 을 기준으로 0번과 1번을 swap했던
    [2, 1, 3, 4, 5, 6] 을 가지고, 다시 한번 0과 1부터... swap하는 리스트들..
    ---
    [1, 2, 3, 4, 5, 6] 0 1  -> 얘네도... 다시 0 1, 0 2, 0 3... swap 해봐야할듯..
    [3, 1, 2, 4, 5, 6] 0 2  -> 언제까지? K번 반복할 때까지...
    [4, 1, 3, 2, 5, 6] 0 3  -> 문제는 K라고 하는 일이... 매 TC마다 다르다!
    [5, 1, 3, 4, 2, 6] 0 4
    [6, 1, 3, 4, 5, 2] 0 5
    
    third_s_l, fourth_s_l, f_s_l, SSL.... 내가 다 만들어 줄 수가 없다.
'''

'''
    3 단계
    위에서 코드 짜다보니까... 반복되는 부분이 있더라.
    arr = [1, 2, 3, 4, 5, 6]
    K = 10
    # K가 가변형이라면...
    # first_ 어쩌구 하는 친구를... Nth_swap_list로 만들어서... K개 만들면되는거아님?
    Nth_swap_list = [[] for _ in range(K)]
    Nth_swap_list[0] = [1, 2, 3, 4, 5, 6]
    # K개 만들어서, K번 만큼 반복해서 k번째 리스트에 넣으면 되는거 아님?
    for k in range(1, K):
        for start_index in range(6):
            for end_index in range(start_index+1, 6):
                Nth_swap_list[k-1][start_index], Nth_swap_list[k-1][end_index] = arr[end_index], arr[start_index]
                Nth_swap_list[k].append(list(arr))    # 복사 문제 조심
                arr[start_index], arr[end_index] = arr[end_index], arr[start_index]
    for item in Nth_swap_list:
        print(item)
    
    # 이렇게 쓰기 시작하면, 코드가 점점 길어지고 난 장판이 난다....
    # 그럼.... 내가 이걸 처리하려면?
    # 함수화 해서 생각해보자.
'''
'''
    4단계
    함수화
'''

def swap(depth):
    '''
        depth: 몇 번 swap 했는지를 기록
            -> Nth_swap_list의 depth 번째에 값을 append
    '''
    Nth_swap_list[depth].append(list(arr))
    # 내가 만약, K번만큼 다 swap을 했다면
    if depth == K:
        # 그때 만들어진 값이 곳, 내가 원하는 최종 답들의 후보 중에 하나다.
        # 왜? 후보중에 하나냐?
        # K번만큼 swap 하는 경우의 수들이 너무 많으니...
        # 그중에 제일 큰 값이 내가 원하는 값이다.
        # 어... list가... 정수들을..가지고 있어서.. 그걸 다 합쳐서.... '123' 으로는 어케 만들지?
            # -> 5단계,,,
        # 최종 결괏값을 최댓값으로 갱신 할 수 있는 어떠한 코드를 작성 완료 했다면...!!!
        # 이제.. 제출 해보자.
            # -> 아마 시간초과가 날 것이다.
        return
    else:
        for i in range(3):
            for j in range(i + 1, 3):
                arr[i], arr[j] = arr[j], arr[i]
                swap(depth + 1) # 바뀐 배열을 가지고, swap을 하러 보내야 한다!
                arr[i], arr[j] = arr[j], arr[i]
arr = [1, 2, 3]
K = 5
Nth_swap_list = [[] for _ in range(6)]
swap(0)

'''
    5단계
    리스트를 받으면 정수로 바꾸는 함수...
    아니면.. 문자열들을 swap 할 수 있게 할 수 있는 작업 을 
'''