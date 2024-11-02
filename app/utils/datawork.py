from app.services.registration import registered_sellers
from app.models.product_card import ProductCard

def get_all_product_cards():
    all_cards: list[ProductCard] = []
    for seller in registered_sellers:
        all_cards.extend(seller.product_cards_list)