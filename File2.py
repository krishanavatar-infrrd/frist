import os
"""fname.strip()[1:].zfill(2)      strip remove white space and zfill fill 0 in front of nuber"""
os.chdir("AA")
print(os.getcwd())
count=1
for f in os.listdir():
    fname,fext=os.path.splitext(f)
    f1="test {}{}".format(str(count),fext)
    print(f1)
    count+=1
    os.rename(f,f1)




