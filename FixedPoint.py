#This code will be a bit different - we will put all of the outputs
#into a list, which will be put into a table
#On top of that, we will have inputs!

import numpy as np
import tabulate

def FixedPoint(p0, g0, TOL, Nmax):
    #turn g into a function (requires eval)
    g = lambda x: eval(g0)

    #put our guess into a list
    p = [p0]    
    err_abs = [0]
    err_rel = [0]

    #Now we run the code
    N = 1
    while N < Nmax:
        #overflow error
        try:
            p.append(g(p[-1])) #fixed point
        except OverflowError as err:
            print("\nFunction diverged and overflowed after p =",p[-1],err)
            break

        #error 
        err_abs.append(np.abs(p[-1]-p[-2]))
        err_rel.append(err_abs[-1]/np.abs(p[-2]))

        if err_abs[-1] < TOL:
            break
        
        N += 1

    if N == Nmax:
        print("\nThe method failed after",Nmax,"iterations")

    #table
    l = [] #to build our list
    for i in range(len(p)):
        if i == 0:
            l.append([i,p[i],'-','-'])
            continue
        l.append([i,p[i],'%E' % err_abs[i],'%E' % err_rel[i]])

    t = tabulate.tabulate(l, headers = ['N', 'p',"absolute error","relative error"],floatfmt=".10f")
    return(t)


if __name__ == "__main__":
    #input initial guess, p, and function f as a string
    p0 = float(input("Enter initial guess: "))
    g0 = input("Enter function: ")
    TOL = 10**float(input("Enter degree of tolerance: "))
    Nmax = int(input("Enter max number of iterations: "))

    print(FixedPoint(p0,g0,TOL,Nmax))
