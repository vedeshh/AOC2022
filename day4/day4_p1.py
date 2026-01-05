with open("input.txt","r") as file:
    pairs = file.read().strip().splitlines()
    overlaps = 0

    for pair in pairs:
        #  a- b = first guy
        #  x - y = second guy
        firstparam,secondparam = pair.split(",")
        
        a,b = map(int,firstparam.split("-"))
        x,y = map(int,secondparam.split("-"))
        
        firstrooms = set(range(a,b+1))
        secondrooms = set(range(x,y+1))
        
        if firstrooms.issuperset(secondrooms) or secondrooms.issuperset(firstrooms):
            overlaps += 1
    
    print(overlaps)