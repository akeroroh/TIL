# 아래 함수를 수정하시오.
def reverse_string(x):
    char_list = list(x)
    char_list.reverse()
    reverse_str = ''.join(char_list)
    return reverse_str


result = reverse_string("Hello, World!")
print(result)  # !dlroW ,olleH
