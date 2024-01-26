
number_of_book = 100

def decrease_book(number):
    global number_of_book
    print (f'남은 책의 수 : {number_of_book - number}')

def rental_book(name, number):
    global decrease_book
    decrease_book(number)
    return (f'{name}님이 {number}권의 책을 대여하였습니다.')

result = rental_book('홍길동', 3)
print(result)