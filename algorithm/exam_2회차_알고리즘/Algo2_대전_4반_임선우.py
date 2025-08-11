

def find(stack, sum):
    
    while stack:
        value = stack.pop()
        
        if value.isnumeric():
            sum += int(value)*int(value)
        if value == '[':
            return stack, sum

# def find(stack, sum):
#     candi = []

#     while stack:
#         value = stack.pop()

#         if value.isnumeric():
#             candi.append(value)
#             if len(candi) == 1 and stack[-1] == '[':
#                 sum += int(value)*int(value)
#             if len(candi) == 2 :
#                 sum += int(candi[0]) * int(candi[1])

#         if value == '[':
#             return stack, sum

def solve(data, i):
    global stack
    global sum
    
    while stack:

        if data[i] == '[':
            stack.append(data[i])

        if data[i].isnumeric(): # 숫자면 
            stack.append(data[i])

        if data[i] == ']': # 닫는 괄호면
            stack, sum = find(stack, sum)
            # for i in range(-1, len(stack), -1):
            #     print(stack[i])
            #     if stack[i].isdigit():
            #         value = stack.pop()
            #         sum += value*value
            #         print('숫자', value, sum)
            #     if stack[-1] == '[':
            #         value = stack.pop()
            #         break
        i = i+1


    
T = int(input()) 

for tc in range(1, T+1):
    N = int(input())

    data = input()
    data = data.replace(',','')

    stack = ['[']
    sum = 0

    solve(data, 1)
    print(f'#{tc}', sum)