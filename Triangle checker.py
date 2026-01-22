# Triangle Type Checker 

side1 = int(input("Enter Side1: "))
side2 = int(input("Enter Side2: "))
side3 = int(input("Enter Side3: "))

if side1 <= 0 or side2 <= 0 or side3 <=0:
  print("Invalid triangle, sides must be positive")

elif (side1+side2>side3) and (side1+side3>side2) and (side2+side3>side1):
  
  if side1 == side2 == side3:
    print("Triangle is Equilateral")
  
  elif side1 == side2 or side2 == side3 or side3 == side1:
    print("Triangle is Isoceles")
  
  else:
    print("Triangle is Scelene")

else:
  print("Invalid triangle, please enter the correct sides")