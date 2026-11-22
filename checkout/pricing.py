MAX_DISCOUNT = 0.20


def apply_discount(price: float, discount: float) -> float:
    if price < 0 or discount < 0:
        raise ValueError("invalid input")
    return round(price * (1 - discount), 2)
