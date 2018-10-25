class Itra:


    def itr(self,x):
        self.a=x;
        self.c=0

        return self
    def nex(self,x):
        if self.c < len(self.a):
            x=self.a[self.c]
            self.c+=1
            return x
        else:
            StopIteration


as1 =[313,131,31,3,13,1,31,3,13,]
aas=["wdf","asd","ada","adaw"]
aas[2]="AS"

aa=Itra()
it=aa.itr(aas)
print(aa.nex(it))
print(aa.nex(it))
print(aa.nex(it))
print(aa.nex(it))
print(aa.nex(it))
print(aa.nex(it))










