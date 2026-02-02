# Marking system
x = int(input("Enter Marks: "))
if x <= 100 and x >= 90:
  print("Grade A")
elif x <= 89 and x >= 75:
  print("Grade B")
elif x <= 74 and x >= 50:
  print("Grade C")
elif x <= 49 and x >= 35:
  print("Grade D")
elif x < 35:
  print("Fail")