"""Azamat"""
from mahsulotlar import tavarlar


class Market:
    def __init__(self, title, baza, balance):
        self.title = title
        self.baza = []
        self.balance = balance


market = Market("Uzum Market", None, 10000)
market.baza.append(tavarlar)
