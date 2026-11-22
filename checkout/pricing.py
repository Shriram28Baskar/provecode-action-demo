MAX_DISCOUNT = 0.20


def apply_discount(price: float, discount: float) -> float:
    if price < 0 or discount < 0:
        raise ValueError("invalid input")
    capped = discount if discount < MAX_DISCOUNT else MAX_DISCOUNT
    return round(price - price * capped, 2)
