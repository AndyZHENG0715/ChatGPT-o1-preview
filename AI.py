import os
from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import UserMessage
from azure.core.credentials import AzureKeyCredential

# Initialize the ChatCompletionsClient
client = ChatCompletionsClient(
    endpoint="https://models.inference.ai.azure.com",
    credential=AzureKeyCredential(os.environ.get("GITHUB_TOKEN")),
)

def select_model():
    available_models = ["o1-mini", "o1-preview", "gpt-4o", "gpt-4o-mini"]
    print("Available Models:")
    for idx, model in enumerate(available_models, start=1):
        print(f"{idx}. {model}")
    
    while True:
        try:
            choice = int(input("Select a model by entering the number: ").strip())
            if 1 <= choice <= len(available_models):
                selected_model = available_models[choice - 1]
                print(f"Selected Model: {selected_model}")
                return selected_model
            else:
                print(f"Please enter a number between 1 and {len(available_models)}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def chat(selected_model):
    print("ChatBot initialized. Type 'q' to quit.")
    print("-" * 50)
    
    while True:
        # Get user input
        user_input = input("\nYou: ").strip()
        
        # Check for exit condition
        if user_input.lower() == 'q':
            print("Goodbye!")
            break
            
        # Skip empty inputs
        if not user_input:
            continue
            
        try:
            # Prepare the user message
            messages = [UserMessage(content=user_input)]
            
            # Get response from the model
            response = client.complete(
                messages=messages,
                model=selected_model
            )
            
            # Print the response
            print("\nBot:", response.choices[0].message.content)
            
        except Exception as e:
            print(f"\nError: {str(e)}")

if __name__ == "__main__":
    chosen_model = select_model()
    chat(chosen_model)