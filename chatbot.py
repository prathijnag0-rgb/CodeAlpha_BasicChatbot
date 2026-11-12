print("=" * 40)
print("       WELCOME TO PYTHON CHATBOT")
print("=" * 40)

print("Bot: Hello! I am your Python chatbot.")
print("Bot: You can talk to me.")
print("Bot: Type 'bye' to exit the chat.")

responses = {
    "hello": "Hi! How can I help you?",
    "hi": "Hello! Nice to meet you.",
    "how are you": "I'm fine, thanks!",
    "what is your name": "I am Python Chatbot.",
    "who created you": "I was created using Python.",
    "what can you do": "I can answer simple questions.",
    "thank you": "You're welcome!",
    "thanks": "Happy to help!",
    "good morning": "Good morning! Have a great day!",
    "good night": "Good night! Sweet dreams!"
}

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input == "bye":
        print("Bot: Goodbye! Have a nice day!")
        break

    elif user_input in responses:
        print("Bot:", responses[user_input])

    else:
        print("Bot: Sorry, I don't understand that.")
        print("Bot: Please try another message.")

print("\nChatbot session ended.")
