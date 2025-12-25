def priority(c: str):
    return ord(c) - 38 if c.isupper() else ord(c) - 96

total = 0

with open("input.txt","r") as file:
    data = file.read().strip().splitlines()
    i = 0
    while i <= len(data) - 3:
        group1 = data[i] ; group2 = data[i+1] ; group3 = data[i+2]
        total += priority((set(group1) & set(group2) & set(group3)).pop())
        i += 3
    print(total)