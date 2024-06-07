#xndir4.py (Write a Python program that generates a random number between 1 and 100 and asks the user to guess the number. The program should give hints whether the guessed number is too high or too low until the correct number is guessed.)
x = int(input("Guess a number from 1-100 "))
y = 7
while y != x:
    if y > x:
        print("Try higher")
    else:
        print("Try lower")
    x = int(input())
print("You guessed it")