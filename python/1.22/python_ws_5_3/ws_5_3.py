# 아래 함수를 수정하시오.
def sort_tuple(tup):
    lst_tup = list(tup)
    lst_tup.sort()
    new_tuple = tuple(lst_tup)
    return new_tuple


result = sort_tuple((5, 2, 8, 1, 3))
print(result)
