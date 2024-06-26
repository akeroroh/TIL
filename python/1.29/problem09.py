############## 주의 ##############
# 입력을 받기위한 input 함수는 절대 사용하지 않습니다.
# 재귀함수를 이용하여 구현합니다.
def dec_to_bin(n):
    num = []
    while n != 0 or n != 1:
        n // 2
        num.append(n % 2)
        continue
    return num


# 추가 테스트를 위한 코드 작성 가능
# 예) print(함수명(인자))

#####################################################
# 아래 코드를 삭제하는 경우 
# 모든 책임은 삭제한 본인에게 있습니다. 
############## 테스트 코드 삭제 금지 #################
print(dec_to_bin(55))   # 110111
print(dec_to_bin(15))   # 1111
#####################################################
