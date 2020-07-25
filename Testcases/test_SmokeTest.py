from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException
import pytest

def test_open_website():
        driver = webdriver.Ie(executable_path="D:\\IEDriverServer_Win32_3.150.1\\IEDriverServer.exe")
        driver.get("http://www.google.com")
        driver.maximize_window()
        print(driver.title)
        assert driver.title=='Google1'
        time.sleep(5)
        try:
                driver.find_element_by_name('q').send_keys("test")
        except NoSuchElementException:
                print("exe")
        driver.close()