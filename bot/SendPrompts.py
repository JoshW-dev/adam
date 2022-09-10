import action 
from clickerTyper import commands


with open('input.txt') as f:
    prompts = f.read().splitlines()

tags = ", ethereal, limerent, dream-like, black and white"


for prompt in prompts:
    fullPrompt = (prompt +tags)
    #print(fullPrompt)
    
    action.sendPrompt(fullPrompt)
    commands.wait(70) 
    #approx initial generation wait time + 10 seconds (relaxed) 
    action.upscale1(1)
    commands.wait(80) 
    #approx first upscale wait time + 20 seconds (relaxed)
    action.upscale1("remaster")
    commands.wait(80) 
    action.upscale1("remaster1")
    
    #approx light redo upscale wait time (relaxed) - 60
    #approx beta redo upscale wait time (relaxed) - 70
    #approx remaster redo upscale wait time (relaxed) - 
    