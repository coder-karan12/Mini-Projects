import random

print("Guess Number Between 1 to 100")

secret = random.randint(1,100)
attempt = 0

while True:
    guess = int(input("Guess a Number: "))
    attempt = attempt + 1

    if guess == secret:
        print("Yayy! you guessed it")
        print("Attempts Taken:",attempt)
        if attempt <= 5:
            print("Gold Medal")
        elif attempt <= 7:
            print("Silver Medal")
        elif attempt <= 10:
            print("Bronze")
        break
    elif guess < secret:
        print("Too Low")
    else:
        print("Too high")