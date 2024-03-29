# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!

def factorial(x):
    total=1
    while x>0:
        total=x*total
        x-=1
    return total

a = []
for char in str(factorial(100)):
    a.append(int(char))

print(sum(a))