import math

# format using width and precision

# width 10
print '%10f' % math.pi

# width 10 and precision 2
print '%10.2f' % math.pi


# width 10 and precision 10
print '%10.10f' % math.pi


# padding value with 0

print '%010.2f' % math.pi


# left align using - sign

a = 1132255.256
print '%-10.3f' % a
print '%-10.3f' % math.pi

# " " before width gives sign before number for non positive number
b = -103222.25
print '% 10.3f' % a
print '% 10.3f' % b


# + sign will add sign before all number
print '%+10.3f' % a
print '%+10.3f' % b
