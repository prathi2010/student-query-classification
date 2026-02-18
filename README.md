Student Query Classification System
 Overview
The Student Query Classification System is a Python-based NLP project that classifies student questions into three categories:
Intent (Explanation, Doubt Clarification, etc.)
Topic (Neural Networks, Optimization, Backpropagation, etc.)
Difficulty Level (Beginner, Intermediate, Advanced)
The system analyzes user input using rule-based keyword detection and produces structured JSON output.
 Features
Real-time question input
Automatic intent detection
Topic classification using keyword rules
Difficulty level identification
Structured JSON output format
Continuous question handling until user exits
 Project Structure
student-query-classification/
│
├── main.py
├── requirements.txt
└── README.md
 Setup Instructions
Prerequisites
Python 3.8 or higher installed
Basic knowledge of running Python scripts
Check Python version:
python --version
Install Dependencies
If using external libraries:
pip install -r requirements.txt
If no external libraries are used, this step can be skipped.
Run the Application
python main.py
 Example Usage
Input:
Enter student question: What is gradient descent?

Output:
{
  "intent": "Explanation",
  "topic": "Optimization",
  "difficulty_level": "Advanced"
}


