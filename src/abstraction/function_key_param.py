

def say_hello(greetings, name):
    print '%s, %s' % (greetings, name)

say_hello("Hi", "Shankar")

# swapping arg

def say_hello2(name, greetings):
    print '%s, %s' % (greetings, name)

say_hello2("shankar", "Hi")


# naming param

say_hello(greetings="Hi", name="Shankar")

# function with default values
def say_hello3(greetings ='Hi', name='world'):
    print '%s, %s' % (greetings, name)


say_hello3()
say_hello3(greetings="Hello")


