

def find_max(x,y,z):
    if x > y and x> z:
        print "max is : %d" % x
    if y > z and z> x :
        print "max is : %d" % y
    if z > x and z > y :
        print "max is : %d" % z



in1 = input("Enter first Number : ")
in2 = input("Enter second Number : ")
in3 = input("Enter third Number : ")

find_max(in1,in2, in3)