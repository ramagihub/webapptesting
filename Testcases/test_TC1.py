
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import  time
import pytest

@pytest.mark.smoke

def test_Login ():
    driver = webdriver.Ie(executable_path="D:\\IEDriverServer_Win32_3.150.1\\IEDriverServer.exe")
    driver.get("http://www.google.com")
    driver.maximize_window()
    print(driver.title)
    time.sleep(5)
    assert driver.title =='Google'
    driver.close()

def test_log():
    x=20
    assert  x==20;
'''def test_Login_app():
    driver = webdriver.Ie(executable_path="D:\\IEDriverServer_Win32_3.150.1\\IEDriverServer.exe")
    driver.get("http://www.google.com")
    driver.maximize_window()
    print(driver.title)
    time.sleep(5)
    assert driver.title == 'Google' '''

''' links=driver.find_elements_by_tag_name('a')
for link in links:
    print(link.get_attribute('href')) '''

'''assert driver.title,"tepy.py.teststing" '''





