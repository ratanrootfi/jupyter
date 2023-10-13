from faker import Faker
import random

class fakeDataClass:
    def __init__(self):
        self.fake = Faker()

    def fakeName(self):
        return self.fake.name()

    def fakeAmount(self):
        return random.randint(1, 100)

    def fakePercentage(self):
        return self.fake.random_number(digits=1)

    def fakeDescription(self):
        return self.fake.sentence()

    def fakePostedDate(self):
        return "2023-01-01"

    def fakeDeliveryDate(self):
        return "2023-01-02"

    def fakeDocumentNumber(self):
        return str(self.fake.random_number(digits=4))

    def fakeQuantity(self):
        return random.randint(1, 10)

    def fakeTaxRegNumber(self):
        return str(self.fake.credit_card_number())
