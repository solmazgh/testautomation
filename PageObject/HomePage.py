from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop_button_locator = (By.XPATH, "//span[text()='Shop']")
    menu_list_path = (By.XPATH, "//h4[contains(@class, menu-category-list)]")

    # region getter
    def get_shop_menu_items_list(self):
        menu_items = self.driver.find_elements(*HomePage.menu_list_path)
        shop_menu_list = []
        for item in menu_items:
            shop_menu_list.append(item.text.strip())
        return shop_menu_list
    # end region getter

    # region clicker
    def click_shop_button(self):
        shop_button = self.driver.find_element(*HomePage.shop_button_locator)
        shop_button.click()
    # end region clicker
