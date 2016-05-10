import csv
''' Read csv file conent'''


def csv_reader (file_object):

    reader = csv.reader(file_object)
    for row in reader:
        print row

def use_dict_reader(file_object):
    extract = []
    reader = csv.DictReader(file_object)
    for line in reader:
            extract.append(line['variable_name']+','+line['dataset'])
    return extract


def csv_write (file , data):
    with open(file, "wb") as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            writer.writerow(line.split(","))


file_name = "sample.csv"
with open(file_name, "rb") as read_obj:
    extracted_data = use_dict_reader(read_obj)

print extracted_data


'''Write Data to file '''
write_path = "output.csv"
csv_write(write_path,extracted_data)
print "Done"

























