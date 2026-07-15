import random
a=random.randint(1,100)
num=int(input('choose a number from 1 to 100:'))
count=0
def game(a,num,count):
    while True:
        if num==a:
            print('You guessed it right!')
            count+=1
            break
        elif num<a:
            print(f'Choose a number bigger than {num} from 1 to 100')
            count+=1
            num=int(input('choose a number:'))
        elif num>a:
            print(f'Choose a number smaller than {num} from 1 to 100')
            count+=1
            num=int(input('choose a number:'))
    print(f'you guess the number in {count} turns!')

game(a,num,count)