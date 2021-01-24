def is_prime(x):
  a = 0
  for i in range(2,x):
    if x%i == 0:
      a = 1
  if a == 0:
    print("prime number")
  else:
    print("not a prime numer")
    return True
def print_primes_between(y,z):
  for i in range(y,z):
    a = 0
    for j in range(2,i):
      if i%j == 0:
        a = 1
    if a == 0:
      print(i)
x = int(input("Enter an integer: "))
is_prime(x)
y  = int(input("Enter the lower integer: "))
z = int(input("Enter the higher integer: "))
print_primes_between(y,z) 
