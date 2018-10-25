class B:
    def A(self,x=None,y=None):
        if x==None and y==None:
            return  10
        elif x!=None and y==None:
            return x
        elif x==None and y!=None:
            return y
        elif x!=None and y!=None:
            return  x,y


a=B()
print(a.A(None,123))
