import string
# collection of important string methods

# ===========  find

str1= "Hi buddies , how are you? Hi you are welcome"

print str1.find("are")

# starting find from given index

print str1.find("are", 20)

# find seq within start and end point

print str1.find("Hi", 5, 35)


# =========== join

names =[ "shankar", "abhi", "swapnil", "gaurav"]

concat_names = ", ".join(names)

print concat_names

paths = 'home', 'shankar', 'shankar_data', 'movies'

complete_path = '/'.join(paths)

print complete_path

# =========== title

print str1.title()

# using capword

print string.capwords(str1)


# =========== replace

print str1.replace('Hi', 'Hello')


#============ split

print complete_path.split('/')

# default split uses whitespaces

print str1.split()


#============ strip

if 'shankar '.strip() in complete_path.split('/') : print "found it"



