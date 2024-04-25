#1018 - Banknotes
v = int(input())
print(v)
print(f"{v//100} nota(s) de R$ 100,00")
n50 = (v % 100) // 50
print(f"{n50} nota(s) de R$ 50,00")
n20 = (v % 50) // 20
print(f"{n20} nota(s) de R$ 20,00")
n10 = ((v % 50) % 20) // 10
print(f"{n10} nota(s) de R$ 10,00")
n5 = (v % 10) // 5
print(f"{n5} nota(s) de R$ 5,00")
n2 = (v % 5) // 2
print(f"{n2} nota(s) de R$ 2,00")
n1 = ((v % 5) % 2) // 1
print(f"{n1} nota(s) de R$ 1,00")