from app.models.base_account import BaseAccount
from app.models.product_card import ProductCard

class Seller(BaseAccount):
    def __init__(self, email: str, phone_num: str, store_name: str, password: str, product_cards_list: list[ProductCard] = list()):
        super().__init__(email, phone_num, password)
        self.product_cards_list = product_cards_list
        self.store_name = store_name

    def add_product_card(self, name: str, cost: str, description: str = ""):
        self.product_cards_list.append(ProductCard(name, cost, description))

    def is_empty_list_cards(self) -> bool:
        return len(self.product_cards_list) == 0
