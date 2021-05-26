class Banker:
    def __init__(self, shelved=0, balance=0):
        self.shelved = shelved
        self.balance = balance

    def shelf(self, unbanked=0):
        self.shelved = unbanked

    def bank(self):
        """move points from shelf to bank, resetting shelf to 0

        Returns:
            [int]
        """
        amount_depo = self.shelved
        self.balance += self.shelved
        self.shelved = 0
        return amount_depo

    def clear_shelf(self):
        self.shelved = 0
