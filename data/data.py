# I don't even need a method, it can just be a script.
# Notice the lack of types or private/public.  You just declare and instantiate variables when/where you need them.
'''
lalala

'''
"""
 more comments
"""
a_tuple = ("an", "ordered", "immutable", "listish", "type")

data_types = {
    1: "one",
    "tuple": a_tuple,

    "dict": {
        1: "some string",
        "another string": 3,
        a_tuple: "is a cool key"
    },
    
    "string": "just a string",
    "char": 'achar',
    
    "double": 1.0,
    
    "int": 10,
    # Notice the items in the list are not of the same type
    "list": [a_tuple, 1.0, "a string"],
    "boolean": False,
    None: "whatever",
    # notice i can leave a trailing comma on this line so it's easy to add more elements
    # and not have to go back to add one
    True: "it's true dude",
    56: "whatever",
    "hshshs": "kksk",
}

for key, value in data_types.iteritems():
    print "\nkey: {0} of type: {1} has value: '{2}' of type: {3}".format(key, type(key), value, type(value))


