games = ["The Last of Us", "Valorant", "Rocket League", "God of War"]
print("My favorite games are", games[0]+",", games[1]+",", games[2]+", and", games[3])
game = ""
while game != "quit":
    game = input("What is your favorite game? Enter a game or enter 'quit': ")
    games.append(game)
    print("My favorite games are" , ', '.join(games))
