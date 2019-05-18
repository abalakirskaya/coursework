def ration(user_breakfast_calories, user_breakfast_proteins, user_breakfast_fats, user_breakfast_carbohydrates, user_dinner_calories, user_dinner_proteins, user_dinner_fats, user_dinner_carbohydrates, user_supper_calories, user_supper_proteins, user_supper_fats, user_supper_carbohydrates, file):

    '''
    (int...) -> list
    A function which returnes menu for user by his/her needs
    '''


    user_calories = user_breakfast_calories + user_dinner_calories + user_supper_calories
    user_proteins = user_breakfast_proteins + user_dinner_proteins + user_supper_proteins
    user_fats = user_breakfast_fats + user_dinner_fats + user_supper_fats
    user_carbohydrates = user_breakfast_carbohydrates + user_dinner_carbohydrates + user_supper_carbohydrates



    user_menu = [[], [], [], []]

    menu = []
    for line in file:
        menu.append(line[:-1].split(' : '))
    difference = 0
    min_difference = 500
    index = 0
    second = 0
    for i in range(0, len(menu)):
        if menu[i][0] == 'САЛАТИ':
            second = i
            break
    for i in range(second, len(menu)):
        if len(menu[i]) != 1:
            difference = user_breakfast_carbohydrates - float(menu[i][4]) * float(menu[i][1])/100
            if difference < min_difference:
                min_difference = difference
                index = i
    user_calories -= float(menu[index][5])
    user_proteins -= float(menu[index][2])
    user_fats -= float(menu[index][3])
    user_carbohydrates -= float(menu[index][4])
    user_menu[0].append(menu.pop(index))
    # ***
    difference = 0
    min_difference = 500
    index = 0
    stop = 0
    while user_dinner_carbohydrates > 0:
        if len(menu) < 5:
            stop = 1
        for i in range(0, len(menu)):
            if len(menu[i]) != 1:
                difference = user_dinner_carbohydrates - float(menu[i][4]) * float(menu[i][1])/100
                if difference < min_difference:
                    min_difference = difference
                    index = i
        try:
            if len(menu[index]) != 1:
                user_dinner_carbohydrates -= float(menu[index][4])
                user_calories -= float(menu[index][5])
                user_proteins -= float(menu[index][2])
                user_fats -= float(menu[index][3])
                user_carbohydrates -= float(menu[index][4])
                user_menu[1].append(menu.pop(index))
        except:
            stop = 1
        if stop == 1:
            break
    difference = 0
    min_difference = 500
    index = 0
    second = 0
    for i in range(0, len(menu)):
        if menu[i][0] == 'ДРУГI СТРАВИ':
            second = i
            break
    if user_dinner_carbohydrates > 10:
        for i in range(second, len(menu)):
            if len(menu[i]) != 1:
                difference = user_dinner_carbohydrates - float(menu[i][4]) * float(menu[i][1])/100
                if difference < min_difference:
                    min_difference = difference
                    index = i
        user_calories -= float(menu[index][5])
        user_proteins -= float(menu[index][2])
        user_fats -= float(menu[index][3])
        user_carbohydrates -= float(menu[index][4])
        user_menu[1].append(menu.pop(index))
    # ***
    difference = 0
    min_difference = 500
    index = 0
    for i in range(0, len(menu)):
        if len(menu[i]) != 1:
            difference = user_supper_carbohydrates - float(menu[i][4]) * float(menu[i][1])/100
            if difference < min_difference:
                min_difference = difference
                index = i
    try:
        user_calories -= float(menu[index][5])
        user_proteins -= float(menu[index][2])
        user_fats -= float(menu[index][3])
        user_carbohydrates -= float(menu[index][4])
        user_menu[2].append(menu.pop(index))
    except:
        pass
    # ***
    difference = 0
    min_difference = 500
    index = 0
    while user_carbohydrates > 0:
        for i in range(0, len(menu)):
            if len(menu[i]) != 1:
                difference = user_carbohydrates - float(menu[i][4]) * float(menu[i][1])/100
                if difference < min_difference:
                    min_difference = difference
                    index = i
        try:
            if len(menu[index]) != 1:
                user_calories -= float(menu[index][5]) * float(menu[index][1])/100
                user_proteins -= float(menu[index][2]) * float(menu[index][1])/100
                user_fats -= float(menu[index][3]) * float(menu[index][1])/100
                user_carbohydrates -= float(menu[index][4]) * float(menu[index][1])/100
                user_menu[3].append(menu.pop(index))
        except:
            break
    return user_menu
