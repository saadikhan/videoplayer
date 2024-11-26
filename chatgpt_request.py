import openai

openai.api_key = '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'  # Replace with your actual API key

# Create a chat completion request using the new interface
response = openai.ChatCompletion.create(
    model="gpt-4",  # You can use "gpt-4" or another model based on your needs
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, how are you?"}
    ]
)

# Print the assistant's response
print(response['choices'][0]['message']['content'])
