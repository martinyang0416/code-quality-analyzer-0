def Fact(n):
  res = 1 
  while n > 0 :
    res *= n
    n -= 1
  return res

def C(n,k):
  return (Fact(n) // ( Fact(k) * Fact(n-k) ) )
  
n = int ( input() ) - 1 

print ( C(n+5,n)*C(n+3,3) )



