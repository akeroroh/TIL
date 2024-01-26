my_set = {'가', '나', (0, 0)}
my_dict = {
        '가': 1, 
        (0, 0): '튜플도 키값으로 사용가능'
    }

# 아래에 코드를 작성하시오.

for i in my_set:
    mine_dict = my_dict.get(i, None)
    print(mine_dict)

var = (1, 2, 3, 'A')

my_dict.update({var : '변수로도 키 설정 가능'})
print(my_dict)
