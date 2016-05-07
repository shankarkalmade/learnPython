

x = 10
y = 30
scope = vars()
print scope

def add():
    'update global x values'
    global y

    x = y
    print "inside block: ", x


add()

print scope


