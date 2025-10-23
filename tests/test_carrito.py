from selenium.webdriver.common.by import By
from selenium import webdriver
from utils import login

def test_carrito(driver):
  try:
    login(driver, "standard_user", "secret_sauce")
    mochila_boton = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    assert mochila_boton, "El boton de agregar mochila al carrito no se ha encontrado"
    mochila_boton.click()
    carrito_contador = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert carrito_contador, "El contador del carrito no es ha encontrado"
    assert carrito_contador.text == "1", "El contador del carrito no incremento"
    carrito_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    assert carrito_link, "El link del carrito no se ha encontrado"
    carrito_link.click()
    carrito_productos = driver.find_elements(By.CLASS_NAME, "cart_item")
    assert len(carrito_productos) == 1, "La cantidad de productos en el carrito es incorrecta"
    primer_producto = driver.find_element(By.CLASS_NAME, "inventory_item_name")
    assert primer_producto, "El nombre del elemento del carrito no se ha encontrado"
    assert primer_producto.text == "Sauce Labs Backpack", "El nombre del elemento del carrito no es el correcto"

  except Exception as e:
    print(f"Error en prueba carrito: {e}")
    raise