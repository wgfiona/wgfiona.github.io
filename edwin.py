while True:
    print("*****************************")
    for i in range(3):
        print("********** WELCOME **********")
    print("*****************************")
    print("This programme is able to calculate *Perimeter* *Area* and *Volume* based on the shape chosen.")
    print(" ")

    print("Choose what to calculate:")
    print("1. Perimeter")
    print("2. Area")
    print("3. Volume")
    

    choice = int(input("Enter your choice (1/2/3): "))
    print(" ")
    print("Choose the shape:")
    print("1. Circle")
    print("2. Triangle")
    print("3. Quadrilateral")
    print("4. Regular polygon(ANY NUMBER)")

    shape_choice = int(input("Enter shape choice (1/2/3/4): "))

    print(" ")
    for p in range(3):
        print("...")
    print("Process-ing")
    for p in range(3):
        print("...")
    print(" ")

    if choice == 1:
        if shape_choice == 1:
            r = float(input("Enter radius of the circle: "))
            jawapan = 2 * 3.142 * r
            
        elif shape_choice == 2:
            print("Choose the type of triangle:")
            print("1. Isosceles")
            print("2. Equilateral")
            print("3. Scalene")
            typetri = int(input("Enter the type of triangle (1/2/3): "))
            if typetri == 1:
                side1 = float(input("Enter length of side a that with the same length on both side:"))
                side2 = float(input("Enter length of side b:"))
                jawapan = (side1 * 2) + side2
               
            elif typetri == 2:
                side = float(input("Enter the length of side"))
                jawapan = side * 3
                
            else:
                side1 = float(input("Enter length of side a :"))
                side2 = float(input("Enter length of side b:"))
                side3 = float(input("Enter length of side c:"))
                jawapan = side1 + side2 + side3

        elif shape_choice == 3:
            print("Choose the type of quadralateral:")
            print("1. Square")
            print("2. Rectangle")
            print("3. Rhombus")
            typequad = int(input("Enter the type of quadrilateral (1/2/3): "))
            if typequad == 1:
                side = float(input("Enter the length of side"))
                jawapan = side * 4
               
            elif typequad == 2:
                length = float(input("Enter the length of rectangle:"))
                width = float(input("Enter the width of rectangle:"))
                jawapan = (2 * length) + (2 * width)
                
            else:
                a = float(input("Enter length of the side of a rhombus :"))
                jawapan = 4 * a
                
        else:
            lengthside = float(input("Enter the length of the side of the polygon"))
            sidepol = int(input("Enter the number of sides of the polygon:"))
            jawapan = lengthside * sidepol
           
    elif choice == 2:
        print(" ")
        print("Choose the shape:")
        print("1. Circle")
        print("2. Triangle")
        print("3. Quadrilateral")
        print("4. Cylinder")
        shape_choice = int(input("Enter shape choice (1/2/3/4): "))
        print(" ")
        for p in range(3):
            print("...")
        print("Process-ing")
        for p in range(3):
            print("...")
        print(" ")

        if shape_choice == 1:
            r = float(input("Enter radius of the circle: "))
            jawapan = 3.142 * (r * r)
            
        elif shape_choice == 2:
            print(" ")
            base=float(input("Enter base of the triangle:"))
            height=float(input("Enter height of the triangle:"))
            jawapan=(base*height)/2
            
        elif shape_choice == 3:
            print("Choose the type of quadrilateral:")
            print("1. Square")
            print("2. Rectangle")
            print("3. Parallelogram")
            typequad = int(input("Enter the type of quadrilateral (1/2/3): "))
            if typequad == 1:
                side = float(input("Enter the length of side"))
                jawapan = side * side
                
            elif typequad == 2:
                length = float(input("Enter the length of rectangle:"))
                width = float(input("Enter the width of rectangle:"))
                jawapan = length * width
                
            else:
                base = float(input("Enter the base of parallelogram:"))
                height = float(input("Enter the height of parallelogram:"))
                jawapan = base * height
                
        else:
            r = float(input("Enter radius of the circle: "))
            pi = float(input("Enter the pi you want (either 3.142 or 22/7): "))
            h = float(input("Enter the height of the cylinder:"))
            jawapan = (2 * pi * r) + (2 * pi * r * h)
            
    elif choice == 3:
        print(" ")
        print("Choose the shape:")
        print("1. Sphere")
        print("2. Pyramid")
        print("3. Cube")
        print("4. Cuboid")
        print("5. Cylinder")
        
        shape_choice = int(input("Enter shape choice (1/2/3/4): "))
        print(" ")
        for p in range(3):
            print("...")
        print("Process-ing")
        for p in range(3):
            print("...")
        print(" ")

        if shape_choice == 1:
            r = float(input("Enter radius of the circle: "))
            jawapan =  ((3.142*r*r*r)*4)/3
            

        elif shape_choice == 2:
            b=float(input("Enter base area of the pyramid: "))
            h=float(input("Enter height of the pyramid: "))
            jawapan=(b*h)/3
            
        elif shape_choice == 3:
            side=float(input("Enter length of side of the cuboid:"))
            jawapan=side*side*side
            

        elif shape_choice == 4:
            l=float(input("Enter length of the cuboid:"))
            w=float(input("Enter width of the cuboid:"))
            b=float(input("Enter breadth of the cuboid:"))
            jawapan=l*w*b
            
        else:
            r = float(input("Enter radius of the cylinder: "))
            h= float(input("Enter height of the cylinder: "))
            jawapan=3.142*r*r*h
            
      
            

    

    #to print the jawapan
    print("The answer is:", round(jawapan, 2))



    #ask if user wants to continue
    continue_choice = input("Do you want to continue to have other calculations? (Y/N): ").upper()
    #if yes,programme will restart from the beginning
    #if no,programme will not restart(no loop) and *** it end the programme after it say goodbye***
    if continue_choice != 'Y':
        break
        print(" ")
    for p in range(3):
        print("...")
    print("Process-ing")
    for p in range(3):
        print("...")
    print(" ")

print(" ")
print("Goodbye and See U Soon")

   

