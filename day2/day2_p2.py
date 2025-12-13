with open("sample.txt", "r") as file:
    games = file.read().strip().splitlines()
    
    score_map = { "A": 1, "B": 2, "C": 3, #opponent inputs
                  "X": 1, "Y": 2, "Z": 3  #outcome requirements X - lose; Y - draw; Z = win
                }

    scores = []

    for game in games:
        opp, outcome = (score_map[s] for s in game.split())
        
        if outcome == 3:
            if opp == 3:
                scores.append(1+6)
            else:
                scores.append(opp + 1)
        elif outcome == 2:
            scores.append(opp + 3)
        else:
            if opp == 1:
                scores.append(3)
            else:
                scores.append(opp - 1)
    
    print(sum(scores))