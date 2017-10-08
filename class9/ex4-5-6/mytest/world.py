def func1():
    print "func1"

class MyClass():
    
    def __init__(self,var1, var2, var3):
        self.var1 = var1
        self.var2 = var2
        self.var3 = var3

    def hello(self):
        print "Hello {}! Please {} your {}.".format(self.var1, self.var2, self.var3)

    def not_hello(self):
        print "Goodbye {}! Please {} your {}.".format(self.var1, self.var2, self.var3)


class MyChildClass(MyClass):

    def __init__(self,*args):
        MyClass.__init__(self, *args) 
        self.var4 = "Come in!"

    def hello(self):
        print "Greetings {}! Please {} your {}. {}".format(self.var1, self.var2, self.var3, self.var4)

if __name__ == "__main__":
    print "world executable code!"
