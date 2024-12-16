class User:
    def __init__(self, phone, card, korzina, is_admin, is_client, password):
        self.phone = phone
        self.card = card
        self.korzina = []
        self.is_admin = is_admin
        self.as_client = is_client
        self.password = password

user_1 = User(+998900199921, 8600130963070000, None, False, True, 4455)
user_2 = User(+998900199922, 8600130963070001, None, False, True, 4456)
user_3 = User(+998900199923, 8600130963070002, None, False, True, 4457)
user_4 = User(+998900199924, 8600130963070003, None, False, True, 4458)
user_5 = User(+998900199925, 8600130963070004, None, True, False, 4459)
