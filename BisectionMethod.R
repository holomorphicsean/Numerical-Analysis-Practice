#The R Implementation of the Bisection Method
#Answers will go into vectors, and we'll be creative with the data output
options(digits = 15)

#gets last element of a vector
last <- function(vec, n = 1) {
  return(vec[length(vec) - n + 1])
}

#packages the vectors into a nice data frame
package <- function(a,b,p,fp,errAbs,errRel) {
  n = c(1:length(a))
  i <- data.frame(
    n <- n,
    a <- a,
    b <- b,
    p <- p,
    fp <- fp,
    errAbs <- errAbs,
    errRel <- errRel)
  
  return(i)
}

BisectionMethod <- function(f,a,b,Nmax,errmax) {
  
  #First we check whether there is a zero in between the bounds
  if (sign(f(a))*sign(f(b)) == 1) {
    print("Zero not guaranteed to be between bounds")
    return()
  }
  
  if (sign(f(a))*sign(f(b)) == 0) {
    print("Zero found on one of the bounds")
    ifelse(f(a) == 0, cat("zero on a =",a,"\n"), cat("zero on b =",b,"\n"))
    return()
  }
  
  #Define parameters
  aa <- a
  bb <- b
  p <- (a+b)/2
  fp <- f(p)
  N <- 1
  errAbs <- 0
  errRel <- 0
  
  ####Now we run the code once to get the error analysis started
  if( f(p) == 0 ) {
    cat("Found an exact zero at ", p,"\n")
    return()
  }
  if ( sign(f(a))*sign(f(p)) == -1 ) {
    bb <- c(bb,p)
    aa <- c(aa,a)
  } else {
    aa <- c(aa,p)
    bb <- c(bb,b)
  }
  
  p <- c(p, .5*(last(aa) + last(bb)))
  fp <- c(fp, f(last(p)))
    
  errAbs <- c(errAbs, abs(last(p) - last(p,2)))
  errRel <- c(errRel, last(errAbs)/last(p,2))
  
  N <- N + 1
  ##############
  #Now let's run
  while (N < Nmax) {
    
    if( f(last(p)) == 0 ) {
      cat("Found an exact zero at ", p,"\n")
      output <- package(aa,bb,p,fp,errAbs,errRel)
      return(output)
    }
    if ( sign(f(last(aa)))*sign(f(last(p))) == -1 ) {
      bb <- c(bb,last(p))
      aa <- c(aa,last(aa))
    } else {
      aa <- c(aa,last(p))
      bb <- c(bb,last(bb))
    }
    
    p <- c(p, .5*(last(aa) + last(bb)))
    fp <- c(fp, f(last(p)))
    
    #error analysis
    errAbs <- c(errAbs, abs(last(p) - last2(p)))
    errRel <- c(errRel, last(errAbs)/last2(p))
    
    if (last(errAbs) < errmax) {
      output <- package(aa,bb,p,fp,errAbs,errRel)
      return(output)
    }
    
    N <- N + 1
  }
  
  print("Nmax limit reached")
  output <- package(aa,bb,p,fp,errAbs,errRel)
  return(output)
}






############
#To get the code running, run functions here
f <- function(x) { return ( x^3 - x - 1 ) }

output <- BisectionMethod(f,1,2,14,10^(-4))
print(output)
