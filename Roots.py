a = [-60, -19, 7, 2]



def Factors(v):
    v = abs(v)
    factors = []
    for i in range(1, v):
        if v % i == 0:
            factors.append(i)
            factors.append(-i)

    return factors



def Zeros(lst, factors):
    zeros = []
    for i in factors:
        sum = 0
        for j in range(0, len(lst)):
            sum += a[j] * (i ** j)
        if sum == 0: zeros.append(i)
    
    return zeros



def Division(lst, r):
    lst = list(reversed(lst))
    output = [lst[0]]
    for i in range(0, len(lst) - 1):
        output.append(lst[i + 1] + r * output[i])
    
    output = list(reversed(output))
    if output[0] == 0: return output[1:]
    else: print("Error Occured..."); return output



zeros = Zeros(a, Factors(a[0]))



for i in zeros: a = Division(a, i)

if len(a) == 2:
    z = -a[0] / a[1]
    zeros.append(z)

if len(a) == 3:
    c = -a[1] / (2 * a[2])
    d = (a[1] ** 2 - 4 * a[2] * a[0]) ** 0.5 / (2 * a[2])
    z1 = c + d
    z2 = c - d
    zeros.append(z1)
    zeros.append(z2)



print(zeros)