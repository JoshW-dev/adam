import action 
import random

from clickerTyper import commands


with open('input1.txt') as f:
    prompts = f.read().splitlines()

tags = ""


print("Started...")
for prompt in prompts:
    fullPrompt = (prompt +tags)
    print(fullPrompt)
    
    action.sendPrompt(fullPrompt)
    print("init gen...70")
    commands.wait(70) 
    #approx initial generation wait time + 10 seconds (relaxed) 
    action.upscale1(random.randint(1, 4))
    print("init upscale...120")
    commands.wait(120) 
    #approx first upscale wait time + 20 seconds (relaxed)
    action.upscale1("remaster")
    print("init remaster...80")
    commands.wait(90) 
    action.upscale1("remaster#1")
    print("second remaster...90")
    commands.wait(60) 
    print("prompt complete")
    
    
    #approx light redo upscale wait time (relaxed) - 60
    #approx beta redo upscale wait time (relaxed) - 70
    #approx remaster redo upscale wait time (relaxed) - 

print("done")