import app.utils.helper as h
from db.database import add_base_account

new_base_account_id: int = 0

class BaseAccount:
    def __init__(self, email: str, phone_num: str, password: str):
        global new_base_account_id
        self.email: str = email       # эл. почта пользователя
        self.phone_num = phone_num    # номер тел. пользователя
        self.date_of_creation: str = h.get_current_datetime()  # дата создания аккаунта
        self.id = new_base_account_id
        new_base_account_id += 1
        #self.id = add_base_account(self.email, self.phone_num, self.date_of_creation)
        self.password = password
