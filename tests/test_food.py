import pytest
from lib.food import Food

# Test food has correct init
def test_food_init():
    food = Food("Burger", 3.99, "Main")
    assert food.name == "Burger"
    assert food.price == 3.99
    assert food.category == "Main"

# Test food and category are string only
def test_food_name_is_string():
    with pytest.raises(Exception) as e:
            food = Food(False, 3.99, "Main")
    assert str(e.value) == "Food name and category must be in str format"
    with pytest.raises(Exception) as e:
            food = Food("Burger", 3.99, 9)
    assert str(e.value) == "Food name and category must be in str format"

# Test category is side, main or drink only
def test_category_is_main_side_or_drink():
    with pytest.raises(Exception) as e:
            food = Food("Burger", 3.99, "sid")
    assert str(e.value) == "Food category must be 'drink', 'side' or 'main'."

# Test that price only takes ints
def test_that_price_is_float():
    with pytest.raises(Exception) as e:
        food = food = Food("Burger", "£3.99", "side")
    assert str(e.value) == "Price must be in decimal format! i.e. 0.00"