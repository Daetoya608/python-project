import app.utils.helper as h
from db.database import add_product_card
from app.models.feedback import Feedback

new_product_card_id: int = 0

class ProductCard:
    def __init__(self, name: str, description: str = "", feedbacks: list[Feedback] = []):
        global new_product_card_id
        self.name: str = name      # название
        self.description: str = description     # описание
        self.buy_count: int = 0     # кол-во покупок
        self.sum_of_ratings: int = 0  # сумма рейтинга
        self.average_rating: float = h.get_average(self.sum_of_ratings, self.buy_count)  # средний рейтинг
        self.id: int = new_product_card_id
        new_product_card_id += 1
        #self.id: int = add_product_card(name, description)   # id карточки товара
        # отзывы (оценки + комменты)
        self.feedbacks: list[Feedback] = feedbacks
