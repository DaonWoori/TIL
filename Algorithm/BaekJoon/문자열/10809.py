# 알파벳 찾기
import string
small_l = string.ascii_lowercase

input_st = input()

for s in small_l:
    idx = input_st.find(s)
    print(idx, end=' ')
    
# 아스키코드 활용
# alphabet = list(range(97,123))
# print(word.find(chr(x)))

