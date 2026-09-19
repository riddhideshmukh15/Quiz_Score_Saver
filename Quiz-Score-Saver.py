print("===== QUIZ SCORE SAVER =====")

name = input("Enter your name: ")

score = 0

questions = [
    ("What is the capital of India?", ["A. Mumbai", "B. Delhi", "C. Pune", "D. Chennai"], "b"),
    ("Which language are we learning?", ["A. Java", "B. C++", "C. Python", "D. HTML"], "c"),
    ("How many days are there in a week?", ["A. 5", "B. 6", "C. 7", "D. 8"], "c"),
    ("Which symbol is used for comments in Python?", ["A. //", "B. #", "C. /*", "D. $"], "b"),
    ("Which function is used to display output in Python?", ["A. print()", "B. show()", "C. display()", "D. output()"], "a")
]

for i, (question, options, answer) in enumerate(questions, 1):
    print(f"\nQuestion {i}: {question}")

    for option in options:
        print(option)

    user_answer = input("Enter your answer (A/B/C/D): ").lower().strip()

    if user_answer == answer:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

total_questions = len(questions)
percentage = (score / total_questions) * 100

print("\n===== QUIZ RESULT =====")
print("Name:", name)
print("Score:", score, "/", total_questions)
print("Percentage:", percentage, "%")

if percentage == 100:
    print("Excellent! Perfect score!")
elif percentage >= 60:
    print("Good job! Keep practicing!")
else:
    print("Keep learning and try again!")

print("Thanks For Using Quiz-Score-Saver!")