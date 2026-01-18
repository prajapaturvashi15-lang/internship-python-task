def chatbot():
    print("🤖 Welcome to Basic Chatbot")
    print("Type: hello, how are you, bye")

    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")
        elif user == "how are you":
            print("Bot: I'm fine, thanks for asking!")
        elif user == "bye":
            print("Bot: Goodbye! Have a nice day 😊")
            break
        else:
            print("Bot: Sorry, I don't understand.")

chatbot()