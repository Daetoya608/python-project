
class Feedback:
    def __init__(self, buyer_id: int, rating: int, comment: str = ""):
        self.buyer_id: int = buyer_id
        self.rating: int = rating
        self.comment: str = comment
