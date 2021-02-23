import statistics as stats
import scipy.stats
import matplotlib.pyplot as plt
import numpy as np



class Statistics():
    def __init__(self, x_list, y_list):
        self.x = x_list
        self.y = y_list

    def SquareSum(self, lst, lst2 = None):
        v = 0
        if lst2 == None:
            for i in range(0, len(lst)): 
                v += lst[i] ** 2
        else:
            for i in range(0, len(lst)): 
                v += lst[i] * lst2[i]
        return v

    def Reduce(self, lst, n):
        output = []
        for i in range(0, len(lst)):
            output.append(lst[i] - n)
        return output
    
    def run(self, P = False, p = False):
        x_mean = stats.mean(x)
        y_mean = stats.mean(y)
        x_r = self.Reduce(x, x_mean)
        y_r = self.Reduce(y, y_mean)
        Sxx = self.SquareSum(x_r)
        Syy = self.SquareSum(y_r)
        Sxy = self.SquareSum(x_r, y_r)

        r = Sxy / ((Sxx * Syy) ** 0.5)
        self.b = b = Sxy / Sxx
        self.a = a = y_mean - b * x_mean

        e = []
        for i in range(0, len(x)): e.append(y[i] - self.y_hat(x[i]))
        See = self.SquareSum(e)
        s_residual = (See / (len(e) - 2)) ** 0.5
        Critical = 	3.891
        CI = [-Critical * s_residual / (len(e) ** 0.5), Critical * s_residual / (len(e) ** 0.5)]

        if p:
            print(f"X Mean: {x_mean}\nY Mean: {y_mean}\n")
            print(f"Reduced X: {x_r}\nReduced Y: {y_r}\n")
            print(f"Sxx: {Sxx}\nSxy: {Sxy}\nSyy: {Syy}\n")
            print(f"a: {a}\nb: {b}\nr: {r}\nr^2: {r ** 2}\n")
            print(f"Residual: {e}\n")
            print(f"Inverval of Confidence: {CI}, z = {Critical} Confidency\n")
        
        if P:
            X = np.linspace(min(x), max(x), 256)
            plt.stem(x, e, use_line_collection = True)
            plt.axhline(y = CI[0], color='g')
            plt.axhline(y = CI[1], color='g')

            #plt.stem(x, y, use_line_collection = True)
            #plt.plot(X, self.a + self.b * X)
            #plt.plot(X, phi + m * X)
            plt.show()


    def y_hat(self, x):
        return self.a + self.b * x
    

    

    


#x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
#y = [1,2,3,4,5,6,7,4,3,4,4,5,6,7,8,7]



''' Random Number Generator For Testing '''
'''m = 0.1415926535
phi = 50
n = 500
x = []
for i in range(0, n): x.append(i)
y = []
for i in range(0, n): 
    sign = np.random.randn()
    if sign >= 0.5: sign = -1
    else: sign = 1
    y.append(12 * sign * np.random.rand() + i * m + phi)
print(f"{x}\n{y}")




#print(f"{x_prime}\n{y_prime}")

'''


y = [4.35,4.52,4.64,4.75,4.63,4.81,4.72,4.61,5.03,4.87,4.98,5.11,5.25,5.39,6.68,7.65,7.71,7.82,7.65,7.7,7.35,6.23,6.09,6.91,7.09,8.68]
x = []
for i in range(0, len(y)): x.append(i)

Statistics(x, y).run(True, True)
print("8.68")


#Statistics(x_prime, y_prime).run(True, True)






''' Intervals
95% = 1.96
99% = 2.576
99.5% = 2.807
99.9% = 3.291
99.99% = 3.891
'''




































'''

B, A, R, P, Se = 

def y(x): return A + B * x

E = []
for i in range(0, len(X[1])):
    E.append(X[1][i] - y(X[0][i]))

print(stats.mean(E))
S_ee = stats.stdev(E)
print(S_ee)
'''







'''



print(scipy.stats.linregress(x, y))




#def regression(lst):


'''



