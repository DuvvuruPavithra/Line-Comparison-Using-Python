
#def calculate_length(x1, y1, x2, y2):
 #   return  (x2 - x1) ** 2 + (y2 - y1) ** 2

#length_of_line1 = calculate_length(12, 14, 24, 18)
#length_of_line2 = calculate_length(2, 14, 34, 18)

#if length_of_line1 == length_of_line2:
 #   print("The two lines lines are equal ")
#else:
 #   print("The two lines lines are not equal ")

def calculate_length():
    x1 = int(input("Enter the Number of x1 Point: "))
    y1 = int(input("Enter the Number of y1 Point: "))
    x2 = int(input("Enter the Number of x2 Point: "))
    y2 = int(input("Enter the Number of y2 Point: "))
    distance1 = (x2 - x1) ** 2 + (y2 - y1) ** 2
    print("The Length of line of x and y coordinates is : ", distance1)

    a1 = int(input("Enter the Number of a1 Point: "))
    b1 = int(input("Enter the Number of b1 Point: "))
    a2 = int(input("Enter the Number of a2 Point: "))
    b2 = int(input("Enter the Number of b2 Point: "))

    distance2 = (a2 - a1) ** 2 + (b2 - b1) ** 2
    print("The Length of line of a and b coordinates is : ", distance2)

    if distance1 == distance2:
        print("The Two distance of length of lines are equal")
    elif distance1 > distance2:
        print("The length of line one is greater than line two  ")
    else:
        print("The length of line two is greater than line one  ")

calculate_length()










