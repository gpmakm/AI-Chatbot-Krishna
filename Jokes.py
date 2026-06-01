import json as js
import random as rnd

def tellJoke():
    with open("jokes.json","r",encoding="utf-8") as jfile:
        jokes=js.load(jfile)
        joke=jokes["joke"]
        joke=rnd.choice(joke)
        print(joke["joke"])
tellJoke()