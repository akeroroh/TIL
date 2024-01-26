# 아래 함수를 수정하시오.
def count_character(str_all, str_1):
    cha_lst = list(str_all)
    return cha_lst.count(str_1)



result = count_character("Hello, World!", "o")
print(result)  # 2
