#1010 - Simple Calculate
a, b, c= list(map(float,input().split()))
d, f, g= list(map(float,input().split()))

print(f"VALOR A PAGAR: R$ {b*c+f*g:.2f}")