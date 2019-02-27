import functions.firstsubtract


class FirstAdd:
    def __init__(self,no1,no2):
        print( "a new instance got made")

    def sum(self,a,b):
        add = a + b
        print(add)




if __name__ == '__main__':
    obj1 = FirstAdd(2,3)
    obj1.sum(2, 3)
    
    FirstAdd.sum(obj1,3,4)
    ob2sub = functions.firstsubtract.FirstSubtract(6,5)
    ob2sub.sub(6,4)





