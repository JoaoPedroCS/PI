x = int(input())

for i in range(0, x, 1):
    x = int(input())
    if x%2!=0 and x<0:
        print("ODD NEGATIVE")
    elif x%2!=0 and x>0:
        print("ODD POSITIVE")
    elif x%2==0 and x<0:
        print("EVEN NEGATIVE")
    elif x%2==0 and x>0:
        print("EVEN POSITIVE")
    else:
        print("NULL")