import json

def load_questions(quiz_data):
    with open(quiz_data, 'r') as file:
        questions = json.load(file)
    return questions

def display_question(question, choices):
    print(question)
    for i, option in enumerate(choices, start=1):
        print(f"{i}. {option}")
    user_answer = input("Your choice (1-4): ")
    return user_answer

def main():
    filename = 'quiz_data.json'
    questions = load_questions(filename)

    score = 0
    total_questions = len(questions)

    for q in questions:
        user_answer = display_question(q['question'], q['choices'])
        # print(q['choices'][int(q['correct_ans'])-1])
        # print((int(q['correct_ans'])))
        # if q['choices'][int(user_answer)-1] == q['choices'][int(q['correct_ans'])-1]:
        # or
        # print(int(user_answer))
        # print(int(q['correct_ans']))
        if (int(user_answer)) ==int(q['correct_ans']):
            score += 1
       
    print(f"Your score: {score}/{total_questions}")

if __name__ == "__main__":
    main()