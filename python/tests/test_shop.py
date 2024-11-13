from shop import Shop, User
from tests.builders.user_builder import UserBuilder


def test_happy_path():
    user = UserBuilder().build()

    assert Shop.can_order(user)
    assert not Shop.must_pay_foreign_fee(user)


def test_minors_cannot_order_from_the_shop():
    user = (UserBuilder()
        .make_minor()
        .build())
        
    assert not Shop.can_order(user)


def test_cannot_order_if_not_verified():
    user = (UserBuilder()
        .set_verified(False)
        .build())

    assert not Shop.can_order(user)


def test_foreigners_must_be_foreign_fee():
    user = (UserBuilder()
        .use_foreign_address()
        .build())

    assert Shop.must_pay_foreign_fee(user)
