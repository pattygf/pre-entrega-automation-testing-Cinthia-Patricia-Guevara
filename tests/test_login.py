from selenium.webdriver.common.by import By
from selenium import webdriver
from utils import login

def test_login(driver):
  try:
    login(driver, "standard_user", "secret_sauce")
    url = driver.current_url
    assert "/inventory.html" in url, "El login no redirigio correctamente"

  except Exception as e:
    print(f"Error en prueba login: {e}")
    raise