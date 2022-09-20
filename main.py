def PrimeNum(n):
  d = 2
  while n % d != 0:
    d += 1
  return d == n
num = int(input())
print("Простое") if PrimeNum(num) else print("Непростое")
