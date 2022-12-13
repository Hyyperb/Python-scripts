from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

settings = Options()
settings.headless = True
settings.set_preference("browser.download.folderList",2)
settings.set_preference("browser.download.manager.showWhenStarting",False)
settings.set_preference("browser.download.dir","/home/bhavik")
settings.set_preference("browser.helperApps.neverAsk.saveToDisk","text/csv")

driver = webdriver.Firefox(options=settings)
driver.get("https://texttohandwriting.com/")

driver.implicitly_wait(5)

text = driver.find_element(By.ID,"note")
render = driver.find_element(By.CLASS_NAME,"generate-image-button")
download = driver.find_element(By.ID,"download-as-pdf-button")
handwriting = Select(driver.find_element(By.ID,"handwriting-font"))

handwriting.select_by_visible_text("handwriting-8")
render.click()
download.click()
