#1051 - Taxes
x = float(input())

if x >= 0 and x <= 2000:
    print("Isento")
    
elif 2000 < x <= 3000:
    print(f"R$ {(x-2000)*0.08:.2f}")

elif 3000 < x <= 4500:
    print(f"R$ {1000*0.08 + (x-3000) * 0.18:.2f}")

elif x > 4500:
    print(f"R$ {1000*0.08 + 1500 * 0.18 + (x-4500) * 0.28:.2f}")