print("==== Quiz Score Saver ====")

name = input("Enter your name: ")

score = 0

questions = [
    ("What is the capital of India? ", "delhi"),
    ("Which language are we learning? ", "python"),
    ("How many days are there in a week? ", "7")
]

for question, answer in questions:
    user_answer = input(question).lower().strip()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\n===== RESULT =====")

print("Name:", name)
print("Score:", score, "/", len(questions))