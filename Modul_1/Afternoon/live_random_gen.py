"""
Use appropriate functions in the random module for 
generating integers and real numbers
Integer between 1 and 100
Real number between 0 and 1
Seeding the random number generator
Setting a seed for reproducibilitiy
"""

import random

#Integer between 1 and 100
result_int = random.randint(1,100)
print(result_int)

#Real number between 0 and 1
result_real = random.random()
print(result_real)

#Seeding the random number generator
#Setting a seed for reproducibilitiy
print("Seeding the RNG.")
random.seed(3)
#Integer between 1 and 100
result_int = random.randint(1,100)
print(result_int)

#Real number between 0 and 1
result_real = random.random()
print(result_real)
