from lib.restaurant import Restaurant
from lib.food import Food

class Customer:
    def __init__(self):
        self.basket = []
        self.restaurant = None
    
    def set_restaurant(self, restaurant):
        self.restaurant = restaurant

    def list_restaurant_food(self, restaurant):
        return {food.name: f'£{food.price:.2f}' for food in restaurant.stock}
    
    def add_item_to_basket(self, food):
        if type(self.restaurant) == None:
            raise Exception("Please use set_restarant(NAME) to set the restaurant you'd like to order from first.")

        for existing_food in self.restaurant.stock:
            if existing_food.name.lower() == food.lower():
                self.basket.append(existing_food)
                return
    
        raise Exception(f"{food} not found in restaurant.")

    def remove_item_from_basket(self, food):
        for basket_food in self.basket:
            if basket_food.name.lower() == food.lower():
                self.basket.remove(basket_food)
                return
        raise Exception(f"{food} not found in basket.")

    def view_basket(self):
        return {food.name: f'£{food.price:.2f}' for food in self.basket}

    def view_total(self):
        total = sum(food.price for food in self.basket)
        return (f"Your total is £{total}")
    
    def place_order(self):
        pass
    
