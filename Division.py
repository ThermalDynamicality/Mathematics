class PolyDiv():
    def __init__(self, numerator, denominator):
        self.numerator   = list(reversed(numerator))
        self.denominator = list(reversed(denominator))
    
    def reduce(self, iterations):
        f = self.numerator; g = self.denominator
        d = len(f) - len(g) - 1
        result = [None] * d; i = 0
        
        while i < iterations:
            k = f[0] / g[0]
            result[d] = k
            for j in range(0, len(g)):
                f[j] = f[j] - k * g[j]
            f = f[1:]
            i += 1

        return result

    def decompose(self, remainder = True):
        f = self.numerator; g = self.denominator

        result = [] * (len(f) - len(g))
        while len(f) >= len(g):
            k = f[0] / g[0]
            result.append(k)
            for j in range(0, len(g)):
                f[j] = f[j] - k * g[j]
            f = f[1:]
        
        result = list(reversed(result))
        if remainder == True: result.append(f)
        return result
    
    def remainder(self):
        f = self.numerator; g = self.denominator

        while len(f) >= len(g):
            k = f[0] / g[0]
            for j in range(0, len(g)):
                f[j] = f[j] - k * g[j]
            f = f[1:]

        return f



f = [7, -2, 3, -1, 0, 2]
g = [-60, -19, 7, 2]

    

print(PolyDiv(f, g).reduce(1))
print(PolyDiv(f, g).reduce(2))
#print(PolyDiv(f, g).decompose())
#print(PolyDiv(f, g).remainder())













'''def printPolynomial(lst, delta = 0):
    lst = list(reversed(lst))
    d = len(lst) - 1 + delta
    phrase = ""

    if lst[d] < 0: phrase += "-"
    while d >= delta + 1:
        if lst[d] != 0:
            if abs(lst[d]) != 1:
                phrase += f"{abs(lst[d])}"
            
            if d > 1:
                phrase += f"x^{d}"
            elif d == 1:
                phrase += "x"

            if lst[d - 1] < 0:
                phrase += " - "
            else:
                phrase += " + "
        d -= 1
    phrase += str(abs(lst[0]))
    return str(phrase)'''