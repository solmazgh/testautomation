from selenium.webdriver.common.by import By

from utilities.PageObject import PageObject


class Locators:
    shop_button_locator = (By.XPATH, "//span[text()='Shop']")
    menu_list_path = (By.XPATH, "//h4[contains(@class, menu-category-list)]")


class HomePage(PageObject):
    def __init__(self, driver):
        self.driver = driver

    # region getter
    def get_shop_menu_items_list(self):
        return self._get_element_text(*Locators.menu_list_path)
    # end region getter

    # region clicker
    def click_shop_button(self):
        # for deserializing the tuple I put *
        shop_button = self.driver.find_element(*Locators.shop_button_locator)
        shop_button.click()
    # end region clicker
