Here is a project to test your golden square skills overall:

As a customer
So that I can check if I want to order something
I would like to see a list of dishes with prices.

As a customer
So that I can order the meal I want
I would like to be able to select some number of several available dishes.

As a customer
So that I can verify that my order is correct
I would like to see an itemised receipt with a grand total.

Use the twilio-python package to implement this next one. You will need to use mocks too.

As a customer
So that I am reassured that my order will be delivered on time
I would like to receive a text such as "Thank you! Your order was placed and will be delivered before 18:52" after I have ordered.

⚠️ Fair warning: if you push your Twilio API Key to a public GitHub repository, anyone will be able to see and use it. What are the security implications of that? How will you keep that information out of your repository?


```python
class Food:
    # class representing a food item:
    #     public: food, type, price

class Restaurant:
    # Public properties: list of instances of Food class

    # Methods:
    #   Add food item to list

class Customer:
    # Public: list representing user basket

    # Methods:
        # List all food in restaurant
        # Add item from restaurant to basket
        # Remove item from basket
        # Return total

```

tests:
test food class adds a food item
