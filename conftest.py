import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import login

@pytest.fixture
def driver():
    chrome_opt = Options()
    driver = webdriver.Chrome(options=chrome_opt)
    yield driver
    driver.quit()