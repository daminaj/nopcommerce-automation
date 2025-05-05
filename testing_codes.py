from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)  # Keeps browser open after script ends

# Initialize the Chrome driver with options
driver = webdriver.Chrome(
    service=ChromeService(ChromeDriverManager().install()),
    options=chrome_options
)


driver.get("https://www.google.com/")
driver.maximize_window()


