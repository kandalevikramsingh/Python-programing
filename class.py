class My_class:
    def __init__(self,name): 
        self.name = name

    def  fun(self,country):
         print("hello",self.name,country)
    
Second= My_class
my = Second("dhoni")
my.fun("india")
