import selenium.webdriver as webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.Service import Service

driver = webdriver.Chrome(ChromeDriverManager().install())
