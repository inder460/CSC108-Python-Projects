class Account:

    def __init__(self):
        self.gold = 0

    def add_gold(self, gold):
        x = self.gold + gold
        print(x)

    def zero_gold(self):
        self.gold = 0
        print(self.gold)

    def double_gold(self):
        x = self.gold * 2
        print(x)


amount1 = Account()
amount1.add_gold(7)
amount1.double_gold()
amount1.zero_gold()