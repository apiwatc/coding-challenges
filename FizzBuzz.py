"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.
"""


def fizzBuzz(n):
    fizzbuzz = []
    for i in range(1, n+1):
        if i % 3 == 0 and i % 5 == 0:
            fizzbuzz.append('FizzBuzz')
        elif i % 3 == 0:
            fizzbuzz.append('Fizz')
        elif i % 5 == 0:
            fizzbuzz.append('Buzz')
        else:
            fizzbuzz.append(str(i))
    return fizzbuzz


n = 15
print(fizzBuzz(n))
