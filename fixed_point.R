#This will be our fixed point iteration code with R
source("useful_functions.R")
options(digits = 15)

package <- function(output, err_abs, err_rel) {
  n <- c(0:(length(output)-1))
  i <- data.frame(
    n <- n,
    output <- output,
    err_abs <- err_abs,
    err_rel <- err_rel
  )
  
  return(i)
}

fixed_point <- function(func, start, err_max, nmax, overflow_max = 1000) {
  
  #a vector to fill up our iterations
  output <- start
  err_abs <- 0
  err_rel <- 0
  
  #loop counter
  n <- 1
  
  #Now we perform the iteration
  while(n < nmax) {
    
    output <- c(output, func(last(output)))
    
    #error checking
    err_abs <- c(err_abs, abs(last(output) - last(output,2)))
    err_rel <- c(err_rel, last(err_abs)/last(output,2))
    
    if(last(err_abs) < err_max || last(err_abs) > overflow_max) {
      pack <- package(output, err_abs, err_rel)
      return(pack)
    } 

    n <- n + 1
  }
  
  cat("Method failed to converge before nmax")
  pack <- package(output, err_abs, err_rel)
  return(pack)
  
}



#To get the code running
func <- function(x) {
  return( (10/(4+x))^(1/2) )
}

start = 1.5
err_max = 10^(-8)
nmax = 35

f = fixed_point(func,start,err_max,nmax)
print(f)
