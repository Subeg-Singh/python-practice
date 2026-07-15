num=int(input('enter a number:'))

class Calculator:

    @staticmethod
    def sq(num):
        return num ** 2
    
    @staticmethod
    def cube(num):
        return num ** 3
    
    @staticmethod
    def sqrt(num):
        return num ** (0.5)
    
calc=Calculator()
ob1=calc.sq(num)
obj2=calc.cube(num)
obj3=calc.sqrt(num)

def Choice():

    while True:

        choice=int(input('type 1 for square, 2 for cube, 3 for square root'))

        if choice==1:
            print(f'square of {num} is {ob1}')

        elif choice==2:
            print(f'cube of {num} is {obj2}')

        elif choice==3:
            print(f'square root of {num} is {obj3}')

        else:
            print('INVALID CHOICE')

        ch=input('do you want to continue? (y/n): ')

        if ch in 'nN':
            print('thank you for using the calculator')
            break
    
Choice()