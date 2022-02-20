def calculate_length():
    x1 = int(input("Enter the Number of x1 Point: "))
    y1 = int(input("Enter the Number of y1 Point: "))
    x2 = int(input("Enter the Number of x2 Point: "))
    y2 = int(input("Enter the Number of y2 Point: "))

    distance = (x2 - x1) ** 2 + (y2 - y1) ** 2
    print("The Length of line is : ", distance)
calculate_length()


