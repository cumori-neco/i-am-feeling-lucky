import json
import os
import random

def load_questions():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    json_path = os.path.join(base_dir, "questions.json")

    try:
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"have a bad day: {e}")
        return []

def question() -> bool:
    data = load_questions()
    if not data:
        print("No questions found...")
        return True

    item = random.choice(data)
    q_text = item["q"]
    correct_answer = item["a"]

    user_input = input(q_text + " : ").lower()

    if correct_answer.lower() in user_input:
        print("Correct!")
        return True
    else:
        print(f"Wrong!!! The correct answer is '{correct_answer}'")
        return False
