dis={'name':"john","age":23,"course":["math","science"]}

print(dis.fromkeys("age"))

for val in dis.popitem():
    if val is "course":
     print(val)
    else:
        for x in val:
            print(x)

for x ,y in dis.items():
    print(x +", "+str(y))


print(dis)