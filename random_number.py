import random
x = random.randint(1,6)
y = random.random()
myList=["rock", "paper", "scissor"]
z = random.choice(myList)
cards=[1,2,3,4,5,6,"j","q"]
random.shuffle(cards)
print(cards)