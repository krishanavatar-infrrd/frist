a=[1,2,3,4,5,6,7]

while True:
    try:
     for y in a:
        if y == 5:
            print(y)
            raise BaseException
        else:
            continue
    except:
        break
