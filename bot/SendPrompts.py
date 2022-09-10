
import action 

with open('input.txt') as f:
    prompts = f.readlines()

for prompt in prompts:
    print(prompt)
    action.sendPrompt(prompt)