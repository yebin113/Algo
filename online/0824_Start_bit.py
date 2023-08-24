def Bbit_print(i):
    output = ''
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output, end=' ')


a = 0x10  # 16
x = 0x01020304
print("%d = " % a, end='')
Bbit_print(a)
print()
"""
16 = 00010000
"""
output = ''
for j in range(31, -1, -1):
    output += "1" if x & (1 << j) else "0"
print(output)
"""
00000001000000100000001100000100 
"""
print("0%X = " % x, end='')
for i in range(0, 4):
    Bbit_print((x >> i * 8) & 0xff)
"""
01020304 = 00000100 00000011 00000010 00000001 -> 역순으로 찍어보기
"""
