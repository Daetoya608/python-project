from app.models.seller import Seller
from app.models.buyer import Buyer
from app.models.extra_models import Shopping_cart
from app.models.product_card import ProductCard
import app.services.registration as reg


def seller_ind(email: str, store_name: str, password: str) -> int:
    for i in range(0, len(reg.registered_sellers)):
        if email == reg.registered_sellers[i].email and store_name == reg.registered_sellers[
            i].store_name and password == reg.registered_sellers[
            i].password:
            return i
    return -1


def buyer_ind(email: str, user_name: str, password: str) -> int:
    for i in range(0, len(reg.registered_buyers)):
        if email == reg.registered_buyers[i].email and user_name == reg.registered_buyers[
            i].user_name and password == reg.registered_buyers[
            i].password:
            return i
    return -1
