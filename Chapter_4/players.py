players = ['charles', 'martina', 'michael', 'florence', 'eli']

print(players)
print(players[0:3])
print(players[1:3])
print(players[:3])
print(players[2:])
print(players[-3:])


for player in players[:3]:
    print(f'Here are the first three: {player.title()}')