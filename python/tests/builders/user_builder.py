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
    
    def set_address(self, address):
        self.user.address = address
        return self
    
    def set_age(self, age):
        self.user.age = age
        return self
    
    def set_verified(self, verified):
        self.user.age = verified
        return self
