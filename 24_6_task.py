l1=[[1, 2], [3, 4], [5, 6]]
flat = [i for j in l1 for i in j]
print(flat)
#From a nested list [[2, 5], [7, 9], [12, 15]], extract all even numbers.
nested = [[2, 5], [7, 9], [12, 15]]
evens = [num for sl in nested for num in sl if num % 2 == 0]
print(evens)
#Create a list of squares for numbers from 1 to 20.
squares = [x**2 for x in range(1, 21)]
print(squares)
#Print prime numbers between 10 to 20 using list comprehension
primes = [x for x in range(10, 21) if all(x % i != 0 for i in range(2, x))]
print(primes)
#Convert a=10 int data type to 10 string data type  with out using str()?
a = 10
s = "{}".format(a)
print(s, type(s)) 
#Write a Python program to swap the case of each character in a given string without using the built-in swapcase() method.
name = "UMA ARUNDATHI"
swapped = ''.join([char.lower() if char.isupper() else char.upper() for char in name])
print(swapped)
#Write a list comprehension to print only the word 'python' from the list.
#S=[ ‘python’ ,’java’ , ‘c++’ , ‘developer’ ]
S = ['python', 'java', 'c++', 'developer']
result = [word for word in S if word == 'python']
print(result)