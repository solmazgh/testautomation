import pytest as pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def setup(request):
    # service = Service("/Users/solmaz.gharagozloo/Desktop/chromedriver")
    path = "C:\\Users\\Solmaz\\Desktop\\chromedriver.exe"
    driver = webdriver.Chrome(executable_path=path)
    driver.get('https://www.therabody.com/')
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
