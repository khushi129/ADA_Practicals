def spam_detector(email_text):
    spam_keywords = ["win", "free", "cash", "click", "offer", "urgent"]
    return "SPAM" if any(word in email_text.lower() for word in spam_keywords) else "NOT SPAM"
def career_guidance(field):
    suggestions = {
        "computer science": "Consider roles in software development, AI, or cybersecurity.",
        "biology": "Explore careers in biotechnology, lab research, or medicine.",
        "business": "You could look into marketing, management, or entrepreneurship.",
        "design": "Think about UX/UI design, graphic design, or animation.",
    }
    return suggestions.get(field.lower(), "Field not found. Please consult a counselor for more info.")
def shopping_assistant(query):
    responses = {
        "laptop": "We have offers on HP and Dell laptops. Looking for gaming or work-related use?",
        "shoes": "Sports, casual, or formal? I can help you find trending styles.",
        "sale": "Seasonal discounts are live! Want me to show top deals?",
    }
    for word, reply in responses.items():
        if word in query.lower():
            return reply
    return "Sorry, I didn’t get that. Can you rephrase or ask about another product?"
def intelligent_system_types():
    types = {
        "Reactive Machines": "Respond only to present inputs. No memory. (e.g., simple calculators)",
        "Limited Memory": "Remember short-term events. (e.g., self-driving cars)",
        "Theory of Mind": "Future AI that can understand feelings and thoughts.",
        "Self-aware": "Theoretical systems aware of their own existence.",
    }
    return types
def main():
    print("\n=== AI Demonstration Console ===")
    while True:
        print("\nChoose an AI feature to try:")
        print("1. Spam Detector (Learning)")
        print("2. Career Guidance (Reasoning)")
        print("3. Shopping Assistant (NLP & Perception)")
        print("4. AI System Categories")
        print("5. AI in Real Life")
        print("6. Exit")
        choice = input("Your choice (1-6): ")
        match choice:
            case "1":
                email = input("Enter an email message: ")
                result = spam_detector(email)
                print(f"Detection: {result}")
            case "2":
                subject = input("Enter a study field (e.g., biology, design): ")
                suggestion = career_guidance(subject)
                print(f"Career Advice: {suggestion}")
            case "3":
                user_query = input("You: ")
                reply = shopping_assistant(user_query)
                print(f"Assistant: {reply}")
            case "4":
                types = intelligent_system_types()
                for category, explanation in types.items():
                    print(f"{category}: {explanation}")
            case "5":
                print("\n--- Real-World AI Applications ---")
                print("- AI-powered job resume screening tools")
                print("- Virtual tutors in e-learning platforms")
                print("- Smart refrigerators that auto-restock items")
                print("- Face recognition at airports")
                print("- ChatGPT for customer support and content creation")
            case "6":
                print("Goodbye! Thanks for exploring AI examples.")
                break
            case _:
                print("Invalid input. Please select a number from 1 to 6.")
if __name__ == "__main__":
    main()
print("\nShah Khushi\n240905041029")
