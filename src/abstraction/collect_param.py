


#sample code to collect param and do arithmetic operation on that

def do_math (operation = 'sum', *values):
    if operation =='sum':
        total =0
        for val in values:
            total+=val
        print total

    elif operation=='mult':
        total =1
        for val in values:
            total*= val
        print total



do_math('sum',1,2,3,4,5)
do_math('mult',1,2,3,4,5)


