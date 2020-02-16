import time

sc1 = ["Hi! How are you? 1: I'm fine. 2: Thanks. How are you?\n", "Where do you live? 1: I am from city A. 2: I come from city A, and I am here for the event at B. Have you heard about that?\n",
                "Do you go to school around here? 1: Yes! I go to school A studying B. How about you? 2: Yeah, I like the school A.\n"]
score1 = [[10, 5], [10, 5], [5, 10]]
sc2 = ["Hi! How has your work been? 1: It's fine I guess. 2: Not so well. I'm looking for advice.\n", "Have you finish the last project? 1: No, struggling. What about you? 2: It's going.\n"]
score2 = [[10, 5], [5, 10]]
sc3 = ["Where did you get your new pens? 1: Amazon. 2: I got them from ebay for only a dollar yeach!\n",
                "How did you do on the quiz? 1: I don't care about it at this point lol. 2: I could definitely study harder. Wanna study together next time?\n",
                "Have you heard about Eric? 1: No. 2: What happened?\n", "What's for lunch? 1: Can't you check yourself? 2: I don't know! I'm starving!\n"]
score3 = [[10, 5], [10, 2], [10, 5], [10, 5]]
sc4 = ["Hi! I like you! 1: Thank you! You are super attractive too! 2: Thanks! Me too!"]
score4 = [[7, 1000000]]

SC = [sc1, sc2, sc3, sc4]
scores = [score1, score2, score3, score4]


print("Welcome to CONVO!!\n")
time.sleep(1)
name = input("Please enter your name:\n")
print("Hello!", name, "!")
email = input("Please enter your email:\n")
age = input("How old are you?\n")
password = input("Password?\n")

learn = True
def runtext():
    time.sleep(1)
    response = input("Please select a scenario: 1: General, 2: School, 3: Work, 4: Date\n")
    if response == "1":
        print("Loading General Scenario")
        scenario = SC[0]
        score = scores[0]
    elif response == "2":
        print("Loading School Scenario")
        scenario = SC[2]
        score = scores[2]
    elif response == "3":
        print("Loading Work Scenario")
        scenario = SC[1]
        score = scores[1]
    else:
        print("Loading Date Scenatio")
        scenario = SC[3]
        score = scores[3]

    time.sleep(1)
    print("Response the following questions by inputing the numerical choice\n")
    total = 0
    time.sleep(1)
    i = 0
    while i < len(scenario):
        response = input(scenario[i])
        if response == "1":
            total += score[i][0]
        else:
            total += score[i][1]
        i += 1
        time.sleep(1)
        print("Total:", total)
    #time.sleep(1)
    print("Loading Results...")
    #time.sleep(1)
    print(".")
    #time.sleep(1)
    print(".")
    #time.sleep(1)
    print(".")
    time.sleep(1)
    if total <= 10:
        print("You are pretty good at communicating with others! Other people feel natural talking to you!")
        print("Score:", total)
    elif total < 25:
        print("Sometimes you slide awkward phrases out, but don't worry too much about them! Try clicking back an see why you receive this score!")
        print("Score:", total)
    else:
        print("Sometimes people think you don't talk as naturally. Keep it up! Click back and see what are some of our recommendations in these scenarios!")
        print("Score:", total)
while learn:
    runtext()
    response = input("Practice More? Type 1. To exit, press ENTER.")
    learn = response == "1"
