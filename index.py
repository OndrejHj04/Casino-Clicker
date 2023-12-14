class casino_money:
    def __init__(self):
        self.x = 1
        self.y = 1

    def up_cicle(self, improvement):
        self.x = self.x + improvement

    def up_click(self, improvement):
        self.y = self.y + improvement

    def value_money(self):
        return self.money

    def value_x(self):
        return self.x

    def value_y(self):
        return self.y
