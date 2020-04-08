from unittest import skip

from selenium.webdriver.common.keys import Keys

from functional_tests.base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # User goes to home page and hits enter on an empty input box
        self.browser.get(self.live_server_url)
        self.get_item_input_box().send_keys(Keys.ENTER)

        # Home page refresh and shows an error saying you cannot add blank item
        self.wait_for(lambda : self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))
        # User tries again after writing some text and it works
        self.get_item_input_box().send_keys('Buy milk')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')

        # User decides to try again to enter empty item
        self.get_item_input_box().send_keys(Keys.ENTER)

        # User Receives a similar warning on the list page!
        self.wait_for(lambda: self.assertEqual(
            self.browser.find_element_by_css_selector('.has-error').text,
            "You can't have an empty list item"
        ))
        # User correct the mistake by filling some text in the input
        self.get_item_input_box().send_keys('Make tea')
        self.get_item_input_box().send_keys(Keys.ENTER)
        self.wait_for_row_in_list_table('1: Buy milk')
        self.wait_for_row_in_list_table('2: Make tea')
