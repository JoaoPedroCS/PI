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
        for x in range(3, 50000000, 2):
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


    p1 = enesimo_primo(j)**2
    p2 = enesimo_primo(j+1)**2

    print(f'Problema 1: resultado = {dif_qntd_primos(p1,p2)}')

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
    for i in range(15):
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
    Problema1(100)
    Problema2(1000)
    Problema3(10)
    Problema3_metodo(10)
    
    
if __name__ == '__main__':
    main()
