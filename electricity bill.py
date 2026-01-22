# Electricity Bill Calculator
x = int(input("Enter the units: "))

if x >= 0 and x <= 100:
  print("Your electricity bill is:",x*5)

elif x >= 101 and x <= 200:
  bill = (100*5) + ((x-100)*7)
  print("Your electricity bill is:",bill)

else:
  bill = (100*5) + (100*7) + ((x-200)*10)
  print("Your electricity bill is:",bill)