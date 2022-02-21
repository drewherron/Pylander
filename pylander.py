import os
import random
import time

battle_speed = 3

# Populate list of all files in dir/subdirs
immortals = []
for subdir, dirs, files in os.walk('./'):
    for file in files:
        # Don't add this program
        if 'pylander' in file:
            continue
        else:
            immortals += [os.path.join(subdir,file)]

print("Files loaded.")
time.sleep(1)
print("The Gathering is complete.")
time.sleep(1)
print("There can be only one.")
time.sleep(1)


# Pick two random files
def encounter(immortals):
    if len(immortals) > 1:
        fighters = random.sample(immortals, 2)
        #print("Immortals: ", immortals)
        #print("Fighters: ", fighters)
        print(fighters[0], "vs.", fighters[1])
        time.sleep(battle_speed)
    return fighters

def quickening(victor):
    if len(immortals) == 1:
        print(immortals[0], "wins the Prize.")

def duel(fighters):
    fail = random.randint(0,1)
    print("fail: ", fail)
    print(fighters[fail], "deleted.")
    os.remove(fighters[fail])
    fighters.remove(fighters[fail])
    immortals.remove(immortals[fail])
    victor = fighters[0]
    quickening(victor)
    time.sleep(battle_speed)


while len(immortals) > 1:
    fighters = encounter(immortals)
    duel(fighters)
