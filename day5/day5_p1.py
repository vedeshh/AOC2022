with open("input.txt","r") as file:
    #  THIS PART HANDLES READING THE INPUT FOR FURTHER OPERATIONS
    
    structure,instructions = file.read().split("\n\n")

    columns = (structure.find('\n') + 1) // 4

    total_list = []

    column_index = 1
    for i in range(columns):
        temp_list = []
        for c in structure[column_index:structure.find('1'):columns * 4]:
            if c != ' ': 
                temp_list.append(c)
        temp_list.reverse()
        total_list.append(temp_list)
        column_index += 4
    # print(total_list)
    
    # THIS PART READS THE INSTRUTIONS AND DOES THE REQUIRED OPERATIONS

    for line in instructions.splitlines():
        # let (a,b,c) be the triplet of numbers that operations are done by
        operation_triplet = []
        
        for number in line.split():
            if number.isdigit():
                operation_triplet.append(number)
        quantity,place,to = map(int,operation_triplet)

        for i in range(quantity):
            total_list[to-1].append(total_list[place-1].pop())

    top_string = ''
    for j in range(columns):
        top_string = top_string + total_list[j].pop()
    print(top_string)