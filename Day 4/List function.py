
import random

names = ["Angela","Ben","Sean","Nicole"]
num_names = len(names)
random_choice = random.randint(0, num_names - 1)
person_who_will_pay = names[random_choice]
print(f"{person_who_will_pay} is going to buy the meaal today")