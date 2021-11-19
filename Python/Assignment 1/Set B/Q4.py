"""
Write a program which accept an integer value ‘n’ and display all prime numbers till ‘n’.
"""

def isPrime(n):
  if(n == 1 or n == 0):
    return False

  for i in range(2, n):
    if(n % i == 0):
      return False
  return True


n = int(input("Enter a number: "))

for i in range(1, n + 1):
  #check if current number is prime
  if(isPrime(i)):
    print(i, end=" ")