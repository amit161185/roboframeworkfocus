import functions.FirstSubtract


class FirstAdd:
    def __init__(self,no1,no2):
        print( "a new instance got made")

    def sum(self,a,b):
        add = a + b
        print("two values added:", add)




if __name__ == '__main__':
    obj1 = FirstAdd(2,3)
    obj1.sum(2, 3)
    
    FirstAdd.sum(obj1,3,4)
    ob2sub = functions.FirstSubtract.FirstSubtract(6, 5)
    ob2sub.sub(6,4)
    obj3sub = functions.FirstSubtract.FirstSubtract(7,8) # (first no should be large a-b)
    obj3sub.sub(7,8)




