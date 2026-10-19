MODEL = "gemma3"
temperature = 0.2
max_tokens = 300
stream = False
system_prompt = "You are a helpful Python tutor"

price_per_1k_tokens = 0.5
tokens_used = int(input("Tokens used: "))
cost = tokens_used / 1000 * price_per_1k_tokens
print("--- AI Model Profile Card ---")
print(f"Model: {MODEL} ({type(MODEL)})")
print(f"Temperature: {temperature} ({type(temperature)})")
print(f"Max tokens: {max_tokens} ({type(max_tokens)})")
print(f"Streaming: {stream} ({type(stream)})")
print(f"System prompt: {system_prompt} ({type(system_prompt)})")
print(f"Estimated cost: {round(cost, 2)} PKR")

api_key = None
print(f"API key: {api_key} ({type(api_key)})")