from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import openpyxl
import time

wb = openpyxl.Workbook()
sheet = wb.active
sheet.title = "Amazon finds"
sheet.append(["Product Name", "Price", "Rating"])

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.amazon.in")

search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("laptop")
search_box.send_keys(Keys.RETURN)

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.XPATH, "//div[@data-component-type='s-search-result']")))

scroll_step = 800
scroll_pause_time = 1.5

for i in range(2): 
    scroll_position = (i + 1) * scroll_step
    driver.execute_script(f"window.scrollTo(0, {scroll_position});")
    print(f"Scroll #{i+1} done")
    time.sleep(scroll_pause_time)

print(" Scrolling stopped after 2 times.")

driver.save_screenshot("amazon_scroll_2x.png")
print("Screenshot saved as 'amazon_scroll_2x.png'")

products = driver.find_elements(By.XPATH, "//div[@data-component-type='s-search-result']")

for product in products[:10]:
    try:
        name = product.find_element(By.TAG_NAME, "h2").text
    except:
        name = "N/A"

    try:
        price = product.find_element(By.CLASS_NAME, "a-price-whole").text
    except:
        price = "N/A"

    try:
        rating = product.find_element(By.CSS_SELECTOR, "span.a-icon-alt").text
    except:
        rating = "N/A"

    sheet.append([name, price, rating])
    print(f"✔ {name} | ₹{price} | Rating: {rating}")

wb.save("amazon finds.xlsx")
print("Excel file saved as 'amazon finds.xlsx'")

driver.quit()
