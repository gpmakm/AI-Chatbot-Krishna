def greet():
    user = "User "
    askNews = "Kaisa h tu?"
    askSadIf = "Yaara kya hua?"
    askProblem = "Yaara jo problem h openly bolne ka, or ha number diya h wo enter kr-"
    name = input("Radhe Radhe yaara, Ek kaam kro apna naam btao taaki kaam ho paye aage-")
    gender = input("Ha gender v bta dena taaki achhe se baat kr skoo mai-")
    if gender == "male":
        user = user.replace("User", "Bhai")
        askProblem = askProblem.replace("Yaara", "Bhai")


    elif gender == "female":
        askSadIf = askSadIf.replace("User", name)
        askProblem = askProblem.replace("Yaara", name)
        askNews = askNews.replace("Kaisa", "Kaisi")

    else:
        user = user.replace("Yaara", name)
        askProblem = askProblem.replace("Yaara", name)
        askNews = askNews.replace("Kaisa", "Kaise")

    #
    haal = input(name + " " + askNews + "\n\t 1.Sad \t2.Happy \t3.Can't decide ---")
    if haal == "1" or haal == "Sad":
        print(askSadIf)
        problemFile = open("problemsList.txt", "r")
        print(problemFile.read())
        prob = int(input(askProblem))


greet()
