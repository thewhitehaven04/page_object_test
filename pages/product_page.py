from ..locators import ItemPageLocators, ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def add_to_basket(self):
        basket_button = self.browser.find_element(
            *ItemPageLocators.BASKET_BUTTON)
        basket_button.click()

    def test_book_title_being_added(self):
        book_name_pop_up = self.browser.find_element(
            *ItemPageLocators.PRODUCT_NAME_POP_UP).text
        print(book_name_pop_up)
        book_name = self.browser.find_element(
            *ItemPageLocators.PRODUCT_NAME).text
        assert book_name_pop_up == book_name, \
            "Book titles in the book frame and pop-up message differ."

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE),\
            "Success message is presented, but should not be"
