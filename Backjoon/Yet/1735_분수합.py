import math
a_top, a_bottom = map(int,input().split())
b_top, b_bottom = map(int,input().split())
c_top =  a_bottom * b_bottom
c_bottom = a_top * b_bottom + b_top * a_bottom
c_gcd = math.gcd(c_top, c_bottom)
print(c_bottom//c_gcd,c_top//c_gcd)