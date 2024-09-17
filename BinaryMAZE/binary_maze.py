b=int("1100101011110010",2)
ab=b & int("1010110010101101",2)
ob=ab | int("0111001100110011",2)
xb=ob ^ int("1101110111001110",2) 
nb=~xb & 0xFFFF
print("Final binary after logical gates:", bin(nb)[2:])


