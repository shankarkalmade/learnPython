

# sample code to search through dict


people = {
'Alice': {
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


# printing lables

labels ={
    'phone': 'Phone Number',
    'addr' : 'Address'
}

name = raw_input("Enter name")

request_info = raw_input("Are you looking for phone Number (p) or Address (a): ")

if request_info=='p' : key = 'phone'
if request_info=='a' : key = 'addr'

if name in people : print "%s's %s is %s" % \
                          (name , labels[key], people[name][key])

