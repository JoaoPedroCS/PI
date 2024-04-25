import time

def inverse(x):
  return x[::-1]
n = input()
start_time = time.time()
di = "1"
df = "1"
count = 0
for i in range(int(n)):
    df = df + "0"
for i in range(int(n)-1):
    di = di + "0"

for i in range(int(di), int(df)):
   teste = int(inverse(str(i)))
   if teste > i:
      count += 1

print(count)
print(f"--- {(time.time() - start_time):.5f} seconds ---")

###########################################################################################
MAXSIZE = 19
revertivel = [0] * MAXSIZE

def bemRevertivel():
    revertivel[1] = 0
    revertivel[2] = 36
    for i in range(3, 19):
        
        if i & 1:
            revertivel[i] = revertivel[i - 1] * 10
        else:
            revertivel[i] = revertivel[i - 2] * 100 + 45 * qtsPalindromo(i - 2)


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