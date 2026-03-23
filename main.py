import random
from datetime import date, timedelta
from ollama import Ollama  # Make sure you have ollama python package installed

# Initialize Ollama client
client = Ollama()

# Define topics and their corresponding chemical reactions
topics = {
    'Acids and Bases': [
        'HCl + NaOH → NaCl + H2O',
        'HNO3 + KOH → KNO3 + H2O'
    ],
    'Chemical Bonding': [
        'H2 + O2 → 2H2O',
        'C6H12O6 + O2 → CO2 + H2O'
    ],
    'Organic Chemistry': [
        'CH4 + O2 → CO2 + H2O',
        'C5H10O + O2 → CO2 + H2O'
    ]
}

# Initialize statistics
correct_reactions = 0
incorrect_reactions = 0

def generate_question():
    """Pick a random topic and reaction"""
    topic = random.choice(list(topics.keys()))
    reaction = random.choice(topics[topic])
    return topic, reaction

def check_answer_ollama(user_answer, reaction):
    """
    Use Ollama 3 to check if the user's answer matches the correct reaction.
    Returns True/False and a feedback string.
    """
    prompt = f"""
You are a chemistry teacher. I will give you a chemical reaction with reactants hidden:
Reactants: {reaction.split('→')[0].strip()}
User answer: {user_answer}
Correct products: {reaction.split('→')[1].strip()}

Check if the user's answer is correct. Respond only in JSON:
{{ "correct": true/false, "feedback": "Explain briefly." }}
"""
    response = client.chat(model="llama3", messages=[{"role": "user", "content": prompt}])
    # Ollama returns text; parse JSON manually
    import json
    try:
        result = json.loads(response.text)
        return result['correct'], result['feedback']
    except:
        return False, "Couldn't interpret the answer. Try again."

def show_statistics():
    global correct_reactions, incorrect_reactions
    today = date.today()
    last_updated = (today - timedelta(days=7)).strftime("%Y-%m-%d")
    print(f"\nStatistics updated as of {last_updated}:")
    print(f"Correct reactions: {correct_reactions}")
    print(f"Incorrect reactions: {incorrect_reactions}\n")

def main():
    global correct_reactions, incorrect_reactions
    print("Welcome to the LLM-powered Chemistry Quiz!")
    print("Type the products of the reaction, or 'q' to quit.\n")

    while True:
        topic, reaction = generate_question()
        print(f"Topic: {topic}")
        print(f"Reactants: {reaction.split('→')[0].strip()} ?")  # hide products
        user_input = input("Enter the products: ")

        if user_input.lower() == 'q':
            break

        correct, feedback = check_answer_ollama(user_input, reaction)
        if correct:
            print("Correct! ✅\n")
            correct_reactions += 1
        else:
            print(f"Wrong ❌. Feedback: {feedback}\n")
            incorrect_reactions += 1

        show_statistics()

    print("Thanks for playing! Final statistics:")
    show_statistics()

if __name__ == "__main__":
    main()
