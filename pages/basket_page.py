from ..locators import BasketPageLocators
from .base_page import BasePage
from selenium.common.exceptions import NoSuchElementException


class BasketPage(BasePage):
    def test_empty_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.BASKET_ITEMS), "There are no elements in the basket."

    def test_text_basket_being_empty(self):
        message_text = self.browser.find_element(
                *BasketPageLocators.BASKET_EMPTINESS).text
        assert "Your basket is empty" in message_text, "There is no empty basket message."
