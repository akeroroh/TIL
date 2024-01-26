# 아래 함수를 수정하시오.
def even_elements(lst):
    i = 0
    while i < len(lst):
        if lst[i] % 2 == 1:
            lst.pop(i)
        else:
            i += 1

    result_list = []
    result_list.extend(lst)
    return result_list

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = even_elements(my_list)
print(result)
