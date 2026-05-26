import json
with open("jokes.txt","r") as f:
    joke=f.readlines(4)
jokes=[]
for m in range(151):
    jokes.append