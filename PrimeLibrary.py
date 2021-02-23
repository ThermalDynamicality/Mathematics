import math
from datetime import datetime




# Inputs Range and Produces A Prime Number Array
def Generate_Prime(Lower, Upper, Debug = False):
    val = 0
    
    if Debug == True:
        before = datetime.now()

    PrimeList = []
    PrimeList.append(2)
    for i in range(3, Upper, 2):
        for p in PrimeList:
            if p <= math.sqrt(i):
                if i % p == 0:
                    val = 1
                    break
        if val == 0:
            PrimeList.append(i)
        else:
            val = 0

    Output = []
    for i in PrimeList:
        if i >= Lower:
            Output.append(i)

    if Debug == True:
        print(Output)
        after = datetime.now()
        print("Time Elapsed:", after - before)

    return Output





# Inputs N and Produces A Prime Factor Array
def Prime_Factors(n, Debug = False):
    Output = []

    if Debug == True:
        before = datetime.now()
    
    while n % 2 == 0:
        Output.append(2)
        n = n / 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            Output.append(i)
            n = n / i

    if n > 2:
        Output.append(int(n))

    if Debug == True:
        print(Output)
        after = datetime.now()
        print("Time Elapsed:", after - before)
    
    return Output





# Inputs N and Produces A Boolean
def IsPrime(n, Debug = False):
    Prime = True

    if Debug == True:
        before = datetime.now()
    
    if n % 2 == 0:
        Prime = False

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            Prime = False

    if Debug == True:
        print(Prime)
        after = datetime.now()
        print("Time Elapsed:", after - before)
    
    return Prime
