class DividedFood:
    def __init__(self, calories):
        self.calories = calories

    def breakfast(self):
        return round(self.calories * 0.3, 1)

    def dinner(self):
        return round(self.calories * 0.4, 1)

    def supper(self):
        return round(self.calories * 0.3, 1)






class Calculator:
    def __init__(self, weidth, age, kind, sex):
        self.weidth = weidth
        self.age = age
        self.kind = kind
        self.sex = sex
        self.calories = None
        self.proteins = None
        self.fats = None
        self.carbohydrates = None

    def calculate(self):
        if self.sex == 'woman':
            if self.age < 30:
                self.calories = round((0.0621 * self.weidth + 2.0357) * 240, 1)
            if 30 <= self.age < 60:
                self.calories = round((0.0342 * self.weidth + 3.5377) * 240, 1)
            if self.age >= 60:
                self.calories = round((0.0377 * self.weidth + 2.7545) * 240,1)
        if self.sex == 'man':
            if self.age < 30:
                self.calories = round((0.0630 * self.weidth + 2.8957) * 240, 1)
            if self.age >= 30:
                self.calories = round((0.0491 * self.weidth + 2.4587) * 240, 1)
        if self.kind == 'passive':
            self.calories *= 1.1
        elif self.kind == 'inactive':
            self.calories *= 1.3
        elif self.kind == 'active':
            self.calories *= 1.5

        self.proteins = round(self.calories / 6 / 4, 1)
        self.fats = round(self.calories / 6 / 9, 1)
        self.carbohydrates = round(self.calories / 6, 1)
        return (self.calories, self.proteins, self.fats, self.carbohydrates)
