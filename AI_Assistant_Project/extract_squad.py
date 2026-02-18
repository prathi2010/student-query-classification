import json
import pandas as pd

def extract_questions(json_file):
    with open(json_file, "r", encoding="utf-8") as f:
        data = json.load(f)
    questions = []
    for article in data["data"]:
        for paragraph in article["paragraphs"]:
            for qa in paragraph["qas"]:
                questions.append(qa["question"])
    return questions

if __name__ == "__main__":
    # Extract questions
    train_questions = extract_questions("train-v2.0.json")
    print("Total questions in train dataset:", len(train_questions))
    
    # ✅ Save questions to CSV
    df = pd.DataFrame(train_questions, columns=["query"])
    df.to_csv("train_questions.csv", index=False)
    print("train_questions.csv created successfully!")
