soma = 0
l = []
for k in range(1, 51):

    l.append(((-1)**(k+1))/(2*k-1))
    soma += ((-1)**(k+1))/(2*k-1)
print(f"4 * {l}")
print(soma*4)