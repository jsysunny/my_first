import random
animals=['cat','dog','turtle','mouse']
print(random.choice(animals))
print(random.sample(animals,2))
print(random.randint(1,6))

from random import choice
from random import sample
from random import randint
animals=['c','d','t','m']
print(choice(animals))
print(sample(animals,2))
print(randint(1,6))