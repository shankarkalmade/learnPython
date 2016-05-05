

# sample bill formatting

width = input("Enter required width : ")

price_width = 10

item_width = width - price_width

header_format = '%-*s%*s'
format = '%-*s%*.2f'


print "=" * width

print header_format % (item_width, 'Item', price_width, 'Price')

print '-' * width

# print each item and price by line

print format % (item_width, 'Apples', price_width, 420.563)
print format % (item_width, 'Coconuts', price_width, 450.5)
print format % (item_width, 'Dried Apricots (16 oz.)', price_width, 146.220)
print format % (item_width, 'Prunes (4 lbs.)', price_width, 256.580)
print format % (item_width, 'Cantaloupes', price_width, 50.55)

print '=' * width