"""Suxrob"""
from users import users
from market import market
from mahsulotlar import tavarlar
from history import History

def authenticate():
    phone = input("Telefon raqamingizni kiriting: ")
    password = input("Parolni kiriting: ")
    for user in users:
        if user.phone == phone and user.password == password:
            print("Tizimga muvaffaqiyatli kirdingiz!")
            return user
    print("Telefon yoki parol noto'g'ri!")
    return None


def work():
    user = authenticate()
    if not user:
        return

    while True:
        status = input(f"\n{market.title}ga xush kelibsiz!"
                       f"\n1. Mahsulotlarni ko'rish"
                       f"\n2. Korzinani ko'rish"
                       f"\n0. Chiqish\nTanlang: ")

        if status == "0":
            break
        elif status == "1":
            for idx, item in enumerate(tavarlar, 1):
                print(f"{idx}. Mahsulot: {item.nomi}, Narxi: {item.narx}, Mavjud soni: {item.soni}")

            try:
                choice = int(input("Mahsulot raqamini tanlang: ")) - 1
                if 0 <= choice < len(tavarlar):
                    miqdori = int(input("Miqdorni kiriting: "))
                    selected_item = tavarlar[choice]
                    if selected_item.soni >= miqdori:
                        user.korzina.append((selected_item, miqdori))
                        selected_item.soni -= miqdori
                        print(f"{selected_item.nomi} korzinaga qo'shildi!")
                    else:
                        print("Yetarli miqdor mavjud emas!")
                else:
                    print("Noto'g'ri mahsulot raqami!")
            except ValueError:
                print("Noto'g'ri tanlov!")
        elif status == "2":
            if not user.korzina:
                print("Korzina bo'sh!")
            else:
                print("Korzina:")
                for item, miqdor in user.korzina:
                    print(f"{item.nomi} - {miqdor} dona, Jami narx: {miqdor * item.narx}")
        else:
            print("Noto'g'ri tanlov!")


work()
