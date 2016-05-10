

''' sample code to convert temp'''

# test commit from pycharm community edition

input_temp = input("Please enter temp tp convert :")
target_metric = raw_input("Convert to (F)ahrenheit or (C)elsius?: ")



if target_metric =='F':
    converted_temp = (9.0 / 5.0) * input_temp + 32
    print 'Converted temp is: %s' % converted_temp
elif target_metric =='C':
    converted_temp = (5.0 / 9.0)*(input_temp-32)
    print 'Converted temp is: %s' % converted_temp
else:
    print "please enter valid metric to convert"

