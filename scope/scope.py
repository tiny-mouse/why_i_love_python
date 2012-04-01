thing = "that"

print "before the method: "+thing

def a_method():
    thing = "this"
    print "in the method: "+thing

a_method()

print "after the method: "+thing

def another_method():
    global thing
    thing = "another thing"
    print "in the other method: "+thing

another_method()

print "after the other method: "+thing

