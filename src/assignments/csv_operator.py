

class student:

    def __init__(self, id, name, roll_no, address):
        self.id = id
        self.name = name
        self.roll_no =roll_no
        self.address = address

    def __str__(self):
        return 'Student id: %d, Name: %s roll No: %d from %s' %s (self.id, self.name, self.roll_no, self.address)




student_list = []

for index in range(1,10):
    s = student(index, "shankar_%s" % index, index+10, "solapur")
    student_list.append(s)




