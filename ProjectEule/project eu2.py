def projeu2():
  a=0
  b=1
  x=0
  while b<4000001:
    a=b
    b=a+b
    if (b%2==0):
      x+=b
  print(x)

projeu2()
      
