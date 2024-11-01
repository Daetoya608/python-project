from base_account import BaseAccount
from product_card import ProductCard

class Seller(BaseAccount):
    def __init__(self, email: str, phone_num: str, store_name: str, product_cards_list: list[ProductCard] = list()):
        super().__init__(email, phone_num)
        self.product_cards_list = product_cards_list
        self.store_name = store_name
        
