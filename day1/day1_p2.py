with open("input.txt","r") as file:
    content = file.read().strip()
    elves_snacks_log = content.split("\n\n")
    
    total_snacks_array = []
    
    for elf in elves_snacks_log:
        sum_of_snacks = sum(map(int,elf.splitlines()))
        total_snacks_array.append(sum_of_snacks)
    
    total_snacks_array.sort()

    print(sum(total_snacks_array[-3:])) 