class Test:
    def __init__(self,name):
        self.__name = name

    def print_name(self):
        print(self.__name)




cheese = Test("Louis")
cheese.print_name()
#print(cheese.__name)
#cheese.__name = "Hello"
#print(cheese.__name)

