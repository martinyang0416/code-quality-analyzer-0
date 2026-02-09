def calculate(n):
  if (n < 5) or (n%2 == 0):
    return 'NO'
  else:
    y = int((n-3)/2)
    return "1 "+str(y)

print (calculate(int(input())))
				 	 		   				 	 	  	  		 		