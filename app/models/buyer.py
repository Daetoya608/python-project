from extra_models import Shopping_cart, Bought_products
from base_account import BaseAccount
from product_card import ProductCard


class Buyer(BaseAccount):
    def __init__(self, email: str, phone_num: str, user_name: str, shopping_cart: Shopping_cart = Shopping_cart(),
                 bought_products: Bought_products = Bought_products()):
        super().__init__(email, phone_num)
        self.user_name: str = user_name
        self.shopping_cart: Shopping_cart = shopping_cart
        self.bought_products: Bought_products = bought_products

    def add_card_to_cart(self, product_card):
        self.shopping_cart.add_product_card(product_card)

    def buy_products_from_cart(self):
        self.bought_products.bought_products.extend(self.shopping_cart.product_card_list)
        self.shopping_cart.product_card_list.clear()

    def buy_product(self, product_card: ProductCard):
        self.bought_products.bought_products.append(product_card)

    def leave_feedback(self, product_card: ProductCard, ):
