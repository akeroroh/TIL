data_1 = 'qweqwYadnOyjnsaU4trwg asjnaAn245krRmkfE 42grTasdnHasdnvEasdn asdevadnBasdanEsdkqefqefvaSasdqaeeqqvedwt5hfbsdT24tewfd'

'''
예시코드
arr = [1, 2, 3, 4, 5]
for num in arr:
    print(num, end='')
출력결과 : 12345
'''

# 아래에 코드를 작성하시오.

for i in range(len(data_1)):
    if data_1[i] == ' ':
        print(data_1[i], end = '')
    elif data_1[i].isupper() == True:
        print(data_1[i], end = '')
    else:
        continue

print()
data_2 = '걉파반샤팝다푸거맥파바자들퍼바배들밥샵파누타히매니배사바파힘다브사부힙헤베내테치대내'
arr = []
# 아래에 코드를 작성하시오.

arr.append(data_2.find('내'))
arr.append(data_2.find('힘'))
arr.append(data_2.find('들'))
arr.append(data_2.find('다'))
print(arr)

arr.sort()
print(arr)

for i in arr:
    print(data_2[i], end='')