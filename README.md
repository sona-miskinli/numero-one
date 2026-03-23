import random
from datetime import date, timedelta
# Chemistry Quiz with Ollama 3

# Define the topics and their corresponding chemical reactions
topics = {
    'Acids and Bases': ['HCl + NaOH → NaCl + H2O', 'HNO3 + KOH → KNO3 + H2O'],
    'Chemical Bonding': ['H2 + O2 → 2H2O', 'C6H12O6 + O2 → CO2 + H2O'],
    'Organic Chemistry': ['CH4 + O2 → CO2 + H2O', 'C5H10O + O2 → CO2 + H2O']
}
A simple interactive chemistry quiz that uses a local Ollama 3 model to check user answers.

# Initialize variables to track statistics
correct_reactions = 0
incorrect_reactions = 0
today = date.today()
## Features
- Randomly selects a chemistry topic and reaction.
- Hides products for the user to guess.
- Uses Ollama 3 to verify answers and provide feedback.
- Tracks correct and incorrect answers with simple statistics.

def generate_reaction():
    """Generate a random reaction from the topics"""
    topic = random.choice(list(topics.keys()))
    reactions = topics[topic]
    return f"{reactions[random.randint(0, len(reactions) - 1)]} ({topic})"
## Requirements
- Python 3.10+
- [Ollama Python package](https://docs.ollama.com/python)
- Local Ollama 3 model installed

def test_reaction(user_reaction):
    """Test if the user's reaction is correct or not"""
    global correct_reactions
    global incorrect_reactions
    reaction = generate_reaction()
    if user_reaction.lower() == reaction:
        print(f"Correct! The reaction was: {reaction}")
        correct_reactions += 1
    else:
        print(f"Wrong. The correct reaction is: {reaction}")
        incorrect_reactions += 1

def show_statistics():
    """Show the statistics of the reactions"""
    global correct_reactions
    global incorrect_reactions
    today = date.today()
    if today.weekday() < 5:  # Only update on weekdays
        last_updated = (date.today() - timedelta(days=7)).strftime("%Y-%m-%d")
        print(f"Statistics updated as of {last_updated}:")
        print(f"Correct reactions: {correct_reactions}")
        print(f"Incorrect reactions: {incorrect_reactions}")

def main():
    """Main function to interact with the user"""
    while True:
        show_statistics()
        user_reaction = input("Enter your reaction, or 'q' to quit: ")
        if user_reaction.lower() == 'q':
            break
        test_reaction(user_reaction)

if __name__ == "__main__":
    main()
## Usage
1. Install dependencies:
```bash
pip install ollama
