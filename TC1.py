from selenium import webdriver
from selenium.webdriver.common.keys import Keys
def test_Login ():
    driver = webdriver.Ie(executable_path="D:\\IEDriverServer_Win32_3.150.1\\IEDriverServer.exe")
    driver.get("http://www.google.com")
    driver.maximize_window()
    print(driver.title)
    assert driver.title == 'Google'
def test_xyz():
    print("helloo")
''' links=driver.find_elements_by_tag_name('a')
for link in links:
    print(link.get_attribute('href')) '''

'''assert driver.title,"testing" '''





