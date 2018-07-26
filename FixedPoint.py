#This code will be a bit different - we will put all of the outputs
#into a list, which will be put into a table
#On top of that, we will have inputs!

import numpy as np
import tabulate

#input initial guess, p, and function f as a string
p0 = float(input("Enter initial guess: "))
g0 = input("Enter function: ")
TOL = 10**float(input("Enter degree of tolerance: "))
Nmax = int(input("Enter max number of iterations: "))

#turn g into a function (requires eval)
g = lambda x: eval(g0)

#put our guess into a list
p = [p0]

#Now we run the code
N = 1
while N < Nmax:
    #overflow error
    try:
        p.append(g(p[-1])) #fixed point
    except OverflowError as err:
        print("\nFunction diverged and overflowed after p =",p[-1],err)
        quit()


    if np.abs(p[-1]-p[-2]) < TOL:
        break
    
    N += 1

#table
l = [] #to build our list
for i in range(len(p)):
    l.append([i,p[i]])

t = tabulate.tabulate(l, headers = ['N', 'p'],floatfmt=".10f")
print(t)

if N == Nmax:
    print("The method failed after",Nmax,"iterations")
