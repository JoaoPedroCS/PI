import time 
start_time = time.time()
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
        print(f'Problema 3: resultado = {sum(l)} - calculo bruto')

Problema3_metodo(20)
print(f"--- {(time.time() - start_time):.5f} seconds ---")