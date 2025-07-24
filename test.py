from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# Create Chrome options
options = Options()
options.add_argument("--window-size=1920x1080")

# Create WebDriver instance
driver = webdriver.Chrome(options=options)

# Wait 2 seconds after browser opens
time.sleep(50)

# Navigate to a website
driver.get("www.google.com")

# Get page title
print(driver.title)

# Keep browser open for 5 seconds before closing
time.sleep(5)

# Close the browser
driver.quit()