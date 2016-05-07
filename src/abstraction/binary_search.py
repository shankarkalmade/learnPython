# sample code for binary search

def binary_search (sequence, number, lower, upper):
    if upper is None:
        upper = len(sequence)-1

    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (upper + lower) // 2
        if number > sequence[middle]:
            binary_search(sequence, number, middle+1, upper)
        else:
            binary_search(sequence, number, lower, middle)



''' Code to check binary search '''

data =  [1,20,5,6,89,45,62,47]

data.sort()

print binary_search(data, 6,0,len(data)-1)






