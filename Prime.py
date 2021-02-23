import math

def isPrime(n):
    if n % 2 == 0: return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0: return False
    
    return True


print(isPrime(13))

n = 400

for x in range(3, n):
    f_0 = int((x - 1) / math.log(x - 1, math.e))
    f_1 = int(x / math.log(x, math.e))
    if f_0 != f_1: print(f"{x}")


'''
print(isPrime(p - 2), p - 2)
print(isPrime(p - 1), p - 1)
print(isPrime(p), p)
print(isPrime(p + 1), p + 1)
print(isPrime(p + 2), p + 2)'''