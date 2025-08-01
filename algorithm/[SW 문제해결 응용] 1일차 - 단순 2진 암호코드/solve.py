num_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}
 
T = int(input())

for t in range(1, T+1): 
    n, m = map(int, input().split()) 
    candidate_grid = []

    flag = False # 플래그 설정

    for _ in range(n):
        row = input().strip()

        if not flag and '1' in row: # 1이 있으면
            candidate_grid.append(row)
            flag = True
 
    end_idx = 0
    for i in range(m-1, 1, -1):
        if candidate_grid[0][i] == '1':
            end_idx = i
            break
 
    result_nums = []
    for j in range(end_idx, end_idx-55, -7):
        binary = candidate_grid[0][j-6:j+1]
        result_nums.append(num_dict.get(binary))
 
    reversed_list = list(reversed(result_nums))
 
    odd_sum = even_sum = result = 0
 
    for i in range(8):
        if i % 2 == 0: # 0 2 4 6
            odd_sum += reversed_list[i]
        else:
            even_sum += reversed_list[i]
 
    result_sum = even_sum + (odd_sum*3)
 
    print(f"#{t} {sum(reversed_list) if result_sum % 10 == 0 else 0}")