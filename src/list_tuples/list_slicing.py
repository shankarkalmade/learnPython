
# slicing demo


counts = [0,1,2,3,4,5,6,7,8,9,10]

print counts[0:1]
print counts[1:5]


# reverse range

# get last three elements
# it wont work
#print counts[-3:-1]

print counts[-3:]

# get first three elements

print counts[:3]

# print complete seq

print counts[:]

# print every 2nd element

print counts[::2]


complete_name = "Shankar Kalmade"

print complete_name[0:7]

print complete_name[8:len(complete_name)]



# slicing web url

url = "http://www.google.com"

domain_name= url[11:-4]

domain_type = url[-3:]

print "domain Name: ", domain_name, " domain Type: ", domain_type

