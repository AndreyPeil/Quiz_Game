def Question():
    questions = ("How many planets are there in the solar system?",
                 "How many bones are there in a human body?",
                 "How many states does the USA have?",
                 "What is the capital of Brazil?")
    return questions

def Option():
    options = (("A. 1", "B. 8", "C. 12"),
               ("A. 206", "B. 207", "C. 208"),
               ("A. 50", "B. 26", "C. 48"),
               ("A. São Paulo", "B. Rio de Janeiro", "C. Brasília"))
    return options

def Answer():
    correct = ("B", "A", "A", "C")
    return correct

def guess(questions, options, correct):
    guesses = []
    score = 0
    question_num = 0

    for question in questions:
        print("")
        print(question)
        for option in options[question_num]:
            print(option)

        guess = input("Enter your guess (A, B, C): ").upper()
        assert guess in ['A', 'B', 'C'], "Invalid input. Please enter 'A', 'B', or 'C'."
        guesses.append(guess)
        if guess == correct[question_num]:
            print("Correct!")
            score += 1
        else:
            print("Incorrect.")
            print(f"The correct option was: {correct[question_num]}")

        question_num += 1

    print("Quiz completed!")
    print(f"Your score: {score}/{len(questions)}")

def main():
    questions = Question()
    options = Option()
    correct = Answer()
    guess(questions, options, correct)

main()
