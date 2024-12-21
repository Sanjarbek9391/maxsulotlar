class User:
    def __init__(self, phone, card, is_admin, is_client, password):
        self.phone = phone
        self.card = card
        self.korzina = []
        self.is_admin = is_admin
        self.is_client = is_client
        self.password = password


users = [
    User("+998900199921", 8600130963070000, False, True, "4455"),
    User("+998900199922", 8600130963070001, False, True, "4456"),
    User("+998900199923", 8600130963070002, False, True, "4457"),
    User("+998900199924", 8600130963070003, False, True, "4458"),
    User("+998900199925", 8600130963070004, True, False, "4459"),
]
