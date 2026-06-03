import json as js
import random as rnd

def tellJoke():
    with open("jokes.json","r",encoding="utf-8") as jfile:
        jokes=js.load(jfile)
        ind_joke=rnd.randint(0,len(jokes)-1)
        joke=jokes[ind_joke]
        print(joke["joke"])
tellJoke()