a=int(input("enter the salary"))
if(a>=10000):
  b=a*0.1
  c=a+b
  print("the salary is",c)
elif(a>=20000):
  b=a*0.2
  c=a+b
  print("the salary is",c)
elif(a>=50000 and a<60000):
  b=a*0.3
  c=a+b
  print("the salary is",c)
  else:
    print("the salary is",a)  
