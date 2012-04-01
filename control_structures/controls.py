import random

# Notice the two types of printing in this method.
# the % is the old style and the {0} format is the new style.
def if_statement():
    print "IF STATEMENT"
    num = random.choice(range(10))
    print "The random we got is: %d" % num
    if num < 5:
        print "%s is less than 2" % num
    elif num > 1 and num < 6:
        print "{0} is greater than 1 and less than 6".format(num)
    else:
        print "{0} don't care".format(num)

def while_loop():
    # Notice you don't need to actually put anything after the print and it'll just print an empty line."
    print
    print "WHILE STATEMENT"
    num = random.choice(range(3,10))
    while num > 0:
        print "While loop num: %s" % num
        num -= 1

def for_loop():
    print
    print "FOR STATEMENT"
    for i in range(10):
        print "for loop iteration: %s" % i

def list_iterator():
    print 
    print "LIST ITERATOR"
    # notice lists are not of fixed length, they can be resized
    lista = []
    [lista.append(i) for i in range(10)]
    print lista

def for_dict_loop():
    print 
    print "DICT ITERATION"
    dicta = dict([(i, i+10) for i in range(10)])
    print dicta
    dicta = dict(zip(range(10), range(10,20)))
    print dicta
    print "\nfor dict loop using keys"
    for key in dicta.keys():
        print "key: {0} has value: {1}".format(key, dicta[key])
    print "\nfor dict loop using iteritems"
    for key, value in dicta.iteritems():
        print "key: {0} has value: {1}".format(key, value)


if __name__ == "__main__":
    if_statement()
    while_loop()
    for_loop()
    list_iterator()
    for_dict_loop()
