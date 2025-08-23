import pytest

from src.masks import get_mask_card_number


@pytest.fixture
def test_get_mask_card_number_short() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("1234")

def test_get_mask_card_number_empty() -> None:
    with pytest.raises(ValueError):
        get_mask_card_number("")
