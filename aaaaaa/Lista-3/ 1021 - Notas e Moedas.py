a = float(input())
b = a*100
print(f"NOTAS:\n{a//100:.0f} nota(s) de R$ 100.00\n{(a%100)//50:.0f} nota(s) de R$ 50.00\n{a%50//20:.0f} nota(s) de R$ 20.00\n{a%50%20//10:.0f} nota(s) de R$ 10.00\n{a%10//5:.0f} nota(s) de R$ 5.00\n{a%5//2:.0f} nota(s) de R$ 2.00")
print(f"MOEDAS:\n{b%500%200//100:.0f} moeda(s) de R$ 1.00\n{b%100//50:.0f} moeda(s) de R$ 0.50\n{b%50//25:.0f} moeda(s) de R$ 0.25\n{b%25//10:.0f} moeda(s) de R$ 0.10\n{b%25%10//5:.0f} moeda(s) de R$ 0.05\n{b%5//1:.0f} moeda(s) de R$ 0.01")