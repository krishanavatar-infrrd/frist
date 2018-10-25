list=("jai","abi","akls","SJS","yoga")


n=7
st=n
sp=int(n/2)
for x in range(0,n):
    for z in range(0,sp):
        print(" ",end="")
    for y in range(0,st):
        print("*", end="")
    print()

    if x<int(n/2):
        sp-=1
        st-=2
    else:
        sp+=1
        st+=2










