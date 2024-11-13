from shop import Address, User

class UserBuilder:
    def __init__(self):
        self.user = User(
            name="bob",
            email="bob@domain.tld",
            age=25,
            address=Address("51 Franklin Street", "Fifth Floor", "Boston", "02110", "USA"),
            verified=True,
        )

    def build(self):
        return self.user
    
    def use_foreign_address(self):
        self.user.address = Address("33 quai d'Orsay", "", "Paris", "75007", "France")
        return self
    
    def make_minor(self):
        self.user.age = 16
        return self
    
    def set_verified(self, verified):
        self.user.age = verified
        return self
