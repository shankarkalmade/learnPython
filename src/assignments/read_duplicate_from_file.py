"""
This code will read file content and count word occurences

"""
def build_count_from_file (file_path) :

    '''

    :param file_path:
    :return: word counts
    '''
    # craete dict to hold counts

    word_counts = {}

    with open(file_path,"r") as file_obj:

        line = file_obj.readline()

        while line:

            line = line.strip()
            if line in word_counts :
                word_counts[line] += 1
            else :
                word_counts[line] =1

            line = file_obj.readline()
    return word_counts



if __name__ =="__main__" :

    """
    Read file and count occurences
    """
    file_name = "image_name_input.txt"

    """
    display word counts
    """

    count_dict = build_count_from_file(file_name)

    for word_count in count_dict:
        print '%s : %d' % (word_count, count_dict[word_count])