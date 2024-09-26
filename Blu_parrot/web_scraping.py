# from selenium import webdriver

# # If chromedriver.exe is in PATH, no need to specify the path
# driver = webdriver.Chrome()

# # Open Google to test
# driver.get("https://www.google.com")

# # Interact with the page (e.g., print the title)
# print(driver.title)

# driver.quit()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import json
import time

# Set up Selenium WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Optional: Run browser in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL of the page to scrape
url = 'https://www.otipy.com/category/vegetables-1'

# Open the page with Selenium
driver.get(url)

# Wait for JavaScript to load the content
time.sleep(5)

# Scroll down to load more products (if applicable)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)  # Adjust sleep time if more products need to load

# Fetch product elements
product_elements = driver.find_elements(By.CLASS_NAME, 'style_card_info__xGm58')


products = []

# Extract product information by HTML Class
for product in product_elements:
    try:
        name = product.find_element(By.CLASS_NAME, 'style_prod_name__QllSp').text
        standard_price = product.find_element(By.CLASS_NAME, 'style_selling_price__GaIsF').text
        selling_price = product.find_element(By.CLASS_NAME, 'style_final_price__FERLK').text
        mrp = product.find_element(By.CLASS_NAME, 'style_striked_price__4ghn5').text
        quantity = product.find_element(By.CLASS_NAME, 'style_prod_qt__cXcqe').text

        # Appending product details to the list
        products.append({
            'Name': name,
            'Standard Price': standard_price,
            'Selling Price': selling_price,
            'MRP': mrp,
            'Quantity': quantity
        })
    except Exception as e:
        print(f"Error extracting product: {e}")
        continue


products_json = json.dumps(products, indent=4)        # Converting the list of products to JSON format


print(products_json)  # printing the output


driver.quit()         # Closing the browser
