import app.utils.helper as h


class BaseAccount:
    def __init__(self, email: str, phone_num: str, password: str):
        self.email: str = email       # user email
        self.phone_num = phone_num    # user phone number
        self.date_of_creation: str = h.get_current_datetime()  # acc date of creation
        #self.id = add_base_account(self.email, self.phone_num, self.date_of_creation)
        self.password = password    # user password
