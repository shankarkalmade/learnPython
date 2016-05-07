

# sample function demo

def say_hello (name) :
    print "Hello!", name


def square (number):
    'This will return square of number'
    return number * number

say_hello("shankar")
print square(20)
print square.__doc__

print help(square)



#create name and change content

def get_name():
    names = ['shankar', "abhi", "michel"]
    names[1] = "Abhishek"

    return  names[1]


print get_name()

