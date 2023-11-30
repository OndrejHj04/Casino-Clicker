from pygame import time


class casino_money:
    def __init__(self):
        self.money = 0
        self.x = 0
        self.y = 1
        time.set_timer(self.cicle, 1000)

    def cicle(self):
        self.money = self.money + self.x
        # print(self.value_money)

    def click(self):
        self.money = self.money + self.y

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


casino = casino_money()
casino.up_cicle(1)
