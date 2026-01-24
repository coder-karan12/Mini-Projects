# Python Program which adds number until user stops inputting number

print("Welcome")
print("To Quit press 'q'")
sum = 0
while (True):
    userInput = input("Enter The Price: ")
    if (userInput!='q'):
        sum = sum + int(userInput)
        print(f"Order total so far: {sum}")

    else:
        print("Thanks for using our calculator")
        print(f"Your Bill total is {sum}. Thanks for shopping with us")
        break
