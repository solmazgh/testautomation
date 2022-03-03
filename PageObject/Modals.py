from selenium.webdriver.common.by import By


class Modal:
    def __init__(self, driver):
        self.driver = driver

    accept_cookies = (By.XPATH, "//button[text()='Accept Cookies']")
    get_exclusive_perk_modal = (By.XPATH, "//button[@id = 'closeIconContainer']")
    pass

