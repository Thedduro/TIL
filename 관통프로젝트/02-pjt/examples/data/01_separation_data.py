import csv

# 파일 경로 설정
input_file_path = 'completed_todos.csv'
todos_output_file_path = 'todos.csv'
users_output_file_path = 'users.csv'

# 입력 파일 읽고 데이터 분리
def read_and_split_csv(file_path):
    todos = []
    users = {}
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # 행 하나하나가 하나의 todo에 대한 정보
            todo = {'id': row['id'], 'title': row['title'], 'user_id': row['user_id']}
            user = {
                 'id': row['user_id'],
                 'first_name': row['user_name'].split()[0],
                 'last_name': row['user_name'].split()[-1],
                 'username': row['user_username'],
                 'email': row['user_email'],
            }
            todos.append(todo)
            users[row['user_id']] = user
    # print(todos)
    # print(users)
    return todos, list(users.values())

# CSV 파일로 저장
def write_csv(file_path, data, fieldnames):
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def main():
    todos, users = read_and_split_csv(input_file_path)
    
    # todos.csv 저장
    todos_fieldnames = ['id', 'title', 'user_id']
    write_csv(todos_output_file_path, todos, todos_fieldnames)
    
    # users.csv 저장
    users_fieldnames = ['id', 'first_name', 'last_name', 'username', 'email']
    write_csv(users_output_file_path, users, users_fieldnames)
    
if __name__ == '__main__':
    main()
