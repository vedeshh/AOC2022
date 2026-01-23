with open("input.txt", "r") as file:
    games = file.read().strip().splitlines()
    
    score_map = { "A": 1, "B": 2, "C": 3, #opponent inputs
                  "X": 1, "Y": 2, "Z": 3  #outcome requirements X - lose; Y - draw; Z = win
                }

    scores = []

    for game in games:
        opp, outcome = (score_map[s] for s in game.split())
        
        if outcome == 1:
            if opp + 2 > 3:
                scores.append((opp + 2) % 3)
            else:
                scores.append(3)
        elif outcome == 2:
            scores.append(opp + 3)
        else:
            if opp + 1 > 3:
                scores.append(7)
            else:
                scores.append(opp + 7)
        
    print(sum(scores))