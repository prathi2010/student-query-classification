import pickle
from sentence_transformers import SentenceTransformer
import json

# Load models
intent_clf = pickle.load(open("intent_model.pkl", "rb"))
difficulty_clf = pickle.load(open("difficulty_model.pkl", "rb"))

# Load embedder
embedder = SentenceTransformer("all-MiniLM-L6-v2")

# Topic detection (keyword-based)
def assign_topic(q):
    q_lower = q.lower()
    if "backpropagation" in q_lower:
        return "Backpropagation"
    elif "cnn" in q_lower:
        return "CNN"
    elif "rnn" in q_lower:
        return "RNN"
    elif "gradient" in q_lower:
        return "Optimization"
    elif "neural network" in q_lower:
        return "Neural Networks"
    else:
        return "General"

print("AI Teaching Assistant Started ✅")
print("Type 'exit' to stop.\n")

while True:
    query = input("Enter student question: ")

    if query.lower() == "exit":
        print("Goodbye 👋")
        break

    # Encode query
    query_emb = embedder.encode([query])

    # Predict using ML models
    intent = intent_clf.predict(query_emb)[0]
    difficulty = difficulty_clf.predict(query_emb)[0]

    # Topic using keyword rules
    topic = assign_topic(query)

    # Output
    output = {
        "intent": intent,
        "topic": topic,
        "difficulty_level": difficulty
    }

    print(json.dumps(output, indent=4))
    print("\n---------------------------------\n")
