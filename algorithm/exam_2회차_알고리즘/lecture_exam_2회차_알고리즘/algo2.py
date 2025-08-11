T = int(input())  # 테스트 케이스 수
for tc in range(1, T + 1):
    N = int(input())  # 문제에서 사용되지는 않는 값
    input_str = input()  # 건물 구조가 담긴 문자열

    # 총 비용을 계산할 변수
    total_amount = 0
    # 괄호의 깊이를 저장할 스택
    stack = []
    # 현재 처리 중인 숫자를 문자열 형태로 저장할 변수
    current_num_str = ''

    # 문자열을 순회하며 각 문자를 처리
    for char in input_str:
        # 1. 문자가 숫자인 경우
        if char.isdigit():
            current_num_str += char
        # 2. 문자가 여는 괄호인 경우
        elif char == '[':
            # 괄호의 깊이를 나타내기 위해 스택에 추가
            stack.append(char)
        # 3. 문자가 닫는 괄호인 경우
        elif char == ']':
            # 닫는 괄호 이전에 숫자가 있었다면 비용 계산
            if current_num_str:
                # 숫자를 정수로 변환하여 현재 괄호 깊이(스택의 길이)만큼 곱해 총 비용에 더함
                total_amount += int(current_num_str) * len(stack)
                # 다음 숫자를 위해 문자열 초기화
                current_num_str = ''
            # 현재 괄호가 닫혔으므로 스택에서 괄호 하나 제거
            stack.pop()
        # 4. 문자가 쉼표인 경우
        elif char == ',':
            # 쉼표 이전에 숫자가 있었다면 비용 계산
            if current_num_str:
                # 숫자를 정수로 변환하여 현재 괄호 깊이(스택의 길이)만큼 곱해 총 비용에 더함
                total_amount += int(current_num_str) * len(stack)
                # 다음 숫자를 위해 문자열 초기화
                current_num_str = ''

    # 최종 결과 출력
    print(f'#{tc} {total_amount}')