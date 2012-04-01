'''
OMG the sub and super classes are in the same file!?!?!  WHAAAAAAAA?????

Notice the lack of braces.  Also, a colon is used for things that denote scope changes.
'''
attribute = "whatever dude"

class AClass(object):
    attribute = "some attribute"

    def some_method(self):
        global attribute
        print "global variable in some_method", attribute
        attribute = "would this change anything"
        # notice the changes between single and double quotes.  It doesn't matter.
        attribute += '?'
        print attribute

'''
    This is a subclass of AClass
'''
class AnotherClass(AClass):

    def some_other_method(self):
        print "My attribute is: %s" % self.attribute

"""
    Notice the main method has nothing to do with the class.
    Also, notice that the filename has nothing to do with the class.
"""
if __name__ == "__main__":
    a_class = AnotherClass()
    a_class.some_method()
    a_class.some_other_method()
