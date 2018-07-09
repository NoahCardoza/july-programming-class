print ("This program will calculate the area of a figure.")

shapechoice = int(input("Would you like to find the area of a square (1), rectangle (2),  triangle (3), or circle (4)."))

if shapechoice == 1:
    sidelength = float(input("What's one of the sides length? "))
    area = sidelength * sidelength
    shape = "square"
elif shapechoice == 2:
    length = float(input("What is the length of the rectangle? "))
    width = float(input("What is the width of the rectangle? "))
    area = length * width
    shape = "rectangle"
elif shapechoice == 3:
    height = float(input("What is the height of the triangle? "))
    basewidth = float(input("What is the base-width of the triangle? "))
    area = height * basewidth / 2
    shape = "triangle"
elif shapechoice == 4:
    radius = float(input("What is the radius of the circle? "))
    area = (radius ** 2) * 3.14
    shape = "circle"
else:
    print ("Sorry, that's not one of the options. What a rebel!")
    exit()

print ("the area of your " + shape + " is " + str(area) + ".")
