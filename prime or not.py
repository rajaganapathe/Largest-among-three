num=int(input("enter the number:"))
if num>1: #prime number are greater than 1
 for i in range(2,num):
  if num%i==0:
   print("not a prime")
   break #if no break its keep on running
  else:
   print("prime")
