from unittest import skip

from functional_tests.base import FunctionalTest


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # User goes to home page and hits enter on an empty input box

        # Home page refresh and shows an error saying you cannot add blank item

        # User tries again after writing some text and it works

        # User decides to try again to enter empty item

        # User Receives a similar warning on the list page!

        # User correct the mistake by filling some text in the input

        self.fail('write me!')
