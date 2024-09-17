def projeul5():
  n = 20
  while True:
    if all(n % i == 0 for i in range(1, 21)):
      print(n)
      break
    n+=1


projeul5()
