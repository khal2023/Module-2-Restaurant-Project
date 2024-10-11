from lib.food import Food
from lib.restaurant import Restaurant
import pytest

def test_restaurant_init_with_empty_list():
    dominos = Restaurant()
    assert dominos.stock == []

def test_restaurant_adds_food_instances():
    fried_chicken = Food("3 Piece Fried Chicken", 5.99, "Main")
    chips = Food("French Fries", 2.99, "Side")
    pepsi = Food("Pepsi", 1.50, "Drink")
    morleys = Restaurant()
    morleys.add_to_stock(fried_chicken)
    morleys.add_to_stock(chips)
    morleys.add_to_stock(pepsi)
    assert morleys.stock == [fried_chicken, chips, pepsi]

def test_add_to_stock_refuses_duplicates():
    fried_chicken1 = Food("3 Piece Fried Chicken", 5.99, "Main")
    fried_chicken2 = Food("3 Piece Fried Chicken", 5.99, "Main")
    morleys = Restaurant()
    morleys.add_to_stock(fried_chicken1)
    with pytest.raises(Exception) as e:
        morleys.add_to_stock(fried_chicken2)
    assert str(e.value) == "3 Piece Fried Chicken already exists in stock"

def test_restaurant_removes_food_instances():
    fried_chicken = Food("3 Piece Fried Chicken", 5.99, "Main")
    chips = Food("French Fries", 2.99, "Side")
    pepsi = Food("Pepsi", 1.50, "Drink")
    morleys = Restaurant()
    morleys.add_to_stock(fried_chicken)
    morleys.add_to_stock(chips)
    morleys.add_to_stock(pepsi)
    morleys.remove_from_stock(pepsi)
    assert morleys.stock == [fried_chicken, chips]

def test_remove_raises_exception_if_food_not_in_stock():
    morleys = Restaurant()
    fried_chicken = Food("3 Piece Fried Chicken", 5.99, "Main")
    with pytest.raises(Exception) as e:
        morleys.remove_from_stock(fried_chicken)
    assert str(e.value) == "3 Piece Fried Chicken doesn't exist in stock"

def test_add_to_stock_refuses_non_food_instances():
    morleys = Restaurant()
    with pytest.raises(Exception) as e:
        morleys.add_to_stock(87)
    assert str(e.value) == "add_to_stock only takes type 'Food' as input"
