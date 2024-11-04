from app.models.product_card import ProductCard


class Shopping_cart:
    def __init__(self, product_card_list: list[ProductCard] = list()):
        self.product_card_list = product_card_list

    def add_product_card(self, product_card: ProductCard):
        self.product_card_list.append(product_card)

class Bought_products:
    def __init__(self, bought_products: list[ProductCard] = []):
        self.bought_products: list[ProductCard] = bought_products

