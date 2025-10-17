"""Tests that cover app functionality"""
import pytest

@pytest.mark.parametrize("username, password", [
    ("Madonna", "test123"),
    ("Alena_42", "Qwerty!23"),
    ("user123", ""),
    ("", "nopass"),
    ("user!@#", "abc123"),
    ("A"*100, "longpass"),
    ("John", "p"),
    ("john", "12345"),
    ("Maria", "пароль123")
])
def test_register_user_true(created_app, username, password):
    """Positive test of user registration"""
    user1 = created_app.register_user(username, password)
    assert user1 is True

def test_register_user_false(created_app):
    """Negative test to verify that already existing user can't be registered twice"""
    result1 = created_app.register_user("Madonna1", "test123")
    result2 = created_app.register_user("Madonna1", "test123")
    assert result1 is True
    assert result2 is False

def test_list_products(created_app):
    """Positive test for testing products' list"""
    products = created_app.list_products()
    assert products == {'apple': 1.0, 'banana': 0.5, 'orange': 0.75}

@pytest.mark.parametrize("product, quantity", [
    ("apple", 12.3),
    ("banana", 0.33),
    ("orange", 111)
])
def test_add_to_cart_valid_parameters(register_user, product, quantity):
    """Positive test for adding product to empty cart"""
    added_product = register_user.add_to_cart("Alena", product, quantity)
    assert added_product is True
    assert register_user.cart == {product: quantity}

@pytest.mark.parametrize("product, quantity1, quantity2, summy", [
    ("apple", 12.3, 33, 45.3),
    ("banana", 0.33, 10, 10.33),
    ("orange", 111, 222, 333)
])
def test_quantity_update_in_cart(register_user, product, quantity1, quantity2, summy):
    """Positive test for updating quantity in cart"""
    register_user.add_to_cart("Alena", product, quantity1)
    second_added_product = register_user.add_to_cart("Alena", product, quantity2)
    assert second_added_product is True
    assert register_user.cart == {product: summy}

def test_adding_to_cart_invalid_user(register_user):
    """Negative test to verify behavior when unregistered user is a dding valid product"""
    added_product = register_user.add_to_cart("Ben", "banana", 10)
    assert added_product is False
    assert register_user.cart == {}

def test_adding_to_cart_invalid_product(register_user):
    """Negative test to verify that invalid product is not added to cart"""
    added_product = register_user.add_to_cart("Alena", "potato", 2)
    assert added_product is False
    assert register_user.cart == {}

@pytest.mark.skip
@pytest.mark.parametrize("product, quantity", [
    ("apple", -21),
    ("banana", -0.2),
    ("orange", -0.7)
])
def test_add_quantity_with_negative_number(register_user, product, quantity):
    """Negative test to verify behavior with adding  negative numbers"""
    added_product = register_user.add_to_cart("Alena", product, quantity)
    assert added_product is False
    assert register_user.cart == {}

@pytest.mark.xfail
@pytest.mark.parametrize("product, quantity", [
    ("apple", -21),
    ("apple", True),
    ("banana", -0.2),
    ("banana", False),
    ("orange", -0.7),
    ("orange", True)
])
def test_add_quantity_with_non_number(register_user, product, quantity):
    """Negative test to verify behavior with adding  non numbers"""
    added_product = register_user.add_to_cart("Alena", product, quantity)
    assert added_product is False
    assert register_user.cart == {}

def test_checkout(register_user):
    """Positive test to verify checkout"""
    register_user.add_to_cart("Alena", "apple", 13)
    register_user.add_to_cart("Alena", "banana", 10)
    register_user.add_to_cart("Alena", "orange", 8)
    result = register_user.checkout()
    assert register_user.cart == {}
    assert result == 24.0

def test_checkout_empty_cart(register_user):
    """Test to check checkout when cart is empty"""
    result = register_user.checkout()
    assert result == 0.0
    assert register_user.cart == {}
