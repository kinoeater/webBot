from selenium import webdriver

class webAutomation():
    def __init__(self):
        self.driver = webdriver.Chrome()
    
    def login(self):
        self.driver.get('https://google.com')
        self.driver.find_element_by_xpath("//a[contains(text(),'Log in')]").click()
        self.driver.find_element_by_name('username').send_keys('kinoeater')
        



