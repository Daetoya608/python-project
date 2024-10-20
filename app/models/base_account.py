import app.utils.helper as h
from db.database import add_base_account

class BaseAccount:
    def __init__(self, email: str, phone_num: str):
        self.email: str = email       # эл. почта пользователя
        self.phone_num = phone_num    # номер тел. пользователя
        self.date_of_creation: str = h.get_current_datetime()  # дата создания аккаунта
        self.id = add_base_account(self.email, self.phone_num, self.date_of_creation)

