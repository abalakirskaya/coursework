from calculator import Calculator, DividedFood
import calculator
import user_menu
import menu
sex = input('Enter your sex - man of woman:\n')
age = int(input('Enter your age:\n'))
weidth = int(input('Enter your weidth:\n'))
kind = input('Enter which lifestyle do you have: passive, inactive or active?\n')
user = Calculator(weidth, age,kind, sex)
params = user.calculate()
print('Calculating individual menu for today...')
# ***

def proteins(calories):
    '''
    Auxiliary function which calculates proteins from calories
    '''
    return round(calories / 6 / 4, 1)


def fats(calories):
    '''
    Auxiliary function which calculates fats from calories
    '''
    return round(calories / 6 / 9, 1)


def carbohydrates(calories):
    '''
    Auxiliary function which calculates carbohydrates from calories
    '''
    return round(calories / 6, 1)
# ***
lists = menu.info()
food_list = lists[0]
food_weidth_list = lists[1]
food_data = open('data.txt', encoding = 'utf-8')
today_menu = open('today_menu.txt', 'w', encoding = 'utf-8')
for line in food_data:
    if 'САЛАТИ\n' == line or 'ПЕРШI СТРАВИ\n' == line or 'ГАРНIРИ\n' == line or 'ДРУГI СТРАВИ\n' == line:
        today_menu.write(line)
    for i in range(0, len(food_list)):
        if (food_list[i] + '"') in line:
            # print(line)
            today_menu.write(line)
food = DividedFood(params[0])
today_menu.close()


# Breakfast
user_breakfast_calories = food.breakfast()
user_breakfast_proteins = proteins(user_breakfast_calories)
user_breakfast_fats = fats(user_breakfast_calories)
user_breakfast_carbohydrates = carbohydrates(user_breakfast_calories)
# Dinner
user_dinner_calories = food.dinner()
user_dinner_proteins = proteins(user_dinner_calories)
user_dinner_fats = fats(user_dinner_calories)
user_dinner_carbohydrates = carbohydrates(user_dinner_calories)
# Supper
user_supper_calories = food.supper()
user_supper_proteins = proteins(user_supper_calories)
user_supper_fats = fats(user_supper_calories)
user_supper_carbohydrates = carbohydrates(user_supper_calories)

file = open('today_menu.txt', encoding = 'utf-8')
result_menu = user_menu.ration(user_breakfast_calories, user_breakfast_proteins, user_breakfast_fats, user_breakfast_carbohydrates, user_dinner_calories, user_dinner_proteins, user_dinner_fats, user_dinner_carbohydrates, user_supper_calories, user_supper_proteins, user_supper_fats, user_supper_carbohydrates, file)

print('For your breakfast you can take:')
for i in range(0, len(result_menu[0])):
    print(result_menu[0][i][0][1:-1])
print('For your dinner you can take:')
for i in range(0, len(result_menu[1])):
    print(result_menu[1][i][0][1:-1])
print('For your supper you can take:')
for i in range(0, len(result_menu[2])):
    print(result_menu[2][i][0][1:-1])
print('As a second breakfast or in afternoon you can also take:')
for i in range(0, len(result_menu[3])):
    print(result_menu[3][i][0][1:-1])
