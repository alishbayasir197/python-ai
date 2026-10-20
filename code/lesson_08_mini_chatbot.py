
BOT = "Dresses Shop Bot"

print(f"{BOT}: Welcome! I can help with prices, orders, delivery and complaints.")
print("Type bye to exit.")

name = input("Bot: What is your name? ").strip().title()

if name == "":
    name = "friend"

print(f"Bot: Nice to meet you, {name}!")

count = 0
unanswered = 0

while True:
    message = input(f"{name}: ").strip().lower()
    count += 1

    if message == "bye" or message == "exit":
        print(f"Bot: Goodbye, {name}!")
        break

    elif message == "":
        print("Bot: Please type a question.")

    elif "complaint" in message or "refund" in message or "late" in message:
        print("Bot: Sorry! Our team will help you.")

    elif "price" in message or "cost" in message or "how much" in message:
        print("Bot: Please contact our shop for current prices.")

    elif "delivery" in message or "shipping" in message:
        print("Bot: Please contact our shop for delivery details.")

    elif "where" in message or "location" in message or "address" in message:
        print("Bot: Please contact our shop for the address.")

    elif "order" in message:
        print("Bot: Please share your order details with our team.")

    elif message in ("hi", "hello") or message.startswith("salam"):
        print(f"Bot: Hello again, {name}! How can I help?")

    else:
        unanswered += 1
        prompt = f"You are a helpful dresses shop assistant. Answer in 2 lines: {message}"
        print("Bot: I don't know this answer yet.")
        print(f"AI prompt: {prompt}")

print("=" * 35)
print(f"Chat summary: {count} messages")
print(f"Unanswered questions: {unanswered}")
