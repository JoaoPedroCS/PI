a, b = map(int, input().split())
item = {1:4.00, 2:4.50, 3:5.00, 4:2.00, 5:1.50}
v = item[a] * b
print(f"Total: R$ {v:.2f}")