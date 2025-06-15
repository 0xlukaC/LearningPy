#!/usr/bin/python3

questions = [
    {
        "text": "People who dislike chocolate are…",
        "options": {
            "a": ("Clearly wrong", 10),
            "b": ("Entitled to their opinion", 3),
            "c": ("Probably lactose intolerant", 0),
        },
    },
    # add 2 more questions
]


def question(q):
    print(q["text"])
    for i, (opt, _) in q["options"].items():
        print(f"{i} {opt}")
    choice = input("your choice: ").lower()
    return q["options"].get(choice, (None, 0))[1]


def runquiz():
    results = [question(i) for i in questions]
    score = sum(results)
    print(f"\nFinal score: {score}")
    if score >= 25:
        print("You're a great fit!")
    else:
        print("Maybe not the right flavor for us.")


runquiz()
