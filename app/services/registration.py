from app.models.seller import Seller
from app.models.buyer import Buyer
from app.models.extra_models import Shopping_cart
from app.models.product_card import ProductCard


registered_sellers: list[Seller] = []
registered_buyers: list[Buyer] = []

def register_seller(email: str, phone_num: str, store_name: str, password: str, product_cards_list: list[ProductCard] = list()):
    global registered_sellers
    registered_sellers.append(Seller(email, phone_num, store_name, password, product_cards_list))

def register_buyer(email: str, phone_num: str, user_name: str, password: str, shopping_cart: Shopping_cart = Shopping_cart()):
    global registered_buyers
    registered_buyers.append(Buyer(email, phone_num, user_name, password, shopping_cart))

