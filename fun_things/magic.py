#print zip(range(10), range(10,20))

#print "\nLet's convert to binary"
#for i in range(20):
    #print "Decimal: %s -> Binary: %s" % (i, bin(i))

def multi_values():
    return "this", "that", 1

vals = multi_values()
for val in vals:
    print val


one, two, three = multi_values()
print one, two, three


