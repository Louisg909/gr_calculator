class Test:
    def __init__(self,name):
        self.__name = name

    def print_name(self):
        print(self.__name)


ind = ["\\mu",
           "\\nu",
           "\\alpha",
           "\\beta",
           "\\lambda",
           "\\eta",
           "\\sigma",
           "\\omega",
           ]


#cheese = Test("Louis")
#cheese.print_name()
#print(cheese.__name)
#cheese.__name = "Hello"
#print(cheese.__name)


class Metric:
    def __init__(self, metric:list[list]=None, symbol="g"):
        if metric != None:
            self.metric = metric
        else:
            self.metric = [[-1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

        self.symbol = symbol

    def symbolise(self,*args):
        string = self.symbol +"_{"
        for arg in args:
            string += arg
        string += "}"
        return string

    def covarient(self):



g = Metric()

print(g.symbolise(ind[0],ind[1]))

# Index writen in numbers when forming the equations, it just numbers the indexes, and then translates them into greek letters by working its way through the "ind" list, which includes all the possible index names in order of preference. Once the list is used up, it goes through them again, numbering them.





