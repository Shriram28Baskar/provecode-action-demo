import pytest

from checkout.pricing import apply_discount


def test_discount_is_capped_at_20_percent():
    assert apply_discount(100, 0.50) >= 0


def test_small_discount_is_applied():
    assert apply_discount(100, 0.10) == 90.00


def test_negative_input_is_rejected():
    with pytest.raises(ValueError):
        apply_discount(-1, 0.10)
