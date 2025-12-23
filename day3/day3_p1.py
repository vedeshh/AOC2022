with open("input.txt","r") as file:
    data = file.read().strip().splitlines()

    value = []

    for entry in data:
        length = len(entry)
        compartment1 = entry[0:(length//2)]
        compartment2 = entry[(length//2):]
        for letter in compartment1:
            if letter in compartment2:
                if ord(letter) < 91:
                    value.append(ord(letter) - 64 + 26)
                    break
                else:
                    value.append(ord(letter) - 96)
                    break
                

# print(ord("A"))
print(sum(value))
