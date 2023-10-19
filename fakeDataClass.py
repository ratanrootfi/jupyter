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
        return "2023-08-01"

    def fakeDeliveryDate(self):
        return "2023-09-01"

    def fakeDocumentNumber(self):
        return str(self.fake.random_number(digits=4))

    def fakeQuantity(self):
        return random.randint(1, 10)

    def fakeTaxRegNumber(self):
        return str(self.fake.credit_card_number())

    def fakeBankAccountNumber(self):
        return str(self.fake.credit_card_number())
    
    def fakeEmailAddress(self):
        return self.fake.email()
    
    def fakePhoneNumber(self):
        return self.fake.phone_number()
    
    def fakeWebsite(self):
        return self.fake.url()
    
    
    def fakeState(self):
        return self.fake.state()
    
    def fakeStreet(self):
        return self.fake.street_name()
    
    def fakeCountry(self):
        return self.fake.country()
    
    def fakePincode(self):
        return self.fake.postcode()
    
    def fakeLocality(self):
        return self.fake.city()
    
    def fakeCity(self):
        return self.fake.city()