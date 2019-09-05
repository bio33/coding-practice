import time
def memoization(fib):
  cache = {}          # create cache ,datatype -> hashmap  
  def helper(n):
    if n not in cache:      
      cache[n] = fib(n)   
    return cache[n]
  return helper

def fib_memo(n):
  if n < 2 :
    return n
  return fib_memo(n-2) + fib_memo (n - 1)

def fib(n):
  if n < 2 :
    return n
  return fib(n-2) + fib (n - 1)


n = 30        # increase value of n to see the difference


start = time.time()
print("With Memoization")
fib_memo = memoization(fib_memo)
print(fib_memo(n))
print(time.time()-start)
print("*"*20)
start = time.time()
print("Without memoization`")
print(fib(n))
print(time.time()-start)



