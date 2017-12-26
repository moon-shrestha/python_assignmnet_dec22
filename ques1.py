''' Ask for a number (n) as an input from user. Using the use input (n), write a program to generate a dictionary
that contains (i, i*i) where i is key and i*i is a value for numbers between the range 1 and n (both included).
and then the program should print the dictionary.'''

num = int(input("Enter a number:"))

loop = {}

for i in range(num):
    loop[i] = i * i

print(loop)

