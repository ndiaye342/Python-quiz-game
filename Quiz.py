# quiz_app.py

def run_quiz():
    quiz = [
        {
            "question": "What is the capital of France?",
            "options": ["A. Berlin", "B. London", "C. Paris", "D. Madrid"],
            "answer": "C"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
            "answer": "B"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"],
            "answer": "D"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'?",
            "options": ["A. Charles Dickens", "B. William Shakespeare", "C. J.K. Rowling", "D. Mark Twain"],
            "answer": "B"
        },
        {
            "question": "Which gas do plants absorb from the atmosphere?",
            "options": ["A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Hydrogen"],
            "answer": "C"
        },
    ]

    score = 0

    print("Welcome to the Quiz!\n")

    for i, q in enumerate(quiz, 1):
        print(f"Q{i}: {q['question']}")
        for option in q['options']:
            print(option)
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()

        if user_answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was {q['answer']}.\n")

    print(f"Quiz completed! Your final score is {score} out of {len(quiz)}.")

if __name__ == "__main__":
    run_quiz()
