def Problema1(j):
    import math
    def is_prime(n):
        if n % 2 == 0 and n != 2:
            return False
        for x in range(3, math.floor(math.sqrt(n)) + 1, 2):
            if n % x == 0:
                return False
        return True

    def enesimo_primo(n):
        if n == 1:
            return 2
        cont = 1
        for x in range(3, 1000000000000000000000000000000000000000, 2):
            if is_prime(x):
                cont += 1
            if cont == n:
                break
        return x

    def dif_qntd_primos(n1,n2):
        if n1 % 2 != 0:
            n1 += 1
        contagem = 0
        for i in range(n1+1, n2+1, 2):
            if is_prime(i):
                contagem += 1
        return contagem

    cont = 0
    for i in range(2, 101):
        p1 = enesimo_primo(i)**2
        p2 = enesimo_primo(i+1)**2
        if dif_qntd_primos(p1, p2) <= j:
            print(f'Problema 1: resultado = {i},{i+1}')
            cont += 1
    if cont == 0:
        print(f"Problema 1: resultado = nao existe")

def Problema2(j):
    def generate_pascals_triangle(num_rows):
        triangle = []
        for row_num in range(num_rows):
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]
            triangle.append(row)
        return triangle


    triangle = generate_pascals_triangle(j)
    cont = 0
    for i in range(j):
        for x in triangle[i]:
            if x % 2 != 0:
                cont += 1
    print(f'Problema 2: resultado = {cont}')

def Problema3(j):
#------------------------------------#
    sequence = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457, 32582657, 37156667, 42643801, 43112609, 57885161]
    soma = 0
    for i in range(0, j):
        soma += sequence[i]

    print(f'Problema 3: resultado = {soma}')

def Problema3_metodo(j):
        import math
        def is_prime(n):
            if n % 2 == 0 and n != 2:
                return False
            for x in range(3, math.floor(math.sqrt(n)) + 1, 2):
                if n % x == 0:
                    return False
            return True
        def lucas_lehmer(p):
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
        p = 3
        l = [2]
        while len(l) < j:
            if is_prime(p) and lucas_lehmer(p):
                l.append(p)
            p += 2
        print(f'Problema 3: resultado = {sum(l)} - *verificação mais rapida')


def main():
    Problema1(4)#quanto a diferença entre c(pn+1^2) - c(pn^2) < n, aqui é 4(pedido no enuciado)
    Problema2(1000)#Valor de i nesse caso é de 1 até 1000(pedido no enuciado)
    Problema3(30)#O numero dos primeiros x valores para serem somados, nesse caso 30(mesmo do enuciado)
    Problema3_metodo(10)#O numero dos primeiros x valores para serem somados, nesse caso 10(mesmo do exemplo)
    #procurei informação em todo lugar, e nao existe forma mais rapida de verificar
    #até porque o maior numero de marsenne descoberto é 51°, entao é um programa pesado

if __name__ == '__main__':
    main()
print("Joao Pedro Correa Silva, 11202321629")