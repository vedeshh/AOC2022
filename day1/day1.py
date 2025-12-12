with open("input.txt", "r") as file:
    data = file.read().strip()
    calories_str = data.split("\n\n")
    calories_with_elf = []
    for snack_strs in calories_str:
        calories_per_snack = snack_strs.split("\n")
        sum = 0
        for calorie_per_snack_str in calories_per_snack:
            calorie_per_snack_str = int(calorie_per_snack_str)
            sum += calorie_per_snack_str
        calories_with_elf.append(sum)
print(max(calories_with_elf))