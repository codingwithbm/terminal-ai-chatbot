import google.generativeai as ai  # Import the Google Generative AI module

# API Key
API_KEY = 'your_api_key'  # Store your unique API key to authenticate requests

# Configure the API
ai.configure(api_key=API_KEY)  # Set the API key for the AI service to use

# Create a new model
model = ai.GenerativeModel("gemini-pro")  # Initialize the generative model (Gemini Pro)

chat = model.start_chat()  # Start a new chat session with the model

# Start a conversation
while True:  # Loop to continuously chat until 'bye' is typed
    message = input('You: ')  # Get user input for the chat message
    if message.lower() == 'bye':  # Exit the loop if user types 'bye'
        print('Chatbot: Goodbye!')  # Print a farewell message
        break  # Exit the loop and end the chat
    response = chat.send_message(message)  # Send the user's message to the model
    print('Chatbot:', response.text)  # Print the model's response
