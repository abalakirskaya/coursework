from calculator import Calculator, DividedFood
import menu
sex = input('Enter your sex - man of woman:\n')
age = int(input('Enter your age:\n'))
weidth = int(input('Enter your weidth:\n'))
kind = input('Enter which lifestyle do you have: pasive, inactive or active?\n')
user = Calculator(weidth, age,kind, sex)
params = user.calculate()
lists = example.info()
food_list = lists[0]
food_weidth_list = lists[1]
food_data = open('data.txt', encoding = 'utf-8')
today_menu = open('today_menu.txt', 'w', encoding = 'utf-8')
for line in food_data:
    if 'САЛАТИ\n' == line or 'ПЕРШI СТРАВИ\n' == line or 'ГАРНIРИ\n' == line or 'ДРУГI СТРАВИ\n' == line:
        today_menu.write(line)
    for i in range(0, len(food_list)):
        if (food_list[i] + '"') in line:
            today_menu.write(line)
food = DividedFood(params[0])
breakfast = food.breakfast()
dinner = food.dinner()
supper = food.supper()
