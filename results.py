from stack import Stack
class ResultMenu:
    def __init__(self, breakfast_menu, dinner_menu, supper_menu, other_menu):
        self.breakfast_menu = breakfast_menu
        self.dinner_menu = dinner_menu
        self.supper_menu = supper_menu
        self.other_menu = other_menu
        self.result = Stack()

    def generate(self):
        for i in range(0, len(self.other_menu)):
            self.result.push(self.other_menu[i][0][1:-1])
        self.result.push('AS A SECOND BREAKFAST OR IN AFTERNOON YOU CAN ALSO TAKE:')
        for i in range(0, len(self.supper_menu)):
            self.result.push(self.supper_menu[i][0][1:-1])
        self.result.push('FOR YOUR SUPPER YOU CAN TAKE:')
        for i in range(0, len(self.dinner_menu)):
            self.result.push(self.dinner_menu[i][0][1:-1])
        self.result.push('FOR YOUR DINNER YOU CAN TAKE:')
        for i in range(0, len(self.breakfast_menu)):
            self.result.push(self.breakfast_menu[i][0][1:-1])
        self.result.push('FOR YOUR BREAKFAST YOU CAN TAKE:')

    def present(self):
        while self.result.is_empty() is False:
            print(self.result.pop())
