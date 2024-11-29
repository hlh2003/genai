import openai


openai.api_key = "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"


def generate_learning_response(topic, level):
    """
    Generates an explanation for a given topic based on the user's learning level.
    
    :param topic: The topic to be explained.
    :param level: The learning level (beginner, intermediate, advanced).
    :return: AI-generated explanation for the topic.
    """
    prompt = f"""
    You are an AI tutor. Explain the topic "{topic}" in a way that matches the learning level:
    - Beginner: Use simple terms, examples, and step-by-step explanations.
    - Intermediate: Include moderate technical details and examples.
    - Advanced: Use technical language and in-depth analysis.

    Respond for the learning level: {level}.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "system", "content": "You are an expert tutor."},
                      {"role": "user", "content": prompt}]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return f"Error generating response: {e}"


def educational_chatbot():
    print("Welcome to the Generative AI Learning Assistant!")
    print("Transforming education by simplifying complex topics.")
    print("Type 'exit' anytime to end the session.")
    
    while True:
        
        topic = input("\nEnter the topic you want to learn about: ")
        if topic.lower() == 'exit':
            print("Goodbye! Keep learning!")
            break
        
        print("\nChoose your learning level:")
        print("1. Beginner")
        print("2. Intermediate")
        print("3. Advanced")
        level_choice = input("Enter the number corresponding to your learning level: ")
        
        level_mapping = {'1': "Beginner", '2': "Intermediate", '3': "Advanced"}
        level = level_mapping.get(level_choice, "Beginner") 
        
       
        print("\nGenerating response, please wait...\n")
        explanation = generate_learning_response(topic, level)
        print(f"AI Explanation ({level} Level):\n")
        print(explanation)


if __name__ == "__main__":
    educational_chatbot()
