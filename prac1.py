
import string
#! Interpreted language
#! https://realpython.com/python-coding-interview-tips/
#! https://prepinsta.com/interview-preparation/technical-interview/most-asked-coding-questions-in-placements/
"""
def sr(a):
    return int(a.split(" ")[1])


s = "amy 100\ndavid 100\nheraldo 50\naakansha 75\naleksa 150"

t = s.splitlines()
for i in t:
    print(sr(i))
print(t)
t.sort(key=sr)
print(t)

numbers = [10, 9, 8, 7]
for i, num in enumerate(numbers):
    if num % 3 == 0 and num % 5 == 0:
        numbers[i] = 'fizzbuzz'
    elif num % 3 == 0:
        numbers[i] = 'fizz'
    elif num % 5 == 0:
        numbers[i] = 'buzz'
print(numbers)
print(ord("d"))
print(string.ascii_lowercase)
"""
# n = 7
# for i in range(n):
#     print((n-i)*" "+"*"*i+(n-i)*" ")
# print(("*"*i).center(7 if(i % 2 == 0) else 8, "5"))

n = 567
t = 0
rev = 0
print(n / 10)
# while t > 0:
#     t =  n%10
while n > 0:
    t = n % 10
    rev = (rev * 10)+t
    n = n//10
    # if((len(str(rev)) == len(str(n)))):
    #     break
print(rev)
print("Fibonacci sequence:")
# Program to display the Fibonacci sequence up to n-th term

nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0
while count < nterms:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1
