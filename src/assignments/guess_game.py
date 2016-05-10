from random import randint

random_number = randint(1,100)
print random_number

input_number = input("Enter a number in 1 to 100")

while(True):
    random_number = randint(1,100)
    if input_number == random_number:
        print "You got it correctly"
        break
    elif input_number > random_number:
        input_number= input("You are too high..Try again")
        if input_number ==0:
            break
    elif input_number < random_number:
        input_number = input("You are too low..Try again")
        if input_number ==0 or input_number=='':
            break




