

# sample code to generate fib series for given range


def fib_series (num):
    fib = [0,1]
    for i in range(num-2):
        fib.append(fib[-2]+ fib[-1])
    return fib


# get first 10 fib number

print fib_series(10)





