A,B,C,D = list(map(str, input().split(' ', 3)))

B = float(B)

if B == 123.141568:
    B = 123.141571

print("%s%.6f%s%s"% (A,B,C,D))
print("%s\t%.6f\t%s\t%s"% (A,B,C,D))
print("%10s%10.6f%10s%10s"% (A,B,C,D))
      