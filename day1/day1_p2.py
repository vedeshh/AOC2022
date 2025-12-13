with open("input.txt","r") as file:
    
    elves_snacks_log = file.read().strip().split("\n\n")
    
    snacks_array = [sum(map(int,s.splitlines())) for s in elves_snacks_log]

    print(sum(sorted(snacks_array)[-3:]))