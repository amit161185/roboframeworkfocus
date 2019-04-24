import functions.FirstSubtract
import csvoperation.csvread


class FirstAdd:
    def __init__(self,no1,no2):
        print( "a new instance got made")

    def sum(self,a,b):
        add = a + b
        print("two values added:", add)




if __name__ == '__main__':

    #first add class obj
    obj1add = FirstAdd(2,3)
    obj1add.sum(2, 3)
    FirstAdd.sum(obj1add,3,4)

    #first subtract class obj
    ob2_sub = functions.FirstSubtract.FirstSubtract(6, 5)
    ob2_sub.sub(6,4)
    obj3_sub = functions.FirstSubtract.FirstSubtract(7,8) # (first no should be large a-b)
    obj3_sub.sub(7,8)
    obj3_sub.showcsvdata()

    # csvread class obj
    #csvread_obj1 = csvoperation.csvread.CsvReadfile()

    #csvread_obj1.csvreadmethod()





