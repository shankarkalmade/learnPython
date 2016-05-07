

# factorial

def factorial (number):
    if number ==1:
        return 1
    else:
        return  number  * factorial(number-1)

print factorial(20)




# POWER OF FUCTION

def power (number, p):
    if p==0:
        return 1
    else:
        return  number * power(number, p-1)


print power(5,3)
