name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']

def create_user(names, ages, addresss):
    user_info = {
        'name' : names,
        'age' : ages,
        'address' : addresss
    } 
    print(f"{user_info['name']}님 환영합니다!")
    return user_info

result = list(map(create_user, name, age, address))
print(result)
