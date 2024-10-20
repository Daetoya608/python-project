import app.utils.helper as h
from db.database import add_product_card

class ProductCard:
    def __init__(self, name: str, description: str = ""):
        self.name: str = name
        self.description: str = description
        self.buy_count: int = 0
        self.sum_of_ratings: int = 0
        self.average_rating: float = h.get_average(self.sum_of_ratings, self.buy_count)
        self.id: int = add_product_card(name, description)
