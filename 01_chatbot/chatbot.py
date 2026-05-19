"""
Rule-Based Chatbot
Demonstrates: control flow, decision-making logic, basic AI concepts
"""

def get_response(user_input):
    user_input = user_input.lower().strip()

    # Exit commands
    if user_input in ["quit", "exit", "bye", "goodbye"]:
        return "EXIT"
    # Positive reactions
    elif user_input in ["wow", "whoa", "omg", "amazing", "awesome", "cool", "nice", "great", "incredible", "unbelievable","haha"]:
        return "Glad that impressed you! 😄"

    # Greetings
    elif user_input in ["hi", "hello", "hey", "howdy", "greetings"]:
        return "Hello! How can I help you today?"

    # How are you
    elif "how are you" in user_input or "how r u" in user_input:
        return "I'm just a bot, but I'm running fine! What about you?"

    # Name
    elif "your name" in user_input or "who are you" in user_input:
        return "I'm RuleBot — a simple rule-based chatbot."

    # Help
    elif "help" in user_input:
        return "I can answer basic questions. Try: greetings, 'what's the time', 'tell me a joke', or 'what can you do'."
   
    # Capabilities
    elif any(phrase in user_input for phrase in ["what can you do", "capabilities", "what do you do", "what are you doing", "what r u doing", "watcha doing", "what do u do"]):
        return "I chat, tell jokes, give the time/date, and answer simple questions. Try typing 'help' for more!"
    # Time
    elif "time" in user_input:
        from datetime import datetime
        return f"Current time: {datetime.now().strftime('%H:%M:%S')}"

    # Date
    elif "date" in user_input or "today" in user_input:
        from datetime import datetime
        return f"Today's date: {datetime.now().strftime('%A, %B %d, %Y')}"

    # Joke
    elif "joke" in user_input:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    # Capabilities
    elif "what can you do" in user_input or "capabilities" in user_input:
        return "I can: greet you, tell jokes, give the time/date, and answer simple questions."

    # Thanks
    elif user_input in ["thanks", "thank you", "thx", "ty"]:
        return "You're welcome!"

    # Basic Calculations
    elif any(op in user_input for op in ["+", "-", "*", "/"]):
        try:
            result = eval(user_input, {"__builtins__": {}})
            return f"The answer is: {result}"
        except:
            return "Couldn't calculate that. Try something like: 5 + 3 or 10 / 2"

    # Unknown
    else:
        return f"I don't understand '{user_input}'. Type 'help' to see what I can do."


def main():
    print("=" * 40)
    print("       Welcome to RuleBot")
    print("  Type 'quit' or 'exit' to stop")
    print("=" * 40)

    while True:
        user_input = input("\nYou: ").strip()

        if not user_input:
            print("Bot: Please type something.")
            continue

        response = get_response(user_input)

        if response == "EXIT":
            print("Bot: Goodbye! Have a great day.")
            break

        print(f"Bot: {response}")


if __name__ == "__main__":
    main()
