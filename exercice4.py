import sqlite3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.add_argument("--disable-extensions")
options.add_argument("--ignore-certificate-errors")

# Use ChromeDriverManager to automatically download and manage chromedriver
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=options)

URL = "https://www.welcometothejungle.com/fr/jobs?page=1&refinementList%5Bprofession_name.fr.Tech%5D%5B%5D=Data%20Analysis&refinementList%5Bcontract_type_names.fr%5D%5B%5D=CDI"

result = driver.get(URL)
time.sleep(4)

# Find job elements
job_elements = driver.find_elements(By.XPATH, "//li[@data-testid='search-results-list-item-wrapper']")

# Connect to SQLite database
conn = sqlite3.connect('jobs.db')
cursor = conn.cursor()

# Create jobs table if not exists
cursor.execute('''CREATE TABLE IF NOT EXISTS jobs (
                    id INTEGER PRIMARY KEY,
                    job_title TEXT,
                    company_name TEXT,
                    location TEXT
                )''')

# Insert job data into the database
for job_element in job_elements:
    job_title = job_element.find_element(By.XPATH, ".//h4").text
    company_name = job_element.find_element(By.XPATH, ".//span[@class='sc-ERObt ldmfCZ sc-6i2fyx-3 eijbZE wui-text']").text
    location = job_element.find_element(By.XPATH, ".//span[@class='sc-68sumg-0 gvkFZv']").text

    # Insert job data into the database
    cursor.execute("INSERT INTO jobs (job_title, company_name, location) VALUES (?, ?, ?)", (job_title, company_name, location))

# Commit changes and close database connection
conn.commit()
conn.close()

# Close the browser
driver.quit()

print("Data stored in the database successfully.")
