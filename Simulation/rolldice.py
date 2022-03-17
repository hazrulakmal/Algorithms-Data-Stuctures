import random
import matplotlib.pyplot as plt


def event(goals, numtrials):
    total = 0
    for j in range(numtrials): 
        end = ""
        for i in range(len(goals)):
            result = random.choice([1,2,3,4,5,6])
            end += str(result)
        if end == goals:
            total += 1
    return round(total/numtrials, 9)
    


trials = [i for i in range(1, 100000, 100)]
prob = []

for i in trials:
    prob.append(event("1111", i))
    
    
plt.plot(trials, prob)