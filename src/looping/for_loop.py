

# testing for loop

names =['shankar', 'abhi', 'swapnil', 'gaurav']

for name in names:
    print name


# printing range

for number in range(0,10):
    print number

# square of first 20 numbers
'''
for number in range(20):
    print pow(number,2)
'''

# iteratting dictionary

shankar_dict = {'name': 'Shankar',
                'last_name': 'Kalmade',
                'age': 26
                }

for key in shankar_dict:
    print key, ' is assigned to : ', shankar_dict[key]

# using key pair values

for key, value in shankar_dict.items():
    print key, " : ", value


# numbered iteration

names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]


for i in range(len(names)):
    print 'Age of %s if %d'% (names[i], ages[i])


# zip functions

for name , age in zip(names, ages):
    print name , ' is ', age, ' old'



