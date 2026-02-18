import pandas as pd

# Load extracted questions
train_df = pd.read_csv("train_questions.csv")  # we will create this CSV next

# Function to assign intent
def assign_intent(q):
    q = q.lower()
    if "example" in q:
        return "Example"
    elif "explain" in q or "what" in q or "how" in q:
        return "Explanation"
    else:
        return "Doubt clarification"

# Function to assign topic
def assign_topic(q):
    q_lower = q.lower()

    # Backpropagation
    if "backprop" in q_lower:
        return "Backpropagation"

    # Neural Networks
    elif "neural network" in q_lower or "neural networks" in q_lower:
        return "Neural Networks"

    # CNN
    elif "cnn" in q_lower or "convolutional" in q_lower:
        return "CNN"

    # RNN
    elif "rnn" in q_lower or "recurrent" in q_lower:
        return "RNN"

    # Optimization / Gradient
    elif "gradient" in q_lower or "optimization" in q_lower or "descent" in q_lower:
        return "Optimization"

    # Loss Function
    elif "loss" in q_lower:
        return "Loss Function"

    # Activation
    elif "activation" in q_lower:
        return "Activation Function"

    else:
        return "General"



# Function to assign difficulty
def assign_difficulty(q):
    q = q.lower()
    if "not sure" in q or "confused" in q:
        return "Beginner"
    if "why" in q or "how" in q:
        return "Intermediate"
    return "Advanced"

# Create labels
train_df["intent"] = train_df["query"].apply(assign_intent)
train_df["topic"] = train_df["query"].apply(assign_topic)
train_df["difficulty"] = train_df["query"].apply(assign_difficulty)

# Save labeled CSV
train_df.to_csv("train_labeled.csv", index=False)

print("Labeled CSV created: train_labeled.csv")
