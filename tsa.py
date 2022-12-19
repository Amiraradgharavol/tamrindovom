import random
tas = random.randint(1, 6)
prize = random.randint(1, 6)
while True:
    if tas != 6:
        print(tas,"bakhti")
        break
    elif  tas == 6:
        print("tas number", tas)
        print("barande shodi va in tas avalet beonvan jaieze ", prize)
        break
