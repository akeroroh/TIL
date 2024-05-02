number_of_book = 100

name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(name, age, address):
    user_info = {
        'name' : name,
        'age' : age,
        'address' : address
    } 
    print(f"{user_info['name']}님 환영합니다!")
    return user_info

def decrease_book(number):
    global number_of_book
    number_of_book -= number
    print (f'남은 책의 수 : {number_of_book}')
    return number_of_book

many_user = list(map(create_user, name, age, address))
info = list(map(lambda user: {'name': user['name'], 'age': user['age']}, many_user))

def rental_book(x):
    name = x['name']
    number = x['age']//10
    decrease_book(number)
    print(f'{name}님이 {number}권의 책을 대여하였습니다.')

list(map(lambda x : rental_book(x), info))