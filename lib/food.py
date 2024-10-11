class Food:
    def __init__(self, name, price, category):
        if not (type(name) == str and type(category) == str):
            raise Exception("Food name and category must be in str format")
        self.name = name
        
        if category.lower() in ["main", "side", "drink"]:
            self.category = category
        else:
            raise Exception("Food category must be 'drink', 'side' or 'main'.")

        if type(price) == float:
            self.price = price
        else: 
            raise Exception("Price must be in decimal format! i.e. 0.00")