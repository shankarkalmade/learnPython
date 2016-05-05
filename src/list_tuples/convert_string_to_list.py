

# sample code to convert string to list

name= "shankar"

name_list = list(name)

print  name_list

# adding last name to list

complete_name = name_list + list(" Kalmade")

print complete_name

complete_name[7]= "_"

print complete_name

# assign list to slice

complete_name[8:] = list("Ghadlatte")

print complete_name





