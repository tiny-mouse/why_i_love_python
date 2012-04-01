thing = "that"

print "before the function: "+thing

def a_function():
    thing = "this"
    print "in the function: "+thing

a_function()

print "after the function: "+thing

def another_function():
    global thing
    thing = "another thing"
    print "in the other function: "+thing

another_function()

print "after the other function: "+thing

