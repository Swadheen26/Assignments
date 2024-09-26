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

# To store files_name as per the execution date & time
import os
from datetime import datetime

# Set up Selenium WebDriver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")  # Optional: Run browser in headless mode
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# URL of the page to scrape
url = 'https://www.otipy.com/category/vegetables-1'

# Open the page with Selenium
driver.get(url)

# Wait for JavaScript to load the content
time.sleep(10)

# Scroll down to load more products (if applicable)
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(10)  # Adjust sleep time if more products need to load

# Fetch product elements
product_elements = driver.find_elements(By.CLASS_NAME, 'style_card_info__xGm58')


products = []

# Extract product information by HTML Class
for product in product_elements:
    try:
        name = product.find_element(By.CLASS_NAME, 'style_prod_name__QllSp').text
        price_element = product.find_element(By.CLASS_NAME, 'style_final_price__FERLK').text
        
        # Separate selling price and quantity based on ₹ 
        price_parts = price_element.split('₹')[-1].split()  # Take the part after the ₹ and split by spaces
        selling_price = price_parts[0]  # Extract the selling price
        
        # Extract quantity, which is typically the last part
        quantity = ' '.join(price_parts[1:])  # Joining the remaining parts to get output as '450 g'
        
        standard_price = product.find_element(By.CLASS_NAME, 'style_selling_price__GaIsF').text
        mrp = product.find_element(By.CLASS_NAME, 'style_striked_price__4ghn5').text

        # Appending product details to the list
        products.append({
            'Name': name,
            'Standard Price': standard_price.replace("₹", "").strip(),
            'Selling Price': selling_price.strip(),
            'MRP': mrp.replace("₹", "").strip(),
            'Quantity': quantity.strip()  # Preserve space between number and unit
        })
    except Exception as e:
        print(f"Error extracting product: {e}")
        continue


# products_json = json.dumps(products, indent=4)        # Converting the list of products to JSON format

def create_json_filename():
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%I%M%p")  
    filename = f"products_{timestamp}.json"

    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Join the directory with the filename to save it in the same location as the script
    file_path = os.path.join(current_directory, filename)

    return file_path

# Save products to a JSON file
def save_to_json_file(products_data):
    # Create the filename
    json_filename = create_json_filename()

    # Save the products data to the file
    with open(json_filename, 'w', encoding='utf-8') as json_file:
        json.dump(products_data, json_file, indent=4, ensure_ascii=False)
    
    print(f"Products saved to {json_filename}")
    print(f"Total products scraped: {len(products)}")

# Save the products to a new JSON file
save_to_json_file(products)

# Close the browser
driver.quit()