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
            # but this file is on holy ground
            if 'pylander' in file:
                continue
            else:
                immortals += [os.path.join(subdir,file)]
    return immortals

# What is happening?
print()
print("All files loaded.")
time.sleep(.5)
print("The Gathering is complete.")
time.sleep(1)
print("There can be only one.\n")
time.sleep(1)

# Why does the sun come up?
def encounter(immortals):
    if len(immortals) > 1:
        fighters = random.sample(immortals, 2)
        print(fighters[0], " vs ", fighters[1])
        time.sleep(battle_length)
    return fighters

# Or are the stars just pinholes in the curtain of night?
def quickening(winner):
    if len(immortals) == 1:
        print(winner, "wins the Prize.\n")

# Who knows?
def duel(fighters):
    # It's all decided for us
    fail = random.randint(0,1)
    print(fighters[fail], "deleted.\n")
    os.remove(fighters[fail])
    fighters.remove(fighters[fail])
    immortals.remove(immortals[fail])
    # This world has only
    winner = fighters[0]
    # one sweet moment
    quickening(winner)
    # set aside for us
    time.sleep(battle_length)

# Who wants to live forever?
immortals = gathering()
while len(immortals) > 1:
    immortals = gathering()
    fighters = encounter(immortals)
    duel(fighters)
