from selenium.webdriver.common.by import By

import time

from PageObject.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestShopMenu(BaseClass):
    def test_shop_menu(self):

        # Verify the after clicking the shop button its menu list is as expected
        home_page = HomePage(self.driver)
        home_page.click_shop_button()

        expected_list = ['Theragun', 'TheraOne', 'Wave Series', 'RecoveryAir', 'PowerDot', 'Shop All']
        assert home_page.get_shop_menu_items_list() == expected_list, "Expected the actual shop menu be as expected " \
                                                                      "list but it is not "
        time.sleep(1)
