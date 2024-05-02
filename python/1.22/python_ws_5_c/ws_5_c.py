original_word = '코딩 공부는ㄴ 1일ㄹ 1커ㅓ밋ㅅ @@@#^()#_+!&~:"'
word = '1ㄴ2ㄹ3ㅓ4ㅅ5'
arr = []

arr.extend(list(original_word))
print(arr)

def restructure_word(word, arr):

    for i in range(len(word)):
        if word[i].isdecimal() == True:
            for z in range(int(word[i])):
                arr.pop()
        else:
            arr.remove(word[i])

    return arr

result = restructure_word(word, arr)
print(result)

result2 = ''.join(result)
print(result2)


