with open("input.txt","r") as file:
    pairs = file.read().strip().splitlines()

    overlaps = 0
    
    for pair in pairs:
        firstparam,secondparam = pair.split(",")

        a,b = map(int,firstparam.split("-"))
        x,y = map(int,secondparam.split("-"))

        firstrooms = set(range(a,b+1))
        secondrooms = set(range(x,y+1))

        if not firstrooms.isdisjoint(secondrooms):
            overlaps += 1

print(overlaps)