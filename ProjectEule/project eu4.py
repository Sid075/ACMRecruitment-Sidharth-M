
def projecteul4():
  x=0
  for i in range(100, 1000):
      for j in range(100, 1000):
          p=i*j
          d=str(p)
          if str(d) == str(d[::-1]):
              l.append(p)
  print(max(l))
l=[]
projecteul4()
