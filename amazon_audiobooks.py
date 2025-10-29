import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pymongo import MongoClient

# === MongoDB connection ===
client = MongoClient('("mongodb+srv://<username>:<password>@cluster0.mongodb.net/?appName=Cluster0")')
db = client["audible_db"]         # database name
collection = db["audiobooks"]     # collection name

options = Options()
options.headless = False
# options.add_argument("window-size=1920x1080")

web = "https://www.audible.com/search"
driver = webdriver.Chrome(options=options)
driver.get(web)
driver.maximize_window()

wait = WebDriverWait(driver, 15)

# pagination
pagination = driver.find_element(By.XPATH, '//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME, 'li')
last_page = int(pages[-2].text)

current_page = 1

book_title = []
book_author = []
book_length = []

while current_page <= last_page:
    # ✅ Wait for the main container
    container = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "adbl-impression-container"))
    )

    products = WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located((By.XPATH, '//li[contains(@class, "productListItem")]'))
    )

    for product in products:
        title = product.find_element(By.XPATH, './/h3[contains(@class, "bc-heading")]').text
        author = product.find_element(By.XPATH, './/li[contains(@class, "authorLabel")]').text
        length = product.find_element(By.XPATH, './/li[contains(@class, "runtimeLabel")]').text

        book_title.append(title)
        book_author.append(author)
        book_length.append(length)

    current_page += 1

    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        break

driver.quit()

# === Save to CSV ===
df = pd.DataFrame({
    'title': book_title,
    'author': book_author,
    'length': book_length
})
df.to_csv('books_headless.csv', index=False)
print(df)

# === Save to MongoDB ===
records = df.to_dict("records")  # convert DataFrame rows to dicts
if records:                      # avoid inserting empty data
    collection.insert_many(records)
    print(f"✅ Inserted {len(records)} records into MongoDB collection 'audiobooks'")
else:
    print("⚠️ No records to insert into MongoDB.")
