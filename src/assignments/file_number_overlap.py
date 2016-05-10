from random import randint

# read two files and find out overlapping numbers

def write_file_one ():
    path = "numbers1.txt"
    with open(path, "wb") as write :
        for i in range(1,250):

            ran = randint(200,500)
            write.write(str(ran)+"\n")


def write_file_two ():
    path = "numbers2.txt"
    with open(path, "wb") as write :
        for i in range(1,250):

            ran = randint(100,500)
            write.write(str(ran)+"\n")

def write_files():
    write_file_one()
    write_file_two()

def read_file(file_path):
    """

    :param file_path:
    :return: list of int stored in file
    """
    values = []

    with open(file_path, "rb") as read_data:
        data = read_data.read()
        for val in data:
            values.append(val)

    return data


def find_overlap(list_one, list_two):

    for number in list_one:
        if number in list_two:
            if number !="\n":
                print "Number %s is overlapped " % number


if __name__ == "__main__" :
    #write_files()

    '''read files and create list out of that'''

    list_one = read_file("numbers1.txt")
    list_two = read_file("numbers2.txt")



    """ find overlap values """

    find_overlap(list_one, list_two)




