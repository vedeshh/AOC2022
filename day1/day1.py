with open("sample.txt", "r") as file:
    
    data = file.read().strip().split("\n\n")
    result = [sum(map(int, i.splitlines())) for i in data]

    print(max(result))