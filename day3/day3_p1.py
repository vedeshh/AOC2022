def priority(c: str):
    return ord(c) - 38 if c.isupper() else ord(c) - 96

total = 0

with open("sample.txt","r") as file:
    for line in file.read().strip().splitlines():
        mid = len(line) // 2
        comp1,comp2 = line[:mid],line[mid:]

        common_char = (set(comp1) & set(comp2)).pop()
        total += priority(common_char)

print(total)
        