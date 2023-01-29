from selenium import webdriver

DRIVER_PATH = "./chromedriver"
CHROME_PATH = "<folder_location_binary_chrome>"

option = webdriver.ChromeOptions()
option.binary_location = CHROME_PATH

browser = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=option)

browser.get("<insert_url>")