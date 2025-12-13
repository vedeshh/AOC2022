with open("input.txt","r") as file:
    games = file.read().strip().splitlines()
    
    my_scores = []
    
    for outcome in games:
        signs = outcome.split()
        for input in signs:
            if input == "A":
                opp = 1
            elif input == "B":
                opp = 2
            elif input == "C":
                opp = 3
            elif input == "X":
                home = 1
            elif input == "Y":
                home = 2
            else:
                home = 3
        if opp == home:
            my_scores.append(3+home)
        else:
            if opp + 1 > 3:
                opp = opp % 3
            if home == opp + 1:
                my_scores.append(6+home)
            else:
                my_scores.append(home)
    print(sum(my_scores))