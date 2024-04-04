MAXSIZE = 19
revertivel = [0] * MAXSIZE
print(revertivel)
def bemRevertivel():
    revertivel[1] = 0
    revertivel[2] = 36
    for i in range(3, 19):
        
        if i & 1:
            revertivel[i] = revertivel[i - 1] * 10
        else:
            revertivel[i] = revertivel[i - 2] * 100 + 45 * qtsPalindromo(i - 2)
        print(revertivel)
        print(i & 1)

def qtsPalindromo(x):
    x //= 2
    retorno = 9

    for i in range(1, x):
        retorno *= 10

    return retorno

if __name__ == "__main__":
    bemRevertivel()
    numero = int(input())
    print(revertivel[numero])