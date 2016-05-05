

# sample list methods

name= "shankar"

name_list = list(name)

print  name_list

# adding last name to list

complete_name = name_list + list(" Kalmade")

complete_name.append("S")

complete_name = complete_name + list("olapur")

print complete_name

# count specific elements

print "Total count of S: ", complete_name.count("S")


# extend
address = list (" Tq: South Solapur, Distt: Solapur")

complete_name.extend(address)

print complete_name


# index: access elements using index


print "10 th element of list: ", complete_name.index("S")


# insert

complete_name.insert(0, "Mr.")

print complete_name

# remove

complete_name.remove(" ")

print complete_name