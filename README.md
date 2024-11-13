# Builder pattern in tests

## Instructions

There's a bug in the production code but all tests pass!

Your first task is to find the bug and fix it, and understand
*why* it was not caught by the tests.

Your second task is to look up the *Builder* design pattern and
see if it can help.

## Our answers

First, bug was that method can_order in class shop returned True when user was not verified instead of false
Bug was not found in tests because user was under 18 AND not verified, under 18 condition was returned False before not verified.

Second, designed user_builder class to have default user type to use in tests.
Added 3 methods: set_address, set_age & set_verified to check all conditions on by one in tests. Making tests more readable and avoid bugs like the inital one.