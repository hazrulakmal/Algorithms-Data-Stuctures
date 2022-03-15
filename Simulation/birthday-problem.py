# SameBirthday Prob
import random

def SameBirthday(num_people, target_num):
    days = range(365)
    freq = [0] * 365
    for i in range(num_people):
        date = random.choice(days)
        freq[date] += 1
    return max(freq) > target_num


def Probility(trials, num_people, target_num):
    total = 0
    for i in range(trials):
        if SameBirthday(num_people, target_num):
            total += 1
    return total/trials

num_people = [5,15,30,50,80,100]
for i in num_people:
    print("esitimated probility", Probility(100000, i, 2))
        
#we can change the distribution of bithdates. For this case we assume equal distributiion across all days in a year but in reality this is not the case.
#we can change the target people, the math becomes more complicated but with simulation we can just change the parameter. 
#example we want probability of atleast 3 people share birhtday. there are three complementary event to consider 1) all distints 2) two pairs