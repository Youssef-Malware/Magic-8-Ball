while True:

    import random

    answers = [
    "Yes",
    "No",
    "Maybe",
    "Ask again later",
    "shut up"
]

    question = input("Ask a question: ")
    print(random.choice(answers))