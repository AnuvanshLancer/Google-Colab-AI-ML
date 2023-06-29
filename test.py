from math import pi
def circle():
    print('Do you want to Find the are of circle with Diamerter or Radius?')
    circle_choice = input('(D == Diamerter), (R == Radius) => ')

    if circle_choice == 'D':
        Diameter = float(input('Enter the Diamerter = '))
        radius = Diameter / 2
        Area_of_Circle = pi * radius**2
        print('The area of the circle is', Area_of_Circle)

    elif circle_choice == 'R':
        radius = float(input('Enter the Radius = '))
        Area_of_Circle = pi * radius**2
        print('The area of the circle is', Area_of_Circle)
    
    else:
        print('Invalid choice! Please try again.')
        circle()


def square():
    s = int(input('Enter the length of the side of the square: '))
    print('Area of the Square is', s * s)


def rectangle():
    l = int(input('Enter the length : '))
    b = int(input('Enter the breadth : '))

    print('The area is ', l * b)


def main():

    print('Welcome to the Area finder')
    print('''Choose your figure
    C == Circle
    S == Square
    R == Rectangle
    !! if you are not able to finder your desired shape/figure. Please contact on anuvanshlancer.official@gmail.com''')
      
    choice = input('Choose: ')

    if choice == 'C':
        circle()

    elif choice == 'S':
        square()

    elif choice == 'R':
        rectangle()

    else:
        print('Invalid Input!')
        print('Try Again!')
        main()


while True:
    main()
    
