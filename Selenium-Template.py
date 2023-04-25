from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import chromedriver_autoinstaller
from pyvirtualdisplay import Display
display = Display(visible=0, size=(800, 800))  
display.start()

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

options = webdriver.ChromeOptions()    
options.add_experimental_option("detach", True)
options.add_argument('--headless')

i = 0
while i < 1:
  try:
    driver = webdriver.Chrome(options=options)
    wait = WebDriverWait(driver, 15)
    driver.get("https://moneroocean.stream/")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="AddrField"]'))).send_keys("49mE3NVouyTiyK9CdfupeTTv7mAQW1ry11kyn7PgKAVBLCSbJ5RtWNLXps2BDY7EfrB4VjJZgiz2z9GzdtzB1uibMbre6gs")
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="AddrField"]'))).send_keys(Keys.ENTER)
    wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="MinerDash"]/div[1]/div[1]/div[3]'))).click()
  except:
    print("error")
