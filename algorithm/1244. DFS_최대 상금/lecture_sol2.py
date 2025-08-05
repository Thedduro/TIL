import sys
sys.stdin = open('input.txt')

def swap(int_number, i, j):
    '''
    :param int_number: 정수로 되어 있는 값 
    :param i: start_index
    :param j: end_index 를 스왑한
    :return: 다시 정수로 바꾼 값
    '''
    # 정수 int_number의 i와 j번째를 스왑
    # 정수를 자릿수별로 분할해서 배열에 저장하기
    arr = [0] * N
    for k in range(N-1, -1, -1):
        arr[k] = int_number % 10
        int_number //= 10
    arr[i], arr[j] = arr[j], arr[i]

    # arr로 만든 값들 다시 문자열로 합치기
    return ''.join(arr)

def search(number, depth):
    global result

    for i in range(MAXSIZE):
        if memo[depth][i] == 0: # 아직 값을 갱신 안했다면
            memo[depth][i] == number
            break
        elif memo[K][i] == number:  # 이미.. K번째 목표지점에 number가 있어?
            # 중복이네? 그럼 뭐... 굳이 이 number를... 내 memo에 넣을 이유가 없다.
            return

    if depth == K:
        if number > result:
            result = number
        return
    else:
        for i in range(N-1):
            for j in range(i + 1, N):
                # 원본 안건들고 작업을 할 수 있어서... 복원이니 뭐니 안해도됨
                search(swap(number, i, j))

T = int(input())

# 최대 6자리 수에 대한 모든 경우의 수 순열 6! -> 720
MAXSIZE = 720
for tc in range(1, T+1):
    numbers, K = map(int, input().split())
    print(numbers, K)
    memo = [[0] * MAXSIZE for _ in range(K+1)]
    N = len(str(numbers))
    print(N)
    
    result = 0 # 최종 결괏값
    print(f'{tc} {result}')

