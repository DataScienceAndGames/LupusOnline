import random
players = [] #in case you fear that someone could cheat, use a hash function and use the hash of the players instead of their name. Tell to every player what is their hash, but to not tell them the hash function
roles = []
with open ("players.txt","r") as r:
    lines = r.readlines()
    for line in lines:
        players.append(line.rstrip())
with open ("roles.txt","r") as r:
    lines = r.readlines()
    for line in lines:
        roles.append(line.rstrip())
random.shuffle(roles)
for i in range(len(players)):
    with open(players[i]+".txt","w") as w:
        w.write(roles[i])

with open("all_roles.txt","w") as w:
    for i in range(len(players)):
        w.write(players[i] + "\t" + roles[i] + "\n")
