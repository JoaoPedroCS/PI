a, b, c, d = map(float, input().split())
m = (a*2 + b*3 + c*4 + d*1)/10
print(f"Media: {m:.1f}")

if m < 5:
    print("Aluno reprovado.")
elif m >= 7:
    print("Aluno aprovado.")
elif 5 <= m < 7:
    print("Aluno em exame.")
    rec = float(input())
    print(f"Nota do exame: {rec:.1f}")
    mf = (rec+m)/2
    if mf >= 5:
        print("Aluno aprovado.")
    elif mf < 5:
        print("Aluno reprovado.")
    print(f"Media final: {mf:.1f}")