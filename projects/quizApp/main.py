quizes=[
    {  
        "question":"who is the cs teacher?",
        "answer":"abhinav sir",
        "options":["abhinav sir","raj sir","raghav sir","arun sir"]
    },
    {
        "question":"who is the bio teacher?",
        "answer":"raj sir",
        "options":["abhinav sir","raj sir","raghav sir","arun sir"]
    },
    {
        "question":"who is the maths teacher?",
        "answer":"raghav sir",
        "option":["abhinav sir","raj sir","raghav sir","arun sir"]
    },
    {
        "question":"who is the physics teacher?",
        "answer":"arun sir",
        "option":["abhinav sir","raj sir","raghav sir","arun sir"]
    },
    
    
]


points = 0
failedStreak = 0


for i in quizes:
    if(failedStreak != 2):
        print(f"Q. {i["question"].upper()}")
        for j in i["options"]:
            print(j)
        x = input('Enter answer: ')
        if(x == i["answer"]):
            points+=10
            print("Answer is correct\n", points)
            failedStreak=0
        else:
            print("Answer is incorrect")
            failedStreak+=1
    else:
        print("You failed")
        break