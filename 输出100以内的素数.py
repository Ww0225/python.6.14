for n in range(1,101):
    if n%2==0:
        continue
    for i in range(2,int(n**0.5)):
        if n%i==0:
            break
    else:
        print(n,end=' ')