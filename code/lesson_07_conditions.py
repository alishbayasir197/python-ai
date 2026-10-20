
task = input("Task (code / private / chat): ").strip().lower()
tokens = int(input("Estimated tokens: "))

if task == "private":
    model = "llama3.2 (local, Ollama)"
    cost = 0
elif task == "code":
    model = "claude (cloud)"
    cost = tokens / 1000 * 0.01
elif task == "chat":
    model = "small cloud model"
    cost = tokens / 1000 * 0.001
else:
    model = "unknown"
    cost = 0

if tokens > 4000:
    warning = "Long request: consider shortening it."
else:
    warning = "Length is fine."

print("=" * 40)
print(f"Chosen model: {model}")
print(warning)
print(f"Estimated cost: ${cost:.4f}")
