import random

# Split string method
names_string = input("Введите имена всех присутствующих через запятую. ")
names = names_string.split(", ")
# random list method
#this
#rand_name = random.randint(0,len(names)-1)
#or this-
rand_name = random.choice(names)
print(f"{rand_name} платит за счет сегодня")
