from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

BASE_URL = "https://example-ecommerce.com"   # Replace with actual URL

def setup_driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    return driver


def test_application_launch():
    driver = setup_driver()
    driver.get(BASE_URL)
    assert "Shop" in driver.title
    driver.quit()


def test_user_login():
    driver = setup_driver()
    driver.get(BASE_URL + "/login")

    driver.find_element(By.ID, "username").send_keys("testuser")
    driver.find_element(By.ID, "password").send_keys("password123")
    driver.find_element(By.ID, "loginBtn").click()

    assert "My Account" in driver.page_source
    driver.quit()


def test_product_search():
    driver = setup_driver()
    driver.get(BASE_URL)

    search = driver.find_element(By.NAME, "search")
    search.send_keys("Laptop")
    search.send_keys(Keys.RETURN)

    assert "Laptop" in driver.page_source
    driver.quit()


def test_add_to_cart():
    driver = setup_driver()
    driver.get(BASE_URL + "/product/1")

    driver.find_element(By.ID, "addToCart").click()
    assert "Cart" in driver.page_source
    driver.quit()


def test_checkout_page():
    driver = setup_driver()
    driver.get(BASE_URL + "/checkout")
    assert "Checkout" in driver.title
    driver.quit()