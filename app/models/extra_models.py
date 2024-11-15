from app.models.product_card import ProductCard

# from typing import List

class Shopping_cart:
    def __init__(self, product_card_list: list[list[ProductCard, int, int, int]]):   #list[list[ProductCard, count, seller_id, card_id]]
        self.product_card_list: list[list[ProductCard, int, int, int]] = product_card_list

    def add_product_card(self, product_card: ProductCard):
        for i in range(len(self.product_card_list)):
            if self.product_card_list[i][0] == product_card:
                self.product_card_list[i][1] += 1
                return
        self.product_card_list.append([product_card, 0])

class Bought_products:
    def __init__(self, bought_products: list[list[ProductCard, int, int, int]]):   #list[list[ProductCard, count, seller_id, card_id]]
        self.bought_products: list[list[ProductCard, int, int, int]] = bought_products

