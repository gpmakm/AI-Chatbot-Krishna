import json as js

def tellJoke():
    with open("jokes.json","r",encoding="utf-8") as jfile:
        jokes=js.load(jfile)
        