text = input()
text_list = text.split()
result_list = []
cur_list = []
cur_char = text_list[0]
for el in text_list:
    if el == cur_char:
        cur_list.append(el)
        cur_char = el
    else:
        result_list.append(cur_list.copy())
        cur_list.clear()
        cur_char = el
        cur_list.append(el)

result_list.append(cur_list)
print(result_list)

