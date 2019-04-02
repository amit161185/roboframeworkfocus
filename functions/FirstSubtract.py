class FirstSubtract:

    def __init__(self,no3,no4):
        print("you are in subtract class and its obj creation done@@")

    def sub(self,a,b):
        if (a>b):
            minus =a-b
            print("value after subtract:",minus)
        elif(a < b):
            print("a is small than b")


print("hello subtract class" , __name__)
