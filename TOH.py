def tohMove(n,src,temp,des):
    if n==1:
        print(str(n)+" disk move "+src+" to "+des)
        return
    tohMove(n-1,src,des,temp)
    print(str(n)+" disk move "+src+" to "+des)
    tohMove(n-1,temp,src,des)

tohMove(4,"A","B","C")