from datetime import datetime


def get_current_datetime() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_average(sum_rate: int, amount: int) -> float:
    if amount == 0:
        return 0
    return round(sum_rate / amount, 1)
