#This code takes in a function, two arguments a and b, and
#tests whether f(a) and f(b) are of different signs; if so, 
#we try to find a zero in between a and b

import numpy as np 


#This function takes in a function f, bounds a and b, a maximum iteration counter Nmax,
#and an error bound of err- once our answer <= err, we can agree on the
#solution

#Just to clear up the code a bit
def print_state(N,a,b,p,err_abs,err_rel):
    print("\nN = ",N)
    print("a = ",a)
    print("b = ",b)
    print("p = ",p)
    print("f(p) = ", f(p))
    print("Absolute error",err_abs)
    print("Relative error:",err_rel,"\n")


def bisection_method(f,a,b,Nmax,errmax):

    #Here, a zero was found at one of the bounds
    if np.sign(f(a))*np.sign(f(b)) == 0:
        if f(a) == 0:
            print("Zero at bound; f(",a,") = 0")
            quit()
        else:
            print("Zero at bound; f(",b,") = 0")
            quit()

    #Error check, we need f(a) and f(b) to be of different signs        
    if np.sign(f(a))*np.sign(f(b)) == 1:
        print("Invalid range; we need f(a) and f(b) to be of different signs")
        quit()
    
    #Now we run the code
    N = 1 #iteration counter
    p2 = 0 #temporary variables for error analysis
    err_abs = 0
    err_rel = 0

    #Print the initial states
    p = (a+b)/2
    print("\nN = ",N)
    print("a = ",a)
    print("b = ",b)
    print("p = ",p)
    print("f(p) = ", f(p), "\n")

    N += 1    

    ###
    # Here we run the code once to get things going, in order to correctly
    #get the errors on the correct step

    #Implies that p is to the right of the zero
    if np.sign(f(a))*np.sign(f(p)) == -1:
        b = p
    else: #p is to the left of the zero
        a = p

    p2 = (a+b)/2
    if f(p2) == 0:
        print("Found a zero at p = ", p2)
        quit()
    
    #Error analysis
    err_abs = np.abs(p2-p)
    err_rel = err_abs/np.abs(p)

    print_state(N,a,b,p2,err_abs,err_rel)

    N += 1

    while N <= Nmax:


        #Implies that p is to the right of the zero
        if np.sign(f(a))*np.sign(f(p2)) == -1:
            b = p2
        else: #p is to the left of the zero
            a = p2

        p2 = (a+b)/2
        if f(p2) == 0: #We found a zero!
            print("Exact zero found!")
            print_state(N,a,b,p2,err_abs,err_rel)          
            quit()

        #Now we compute the error
        err_abs = np.abs(p2-p)
        err_rel = err_abs/np.abs(p)

        if err_abs < errmax:
            print("\nZero found near:", p2)
            print_state(N,a,b,p2,err_abs,err_rel)        
            quit()


        #Progress

        #Also, let's print a table!
        print_state(N,a,b,p2,err_abs,err_rel)

        p = p2
        N += 1

    #Nmax was reached and we did not find a suitable number
    print("Function maxed out without converging to a solution")




####CODE

#Just to get the code running, define your function here
def f(x):
    return x*np.cos(x) - 2*x**2 + 3*x - 1

a = 1.2
b = 1.3
Nmax = 20
errmax = 10**(-5)

bisection_method(f,a,b,Nmax,errmax)
