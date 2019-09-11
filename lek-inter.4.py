# en slumpgenerator
# program som rullar en tärning

import random # laddar in random klassen så vi kan använda den

print("Vill du rulla en tärning?") # meddelande till användaren

# försök läsa in sides som en int, vid fel sätt sides till 1
try:
    sides = int(input("Hur många sidor vill du rulla:"))
except:
    print("Tärningen behöver 1+ sidor")
    sides = 1

run = "y" # vi ger run värdet y som standard

# Så länge run == y kör loopen
while run.lower() == "y":
    randomNumber = random.randint(1, sides)
    print(randomNumber)

# Fråga om användaren vill fortsätta rulla träning
    run = input("Vill du rulla en tärning[y/n]: ")