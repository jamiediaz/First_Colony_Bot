from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options 

service = ChromeService(executable_path="E:\projects\First_Colony_Bot\chromedriver.exe")

driver = webdriver.Chrome(options=Options())
driver.implicitly_wait(5000000)

driver.get("https://www.selenium.dev/selenium/web/web-form.html")

title = driver.title


# text_box = driver.find_element(by=By.NAME, value="my-text")
# submit_button = driver.find_element(by=By.CSS_SELECTOR, value="button")


# options = ChromeOptions()
# driver = webdriver.Chrome(s)
# driver.get('https://booknow.appointment-plus.com/b6l56ers/')

# driver.quit()

