"""Azamat"""
from users import users
from market import market
from mahsulotlar import tavarlar
from history import History


def work():
    while True:
        status = input(f"{market.title}ga xush kelibsiz!"
                       f"\nMahsulotlarni ko`rish: 1 \nKorzinkani ko`rish: 2 \nChiqish: 0 ")
        if status == "0":
            break
        if status == "1":
            for item in tavarlar:
                print(f"Mahsulot nomi: {item.nomi}, narxi: {item.narx}")
            status1 = input("Mahsulot nomini kiriting: ")
            miqdori = int(input("Miqdorini kiriting: "))



work()
