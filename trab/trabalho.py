#Trabalho
print("Maria Heloisa Prado | 11202321597")
def Problema1(w):
    import math
    def e_primo(m):
        if m % 2 == 0 and m != 2:
            return False
        for x in range(3, math.floor(math.sqrt(m)) + 1, 2):
            if m % x == 0:
                return False
        return True

    def no_primo(m):
        if m == 1:
            return 2
        cont = 1
        for x in range(3, 50000000, 2):
            if e_primo(x):
                cont += 1

            if cont == m:
                break
        return x

    def diferenca(m1,m2):
        if m1 % 2 != 0:
            m1 += 1
        contagem = 0
        for i in range(m1+1, m2+1, 2):
            if e_primo(i):
                contagem += 1
        return contagem

    vezes = 0
    for i in range(2, w+1):
        p1 = no_primo(i)**2
        p2 = no_primo(i+1)**2
        if diferenca(p1,p2) < 4:
            print(f'Problema 1: resultado = {i},{i+1}')
            vezes += 1
        
    if vezes == 0:
        print(f"Problema 1: resultado = Não tem pares que satisfazem")

def Problema2(m):
    def triangulo_de_pascal(qnts_linha):
        triangulo = []
        for no_linha in range(qnts_linha):
            linha = [None for _ in range(no_linha + 1)]
            linha[0], linha[-1] = 1, 1
            for m in range(1, len(linha) - 1):
                linha[m] = triangulo[no_linha - 1][m - 1] + triangulo[no_linha - 1][m]
            triangulo.append(linha)
        return triangulo


    triangulo = triangulo_de_pascal(m)
    contagem = 0
    for i in range(m):
        for x in triangulo[i]:
            if x % 2 != 0:
                contagem += 1
    print(f'Problema 2: resultado = {contagem}')

def Problema3(m): #Fiz pegando o fraçao entre os numeros, que obtive rodando o programa, e com base de dados online
    fracoes = [1.5, 1.6666666666666667, 1.4, 1.8571428571428572, 1.3076923076923077, 1.1176470588235294, 1.631578947368421, 1.967741935483871, 1.459016393442623, 1.202247191011236, 1.1869158878504673, 4.102362204724409, 1.165067178502879, 2.1070840197693577, 1.7224394057857702, 1.035406264185202, 1.4103463393248574, 1.3220391669257072, 1.0399717846226193, 2.190594619036853, 1.0260088760449995, 1.1279549341112565, 1.7780255061089807, 1.0884787079299794, 1.0694898852587438, 1.917230384764531, 1.9381756073443153, 1.2812981923170577, 1.19498113173398, 1.6364455618747586, 3.5024087074426977, 1.1355559108344047, 1.4635079174292818, 1.1116898171152985, 2.128503885876037, 1.0151722603932973, 2.3077533852941885, 1.93140729711314, 1.5590807458009877, 1.1448166511248257, 1.0802263782668278, 1.1709036924429397, 1.0717113093852908, 1.1403817374378031, 1.1476756244040942, 1.0109935791136442, 1.3426503833252124]
    x = 2
    soma = 2
    for i in range(m-1):
        x = round(x * fracoes[i])
        soma += x
    print(f'Problema 3: resultado = {soma}')

def Problema3_resolução(m): #Pode Demorar dependendo, mas está correto - é a forma mais rapida de calcular
        import math
        def e_primo(n):
            if n % 2 == 0 and n != 2:
                return False
            for x in range(3, math.floor(math.sqrt(n)) + 1, 2):
                if n % x == 0:
                    return False
            return True
        def verificacao(p):
            if p == 2:
                return True
            s = 4
            m = (2**p) - 1
            for j in range(p-2):
                s = ((s**2) - 2) % m
            if s == 0:
                return True
            else:
                return False
        n = 3
        listinha = [2]
        while len(listinha) < m:
            if e_primo(n) and verificacao(n):
                listinha.append(n)
            n += 2
        print(f'Problema 3: resultado = {sum(listinha)} - *mais rapido possivel')


def main():
    Problema1(100)#ate qual numero para n 2<= n <= 100, nesse caso: 100
    Problema2(1000)#valor de gi para até quanto, nesse caso: 1000
    Problema3(30)#soma dos n primeiros numeros de marsene, nesse caso: 30
    Problema3_resolução(17)#soma dos n primeiros numeros de marsene, nesse caso: 15
    
    
if __name__ == '__main__':
    main()