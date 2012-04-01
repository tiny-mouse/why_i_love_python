# Notice the sys here.  In java you always have String[] args in the main.
# in python you can access the sys args anywhere

import sys

def add(a, b):
    return a+b

def subtract(a, b):
    return a-b

def multiply(a,b):
    return a*b

def divide(a,b):
    return a/b

def quotient(a,b):
    return a%b

class MathClass(object):
    def add(self, a, b):
        return a+b
    
    def subtract(self, a, b):
        return a-b
    
    def multiply(self, a, b):
        return a*b
    
    def divide(self, a, b):
        return a/b
    
    def quotient(self, a, b):
        return a%b

# notice the lack of "new"
math_class = MathClass()

functions = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'quotient': quotient
}

methods = {
    'add': math_class.add,
    'subtract': math_class.subtract,
    'multiply': math_class.multiply,
    'divide': math_class.divide,
    'quotient': math_class.quotient
}

if __name__ == "__main__":
    try: 
        print sys.argv
        if len(sys.argv) == 4:
            print "I want to ", sys.argv[1]
            print "function: ", functions['add']
            print "method: ", methods['add']
            print "Function is: ", functions[sys.argv[1]]
            print "Function gives: ", functions[sys.argv[1]](int(sys.argv[2]), int(sys.argv[3]))
            print "Class method gives: ", methods[sys.argv[1]](int(sys.argv[2]), int(sys.argv[3]))
        else:
            print "Nothing doing give me 3 args (operation, number 1, number 2)"
    except ValueError:
        print "One of your inputs was not an int"

