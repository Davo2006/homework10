#xndir5.py (Write a Python program that calculates the Fibonacci sequence up to a given number n using a while loop. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones.)
x = int(input())
y = 0
z = 1
q = 1
print(y)
print(z)
while q < x:
    q = y+z
    y = z
    z = q
print(q)