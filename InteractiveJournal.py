print("Welcome to your interactive journal!")

prompts = [
    "What were the high points and low points of my week, and what caused them?",
    "What were the things that brought me joy and happiness this week?",
    "What challenges did I face this week, and how did I overcome them?",
    "What did I learn about myself this week?",
    "What goals did I accomplish this week, and what goals did I fall short of?"
]

entries = []

for prompt in prompts:
    print(prompt)
    response = []
    try:
        while True:
            line = input()
            response.append(line)
    except EOFError:
        pass
    entries.append((prompt, '\n'.join(response)))

print("\nHere are your journal entries:")
for i, entry in enumerate(entries):
    prompt, response = entry
    print(f"Entry {i+1}: {prompt}\n{response}\n")
