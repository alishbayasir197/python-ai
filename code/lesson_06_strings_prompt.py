name = input("Your name: ")
raw = input("Your question: ")

clean_name = name.strip().title()
clean = raw.strip().capitalize()
estimated_tokens = round(len(clean) / 4)
short = clean[:150]
estimated_tokens = round(len(clean) / 4)
short = clean[:150]
mentions_python = "python" in clean.lower()
prompt = f"""You are a helpful Python tutor.
Answer in 3 lines.
Student name: {clean_name}
Question: {short}"""
print("=" * 40)
print(f"Cleaned name: {clean_name}")
print(f"Cleaned question: {clean}")
print(f"Characters: {len(clean)}")
print(f"Estimated tokens: {estimated_tokens}")
print(f"Mentions Python: {mentions_python}")
print("=" * 40)
print(prompt)