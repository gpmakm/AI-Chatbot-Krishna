def joke():
    j=[]
    f=open("jokes.txt","r")
    for i in range(4):
        d=f.readline()
        j.append(d)
    return j


jokes=[]
for m in range(151):
    jokes.append(joke[m])