

class person (object):

    def __init__(self, fn, ln, a):
        self.first_name = fn
        self.last_name = ln
        self.age= a


    def __str__(self):
        return self.first_name +"   "+self.last_name

    def __eq__(self, other):
        return self.first_name == other.first_name and self.last_name == other.last_name

    def say_hello(self):
        print 'Hi %s, How are you ' % self.first_name


class student(person):
    def __init__(self,fn, ln, a, g):
        super(student, self).__init__(fn, ln, a)
        self.grades =g

    def __str__(self):
        return 'Name: %s %s, Age: %d , Grades Opt: %s' % (self.first_name, self.last_name,self.age, self.grades)

p = person("shankar","kalmade ",25)
print p

s = student("shankar","kalmade ",25,['math', 'science'])
print s



