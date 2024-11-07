
question_data = [
    {
        "category": data["results"]["category"],
        "type": data["results"]["type"],
        "difficulty": data["results"]["difficulty"],
        "question": data["results"]["question"],
        "correct_answer": data["results"]["correct_answer"],
        "incorrect_answers": [
            data["results"]["incorrect_answer"]
        ]
    }]

print(question_data)