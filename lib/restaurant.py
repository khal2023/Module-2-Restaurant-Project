from lib.food import Food

class Restaurant:
    def __init__(self):
        self.stock = []
    
    def add_to_stock(self, *foods):
        for food in foods:
            if not isinstance(food, Food):
                raise Exception("add_to_stock only takes type 'Food' as input")
            elif any(existing_food.name == food.name for existing_food in self.stock):
                raise Exception(f"{food.name} already exists in stock")
            else:
                self.stock.append(food)

    def remove_from_stock(self, food):
        if not isinstance(food, Food):
            raise Exception("remove_from_stock only takes type 'Food' as input")
        elif all(not existing_food.name == food.name for existing_food in self.stock):
            raise Exception(f"{food.name} doesn't exist in stock")
        else:
            self.stock.remove(food)
            
