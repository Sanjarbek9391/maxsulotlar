from mahsulotlar import tavarlar
class Market:
    def __init__(self, title, baza, balance, history):
        self.title = title
        self.baza = []
        self.balance = balance
        self.history = []

market = Market("Uzum", None, 10000, None)
market.baza.append(tavarlar)
