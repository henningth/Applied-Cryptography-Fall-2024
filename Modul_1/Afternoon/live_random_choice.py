"""
Choosing elements at random from a list
Single random choice
Multiple random choices with replacement
Weighted random choices
Random sample without replacement
"""
import random
mylist = ['apple', 'microsoft', 'google', 'meta', 'lenovo']
# Single random choice
result1 = random.choice(mylist)
print(result1)
# Multiple random choices with replacement
result2 = random.choices(mylist, k=2)
print(result2)
# Weighted random choices
result3 = random.choices(mylist, weights=[1,100,1,1,1], k=1)
print(result3)
# Random sample without replacement
result4 = random.sample(mylist, k=6)
print(result4)