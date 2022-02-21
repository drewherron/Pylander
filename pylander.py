import os
import random
import time

# How long should each battle last?
battle_length = 1

# Your files feel an irresistible pull...
def gathering():
    immortals = []
    for subdir, dirs, files in os.walk('./'):
        for file in files:
            # This file is on holy ground
            if 'pylander' in file:
                continue
            else:
                immortals += [os.path.join(subdir,file)]
    return immortals

print("Files loaded.")
time.sleep(1)
print("The Gathering is complete.")
time.sleep(1)
print("There can be only one.")
time.sleep(1)

def encounter(immortals):
    if len(immortals) > 1:
        fighters = random.sample(immortals, 2)
        print(fighters[0], "vs.", fighters[1])
        time.sleep(battle_length)
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
    time.sleep(battle_length)

immortals = gathering()
while len(immortals) > 1:
    immortals = gathering()
    fighters = encounter(immortals)
    duel(fighters)
