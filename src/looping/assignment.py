

# sequence unpacking

x,y,z = 1,2,"Shankar"

print x,y,z

# swap variable content

a, b = 10,20
print a, b

print "after swap"
a,b = b,a
print a, b

# using single variable

shankar_data = "shankar", "kalmade", 26

name , last_name , ageg = shankar_data

print name, last_name

# Assigning  tuple

shankar_dict = {'name' : 'Shankar',
                'last_name' : 'Kalmade',
                'age' : 26
                }

key , value = shankar_dict.popitem()

print "Age:" , value

#augmented assignment

complete_name  ="shankar"
complete_name +=  " Kalmade"

print complete_name

