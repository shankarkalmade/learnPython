

# sample code to grant access using  memborship

sample_data = [

    ["shankar", "root"],
    ["abhi", "dev"],
    ["gaurav", "tmp"],
    ["mahendra",]

]


user_name = raw_input("Enter username: ")
password= raw_input("Enter password: ")

if [user_name,password] in sample_data :
    print "access granted"
else :
    print "Not valid login"
