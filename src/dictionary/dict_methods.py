from copy import  deepcopy


people ={ 'Alice': {
'phone': '2341',
'addr': 'Foo drive 23'
},
'Beth': {
'phone': '9102',
'addr': 'Bar street 42'
},'Cecil': {
'phone': '3158',
'addr': 'Baz avenue 90'
}
}

print people


# shallow copy
copied_people = people.copy()

people['Beth']['phone'] = '2016'

print people

print copied_people

# deep copy dict

deep_copy = deepcopy(people)

people['Beth']['phone'] = '1989'

print "after deep copy changed values"

print people
print deep_copy


# fromkeys
# get only name and address
print copied_people.fromkeys({'name', 'addr'})


#haskeys
print "checking if dict contains key named Beth"
print people.has_key('Beth')

# item method
print "Printing all items in dict"
print people.items()

# get all keys in dict

print "Printing all keys IN DICT for Beth"
print people.get('Beth').keys()

# pop specific pair
print "Poping addr for Beth"
copied_people.get('Beth').pop('addr')
print copied_people
print people

# update Beths content

print "After update"
address ={'phone', '2265'}

copied_people.get('Beth').update({'phone': '2341', 'addr': 'Foo drive 23'})
print copied_people










