from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import database
import time
import os

os.environ['GH_TOKEN'] = ' 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 '
options = webdriver.FirefoxOptions()
options.set_preference("dom.webdriver.enabled", False)
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:97.0) Gecko/20100101 Firefox/97.0")
options.headless = True

driver = webdriver.Firefox(
    executable_path=GeckoDriverManager().install(),
    options=options
)


def get_website_url(name_website):
    try:
        driver.get("https://proxysite.cloud/")
        element = driver.find_element(By.ID, 'appendedInputButton')
        element.send_keys(name_website)
        element.submit()
        time.sleep(10)
        database.insert_new_url(name_website, driver.current_url)
        return driver.current_url
    finally:
        driver.close()
        driver.quit()
