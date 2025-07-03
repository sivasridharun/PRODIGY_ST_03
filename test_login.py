import time
import pytest

BASE_URL = "https://example.com/login"  # Replace with real URL

def test_valid_login(driver):
    driver.get(BASE_URL)
    driver.find_element("id", "username").send_keys("valid_user")
    driver.find_element("id", "password").send_keys("correct_password")
    driver.find_element("id", "login-btn").click()
    time.sleep(2)
    assert "Dashboard" in driver.page_source or "Welcome" in driver.title

def test_invalid_login(driver):
    driver.get(BASE_URL)
    driver.find_element("id", "username").send_keys("invalid_user")
    driver.find_element("id", "password").send_keys("wrong_password")
    driver.find_element("id", "login-btn").click()
    time.sleep(2)
    assert "Invalid credentials" in driver.page_source

def test_empty_fields(driver):
    driver.get(BASE_URL)
    driver.find_element("id", "login-btn").click()
    time.sleep(1)
    assert "This field is required" in driver.page_source or "required" in driver.page_source.lower()
