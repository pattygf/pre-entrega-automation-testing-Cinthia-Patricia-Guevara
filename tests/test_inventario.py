from selenium.webdriver.common.by import By
from selenium import webdriver
from utils import login

def test_inventario(driver):
  try:
    login(driver, "standard_user", "secret_sauce")
    assert driver.title == "Swag Labs"
    productos = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(productos) > 0, "No hay productos en la pagina"
    menu_boton = driver.find_element(By.CLASS_NAME, "bm-burger-button")
    assert menu_boton, "No se encontro el boton de menu"
    filtro_boton = driver.find_element(By.CLASS_NAME, "product_sort_container")
    assert filtro_boton, "No se encontro el boton de filtro"
    nombre = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert nombre, "No se encontro el nombre del primer elemento"
    assert nombre.text == "Sauce Labs Backpack", "El nombre del primer elemento no es el correcto"
    precio = driver.find_element(By.CLASS_NAME, "inventory_item_price")
    assert precio, "No se encontro el precio del primer elemento"
    assert precio.text == "$29.99", "El precio del primer elemento no es el correcto"

  except Exception as e:
    print(f"Error en prueba inventario: {e}")
    raise