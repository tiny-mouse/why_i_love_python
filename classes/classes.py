class AClass(object):
    attribute = "some attribute"

    def some_method(self):
        print self.attribute

class AnotherClass(AClass):

    def some_other_method(self):
        print "My attribute is: %s" % self.attribute

"""
    Notice the main method has nothing to do with the class.
    Also, notice that the filename has nothing to do with the class.
"""
if __name__ == "__main__":
    a_class = AnotherClass()
    a_class.some_other_method()
