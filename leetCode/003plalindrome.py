# 判断某个输入项是否是字符串
print("请输入任意字符串")
a_string = list(input())
a_string_len = len(a_string)

i = 0
while i < a_string_len/2:
    last_num = a_string_len - 1 -i
    if a_string[i] != a_string[last_num]:
        break
    else:
        i += 1
        continue
if a_string_len % 2 ==0:
    if i != a_string_len/2:
        print("这不是回文")
    else:
        print("这是回文")
else:
    if i != (a_string_len + 1)/2:
        print("这不是回文")
    else:
        print("这是回文")