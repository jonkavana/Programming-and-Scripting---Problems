# John Kavanagh
# check if a number is a prime
# primes are 2, 3, 5, 7, 11, 13, 17, 19

p = 221
m = 2
isprime = True

while m < p:
    if p % m == 0:
      isprime = False
      break
    m = m + 1

if isprime:
    print (p, "is a prime number.")
else:
    print(p, "is not prime.")
    