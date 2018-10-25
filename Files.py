

# with open("Do.jpg","rb") as fr:
#     with open("Do_c.jpg","wb") as fw:
#         size=100
#         fs = fr.read()
#         while len(fs)>0:
#             fw.write(fs)
#             fs=fr.read(size)
class Dog:
    def __init__(this,type,clr):
        this.type=type
        this.clr=clr

d1=Dog("bulldog","black")

with open("Testt.txt",'w') as fw:
    fw.write(d1.type+"\n")
    fw.write(d1.clr)
with open("Testt.txt","r") as fr:
    type=fr.readline()
    clr=fr.readline()


d2=Dog("bulldog","black")

print(d2.type)

print(d2.clr)

print(d1.type)

print(d1.clr)
print(d1 is d2)

a=[1,2,3]
b=[1,2,3]
print(a==b)


