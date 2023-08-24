def Bbit_print(i):
    output =""
    for j in range(7,-1,-1):
        output += "1" if i & (1<<j) else "0"
    print(output)

for i in range(-5,6):
    print("%3d = " %i, end = '')
    Bbit_print(i)
"""
 -5 = 11111011
 -4 = 11111100
 -3 = 11111101
 -2 = 11111110
 -1 = 11111111
  0 = 00000000
  1 = 00000001
  2 = 00000010
  3 = 00000011
  4 = 00000100
  5 = 00000101
  """