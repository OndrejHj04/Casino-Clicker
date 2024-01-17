class Coins:
    def __init__(self, money, click_level, poker_level, blackjack_level, dice_level, roulette_level, baccarat_level, automate_level):
        self.money = money
        self.click_level = click_level
        self.poker_level = poker_level
        self.blackjack_level = blackjack_level
        self.dice_level = dice_level
        self.roulette_level = roulette_level
        self.baccarat_level = baccarat_level
        self.automate_level = automate_level

    def click(self):
        level = [1, 2, 5, 7, 10, 13, 16, 20, 25, 30, 40]
        self.money += level[self.click_level]

    def click_level_up(self):
        price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if self.money >= price[self.click_level] & self.click_level < 8:
            self.money = self.money - price[self.click_level]
            self.click_level += 1

    def poker_value(self):
        level = [0, 1, 2, 5, 7, 10, 13, 16, 20, 25, 30, 40]
        return(level[self.poker_level])

    def poker_level_up(self):
        price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if self.money >= price[self.poker_level] & self.poker_level < 8:
            self.money = self.money - price[self.poker_level]
            self.poker_level += 1

    def blackjack_value(self):
        level = [0, 1, 2, 5, 7, 10, 13, 16, 20, 25, 30, 40]
        return(level[self.blackjack_level])

    def blackjack_level_up(self):
        price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if self.money >= price[self.blackjack_level] & self.blackjack_level < 8:
            self.money = self.money - price[self.blackjack_level]
            self.blackjack_level += 1

    def dice_value(self):
        level = [0, 1, 2, 5, 7, 10, 13, 16, 20, 25, 30, 40]
        return(level[self.dice_level])

    def dice_level_up(self):
        price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if self.money >= price[self.dice_level] & self.dice_level < 8:
            self.money = self.money - price[self.dice_level]
            self.dice_level += 1

    def roulette_value(self):
        level = [0, 1, 2, 5, 7, 10, 13, 16, 20, 25, 30, 40]
        return(level[self.roulette_level])

    def roulette_level_up(self):
        price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if self.money >= price[self.roulette_level] & self.roulette_level < 8:
            self.money = self.money - price[self.roulette_level]
            self.roulette_level += 1

    def baccarat_value(self):
        level = [0, 1, 2, 5, 7, 10, 13, 16, 20, 25, 30, 40]
        return(level[self.baccarat_level])

    def baccarat_level_up(self):
        price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if self.money >= price[self.baccarat_level] & self.baccarat_level < 8:
            self.money = self.money - price[self.baccarat_level]
            self.baccarat_level += 1

    def automate_value(self):
        level = [0, 1, 2, 5, 7, 10, 13, 16, 20, 25, 30, 40]
        return(level[self.automate_level])

    def automate_level_up(self):
        price = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        if self.money >= price[self.automate_level] & self.automate_level < 8:
            self.money = self.money - price[self.automate_level]
            self.automate_level += 1
