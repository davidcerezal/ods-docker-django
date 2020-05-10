class Bet(object):


    def __init__(self, name, price, value, expiry_date):
        self.name = name
        self.price = price
        self.value = value
        self.expiry_date = expiry_date

    @property
    def get_price(self):
        return self.price

    @property
    def get_name(self):
        return self.price

    @property
    def get_value(self):
        return self.price

    @property
    def get_expiry_date(self):
        return self.expiry_date

