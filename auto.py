from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path='./chromedriver.exe')
web_driver = webdriver.Chrome(options=options, service=service)
web_driver.maximize_window()
web_driver.get("https://maxfoccroulle.pythonanywhere.com/contact.html")
web_driver.find_element(By.ID, "email").send_keys("foccroullemax@gmail.com")
web_driver.find_element(By.ID, "subject").send_keys("Test")
web_driver.find_element(By.NAME, "message").send_keys("Do you like my website?")
print("-------------------")
(web_driver.find_element(By.CSS_SELECTOR, "button[type='submit'].btn.btn-default.btn-lg").click())
