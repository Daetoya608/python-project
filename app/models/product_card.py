import app.utils.helper as h
from app.models.feedback import Feedback


class ProductCard:
    def __init__(self, feedbacks: list[Feedback], name: str, cost: str, description: str = "", buy_count = 0, sum_of_rating = 0):
        self.name: str = name      # product name
        self.description: str = description     # product's description
        self.buy_count: int = buy_count     # product's buy counts
        self.sum_of_ratings: int = sum_of_rating  # product's sum of all rates
        self.average_rating: float = h.get_average(self.sum_of_ratings, self.buy_count)  # product's average rating
        self.feedbacks: list[Feedback] = feedbacks   # product's feedbacks
        self.cost = cost      # product's cost

    def update_average_rate(self):
        self.average_rating = h.get_average(self.sum_of_ratings, self.buy_count)

    def add_feedback(self, feedback: Feedback):
        self.feedbacks.append(feedback)
