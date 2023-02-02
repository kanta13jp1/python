import openai

# Set your API key
openai.api_key = "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"

# Use the Image.create method to generate an image
response = openai.Image.create(
    prompt="玉木雄一郎"
)

# Print the response from the API
print(response)