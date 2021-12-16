def arrithmetic_arranger(number_set: list):

    #problem check
    if len(number_set) > 5:
        print("Error: Too many problems")
        return

    #separate each problem
    first_number = []
    operator = []
    second_number = []

    for i in range(len(number_set)):
        separated = number_set[i].split()
        first_number.append(separated[0])
        operator.append(separated[1])
        second_number.append(separated[2])

    #operation check
    op_check = True
    for op in operator:
        if op != "+" and op != "-":
            op_check = False
    if op_check == False:
        print("Error: Operator must be '+' or '-'")
        return
    
    #digit check
    digit_check = True
    for num in first_number:
        try:
            num = int(num)
        except:
            digit_check = False
    for num in second_number:
        try:
            num = int(num)
        except:
            digit_check = False
    if digit_check == False:
        print("Error: Number must contain only digit")
        return

    #number length check
    len_check = True
    for num in first_number:
        if len(num) > 4:
            len_check = False
    for num in second_number:
        if len(num) > 4:
            len_check = False
    if len_check == False:
        print("Error: Number cannot be more than four digit")
        return

    #calculate
    answer = []
    for i in range(len(number_set)):
        if operator[i] == "+":
            answer.append(int(first_number[i]) + int(second_number[i]))
        else:
            answer.append(int(first_number[i]) - int(second_number[i]))

    long = "0"
    for num in first_number:
        if len(num) > len(long):
            long = num
    for num in second_number:
        if len(num) > len(long):
            long = num
    
    space = len(long) + 3

    first_line = " "
    second_line = " "
    third_line = " "
    forth_line = " "
    line = "-------"
    for i in range(len(number_set)):
        first_line = first_line + "    " + f"{first_number[i]: >{space}}"
        second_line = second_line + "    " + f"{operator[i]: <2} {second_number[i]: >{len(long)}}"
        third_line = third_line + "    " + f"{line[:space]}"   
        forth_line = forth_line + "    " + f"{answer[i]: >{space}}"

    print(first_line)
    print(second_line)
    print(third_line)
    print(forth_line)

