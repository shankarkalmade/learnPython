
# list sort demo


sample_list =[10,2,30,45,25,41,20,89]

print sample_list

# sample_list.sort()

#print sample_list


# sort and assign to new list

sorted_list = sample_list[:]

sorted_list.sort()

print sorted_list


sorted_list_using_copy= sample_list

sorted_list_using_copy.sort()

print  sorted_list_using_copy


# using sorted function

sorted_using_function = sorted(sample_list)

print sorted_using_function



