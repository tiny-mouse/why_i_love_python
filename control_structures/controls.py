import random

def if_statement():
    print "IF STATEMENT START"
    num = random.choice(range(10))
    print "The random we got is: %d" % num
    if num < 5:
        print "%s is less than 2" % num
    elif num > 1 and num < 6:
        print "{0} is greater than 1".format(num)
    else:
        print "{0} don't care,".format(num)
    print "IF STATEMENT END"

def while_loop():
    # Notice you don't need to actually put anything after the print and it'll just print an empty line."
    print
    print "WHILE STATEMENT START"
    num = random.choice(range(3,10))
    while num > 0:
        print "While loop num: %s" % num
        num -= 1
    print "WHILE STATEMENT END"

def for_loop():
    print
    print "FOR STATEMENT START"
    for i in range(10):
        print "for loop iteration: %s" % i
    print "FOR STATEMENT END"


if __name__ == "__main__":
    if_statement()
    while_loop()
    for_loop()
