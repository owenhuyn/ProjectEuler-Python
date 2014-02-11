def prime(n):
  i=2
  while (n%i != 0 and i < n):
    i += 1
  if (i < n):
    return prime (n/i)
  else:
    print("The highest prime factor is: "),n

print("Enter a number to find its highest prime factor")
n=input()
prime(n)
