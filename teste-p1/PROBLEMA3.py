valor_ant = 0
valor_atual = 1
l = [0]
while valor_atual < 4000000:
    guard_lug = valor_atual
    valor_atual = valor_ant + valor_atual
    valor_ant = guard_lug
    
    if valor_atual%2==0:
        l.append(valor_atual)
    print(l)
print(sum(l))