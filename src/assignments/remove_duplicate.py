


original_list = ['shankar', 'abi', 'swapnil','shankar']
trimmed_list =[]
count_dict = {}

for count in range(0, len(original_list)-1):
    word = original_list[count]
    if word not in count_dict:
        count_dict[word] =1
        trimmed_list.append(word)

print trimmed_list