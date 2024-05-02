############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
def is_position_safe(N, M, current):
    current_list = list(current)
    if M == 0:
        current_list[0] -= 1
    if M == 1:
        current_list[0] += 1
    if M == 2:
        current_list[1] -= 1
    if M == 3:
        current_list[1] += 1 
    return 0 <= current_list[0] < N and 0 <= current_list[1] < N



# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(is_position_safe(3, 1, (0, 0))) # True
print(is_position_safe(3, 0, (0, 0))) # False
#####################################################
