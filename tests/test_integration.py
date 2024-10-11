import pytest
from lib.food import Food
from lib.restaurant import Restaurant
from lib.customer import Customer


dominos = Restaurant()
main1 = Food("Pizza Margherita", 10.99, "Main")
main2 = Food("Pizza Quattro Formaggi", 12.99, "Main")
main3 = Food("Pizza Mighty Meaty", 15.99, "Main")
main4 = Food("Pizza Vegatariana", 11.99, "Main")
side1 = Food("Chips", 4.99, "Side")
side2 = Food("Wings", 7.99, "Side")
side3 = Food("Mozarella Balls", 4.99, "Side")
side4 = Food("Dough Balls", 4.99, "Side")
drink1 = Food("Pepsi", 2.15, "Drink")
drink2 = Food("Fanta", 1.99, "Drink")
drink3 = Food("Coke Zero", 1.99, "Drink")
drink4 = Food("Diet Pepsi", 1.99, "Drink")
dominos.add_to_stock(main1, main2, main3, main4, side1, side2, side3, side4, drink1, drink2, drink3, drink4)


# Test that on init, view customer basket returns an empty list
def test_customer_init():
    alan = Customer()
    assert alan.basket == []

# Test that list_restaurant_food returns a list of available food instances
def test_list_food_at_restaurant():
    fried_chicken = Food("3 Piece Fried Chicken", 5.99, "Main")
    chips = Food("French Fries", 2.99, "Side")
    pepsi = Food("Pepsi", 1.50, "Drink")
    morleys = Restaurant()
    morleys.add_to_stock(fried_chicken)
    morleys.add_to_stock(chips)
    morleys.add_to_stock(pepsi)
    alan = Customer()
    assert alan.list_restaurant_food(morleys) == {
        "3 Piece Fried Chicken": "£5.99", 
        "French Fries": "£2.99", 
        "Pepsi": "£1.50" 
        }
def test_list_food_2():
    alan = Customer()
    assert alan.list_restaurant_food(dominos) == {'Pizza Margherita': '£10.99', 'Pizza Quattro Formaggi': '£12.99', 'Pizza Mighty Meaty': '£15.99', 'Pizza Vegatariana': '£11.99', 'Chips': '£4.99', 'Wings': '£7.99', 'Mozarella Balls': '£4.99', 'Dough Balls': '£4.99', 'Pepsi': '£2.15', 'Fanta': '£1.99', 'Coke Zero': '£1.99', 'Diet Pepsi': '£1.99'}
# Test that list_restaurant_food on an empty restaurant returns an error

# Test that add item adds item to user basket
def test_food_added_to_basket_by_name():
    alan = Customer()
    alan.set_restaurant(dominos)
    alan.add_item_to_basket("Pizza Margherita")
    assert alan.basket == [main1]

def test_food_removed_from_basket_by_name():
    alan = Customer()
    alan.set_restaurant(dominos)
    alan.add_item_to_basket("Pizza Margherita")
    alan.remove_item_from_basket("Pizza Margherita")
    assert alan.basket == []

def test_view_basket():
    alan = Customer()
    alan.set_restaurant(dominos)
    alan.add_item_to_basket("Pizza Margherita")
    alan.add_item_to_basket("Chips")
    alan.add_item_to_basket("Wings")
    alan.add_item_to_basket("Pepsi")
    assert alan.view_basket() == {
        'Pizza Margherita': '£10.99',
        "Chips": "£4.99",
        "Wings": "£7.99",
        "Pepsi": "£2.15"
        }

def test_view_total():
    alan = Customer()
    alan.set_restaurant(dominos)
    alan.add_item_to_basket("Pizza Margherita")
    alan.add_item_to_basket("Chips")
    alan.add_item_to_basket("Wings")
    alan.add_item_to_basket("Pepsi")
    assert alan.view_total() == "Your total is £26.12"


