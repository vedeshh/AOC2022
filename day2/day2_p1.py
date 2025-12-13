with open("input.txt","r") as file:
    
    games = file.read().strip().splitlines()
    
    #making a dict instead of using long if elif ladders

    score_map = { "A": 1, "B": 2, "C": 3, "X": 1, "Y": 2, "Z": 3 }

    scores = []

    for game in games:
        opp , home = (score_map[s] for s in game.split())
        if opp == home:
            scores.append(3 + home)
        elif home == (opp % 3) + 1:
            scores.append(6 + home)
        else:
            scores.append(home)
    print(sum(scores))