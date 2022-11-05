#Formula Counter Application Program by Muhammad Amaradipta
from time import sleep


def menu():
    print ('Menu')
    print
    print ('1. Triangle')
    print ('2. Rectangle')
    print ('3. Odd and Even Numbers')
    print ('4. Quit')

def Triangle():
    print ('Calculate the Area of the Triangle')
    b = float(input('Input base: '))
    h = float(input('input height: '))
    area = (b*h)/2
    print ('the Area of the Triangle is: ', area)
    print
    print ('Back to Menu (y/n)?')
    back = input().lower()
    if back =='y':
        menu()
    else:
        exit()

def Rectangle():
    print ('Calculate the Area of the Rectangle')
    l = float(input('Input length: '))
    w = float(input('input width: '))
    area = (l*w)
    print ('the Area of the Rectangle is: ', area)
    print
    print ('Back to Menu (y/n)?')
    back = input().lower()
    if back =='y':
        menu()
    else:
        exit()

def OddEven():
    print ('Determine Odd and Even Number')
    print()
    number = int(input("Input Number: "))
    if(number % 2 == 0):
        print("Number", number, "is Even Number.")
    else:
        print("Number", number, "is Odd Number.")
    print
    print ('Back to Menu (y/n)?')
    back = input().lower()
    if back =='y':
        menu()
    else:
        exit()

menu()

while 1:
    choose = int(input("Choose Menu: "))
    if choose==1:
        Triangle()
    elif choose==2:
        Rectangle()
    elif choose==3:
        OddEven()
    elif choose==4:
        print('Thank You')
        sleep(2)
        break
    else:
        print('---')
        print('Try Again?(y/n)?')
        coba=input().lower()
        if coba =='y':
            menu()
        else:
            print ('\n'*100)
            break