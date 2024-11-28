import random
from datetime import datetime

def chatbot():
    print("Chatbot: Hello! I'm your friendly assistant. Let me know how I can help you!")
    print("Type 'exit' anytime to leave the chat.\n")

    # Predefined data
    data = {
        "jokes": [
            "Why don’t scientists eat clocks? Because it's too time-consuming!",
            "Why was the math book sad? It had too many problems.",
            "What do you call a dinosaur with an extensive vocabulary? A thesaurus!",
            "How does the ocean say hi? It waves!",
            "Why did the tomato blush? Because it saw the salad dressing!"
        ],
        "quotes": [
            "Do not wait to strike till the iron is hot, but make it hot by striking. - William Butler Yeats",
            "Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs",
            "Happiness depends upon ourselves. - Aristotle",
            "In a gentle way, you can shake the world. - Mahatma Gandhi",
            "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
        ],
        "capitals": {
            "spain": "The capital of Spain is Madrid.",
            "mexico": "The capital of Mexico is Mexico City.",
            "egypt": "The capital of Egypt is Cairo.",
            "south africa": "South Africa has three capitals: Pretoria, Bloemfontein, and Cape Town.",
            "thailand": "The capital of Thailand is Bangkok."
        },
        "facts": {
            "sports": [
                "Michael Phelps has won more Olympic medals than 161 countries.",
                "Golf is the only sport to have been played on the moon.",
                "The FIFA World Cup is the most-watched sporting event in the world."
            ],
            "space": [
                "Saturn has 83 moons, the most in the solar system.",
                "A neutron star is so dense that a sugar-cube-sized amount of its material would weigh a billion tons.",
                "The sun accounts for about 99.86% of the mass in the solar system."
            ],
            "history": [
                "The shortest war in history lasted 38 minutes between Britain and Zanzibar in 1896.",
                "Leonardo da Vinci could write with one hand while drawing with the other.",
                "Cleopatra lived closer in time to the iPhone than the building of the Great Pyramid."
            ],
            "movies": [
                "The first animated film to be nominated for Best Picture at the Oscars was 'Beauty and the Beast' in 1991.",
                "In 'The Wizard of Oz,' the snow in the poppy field scene was actually asbestos.",
                "James Cameron drew the famous nude sketch of Rose in 'Titanic.'"
            ]
        }
    }

    # Helper functions
    def handle_greetings():
        print("Chatbot: Hi there! How can I assist you today?")

    def handle_time():
        current_time = datetime.now().strftime("%H:%M:%S")
        print(f"Chatbot: The current time is {current_time}.")

    def handle_date():
        current_date = datetime.now().strftime("%Y-%m-%d")
        print(f"Chatbot: Today's date is {current_date}.")

    def handle_joke():
        print(f"Chatbot: Here's a joke for you: {random.choice(data['jokes'])}")

    def handle_quote():
        print(f"Chatbot: Here's an inspirational quote: {random.choice(data['quotes'])}")

    def handle_capital(user_input):
        country = user_input.split("capital of")[-1].strip()
        response = data["capitals"].get(country, f"Sorry, I don't know the capital of {country}.")
        print(f"Chatbot: {response}")

    def handle_fact(category):
        facts = data["facts"].get(category)
        if facts:
            print(f"Chatbot: Here's a {category} fact: {random.choice(facts)}")
        else:
            print(f"Chatbot: Sorry, I don't have any facts about {category}.")

    def play_game():
        print("Chatbot: Let's play a number guessing game! Guess a number between 1 and 20.")
        number = random.randint(1, 20)
        while True:
            try:
                guess = int(input("You: "))
                if guess == number:
                    print("Chatbot: You got it! Well done!")
                    break
                elif guess < number:
                    print("Chatbot: Too low. Try again!")
                else:
                    print("Chatbot: Too high. Try again!")
            except ValueError:
                print("Chatbot: Please enter a valid number.")

    # Main loop
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["exit", "bye", "quit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        elif user_input in ["hi", "hello", "hey"]:
            handle_greetings()

        elif "time" in user_input:
            handle_time()

        elif "date" in user_input:
            handle_date()

        elif "joke" in user_input:
            handle_joke()

        elif "quote" in user_input:
            handle_quote()

        elif "capital of" in user_input:
            handle_capital(user_input)

        elif "sports fact" in user_input:
            handle_fact("sports")

        elif "space fact" in user_input:
            handle_fact("space")

        elif "history fact" in user_input:
            handle_fact("history")

        elif "movie trivia" in user_input:
            handle_fact("movies")

        elif "play a game" in user_input:
            play_game()

        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you try asking differently?")

chatbot()
