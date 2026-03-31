from blackrhinorandomminigame import random_minigame as rm

players = ["Alice", "Bob", "Charlie", "Diana"]

# chooses one of rock, paper, and scizzors
print("Choice:", rm.choose_option(["rock", "paper", "scissors"]))

# rolls a six-sided die, with faces numbered 1-6, twice 
print("Dice:", rm.roll_dice(2, 6, 1, 1))

# flips a coin five times
print("Coin:", rm.coin_flip(5))

# generates a score for each item in players
print("Scores:", rm.generate_scores(players, 0, 100, True))

# generates two teams out of the items in players
print("Teams:", rm.generate_teams(players, 2))