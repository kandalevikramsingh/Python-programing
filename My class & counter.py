##my_counter=0
##def fun():
##    global my_counter
##    my_counter= my_counter +1
##    print("Vicky",my_counter)
##    while my_counter <=100:
##        fun()
##fun()        

##class My_class:
##    def fun():
##        print("vicky")
##My_class.fun()        


##class My_class:
##    def fun(name):
##        print("vicky",name)
##my =My_class
##my.fun("sonali")

##class My_class:
##    def fun(name):
##        print("vicky",name)
##    def fun1(name):
##        print("hi",name)
##
##my =My_class
##my.fun("sonali")
##my.fun1("vicky")

class My_class:
    def __init__(self,name):
        self.name = name
        
    def fun(self):
        print("vicky",self.name)
        
    def fun1(self):
        print("hi",self.name)
        
my = My_class("sonali")
my.fun1()
my.fun()
