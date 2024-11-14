from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import concurrent.futures
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import requests


#Drivers Call
# Specify the path to chromedriver
service = Service("/usr/local/bin/chromedriver")

# Create a new instance of the Chrome WebDriver
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://www.immoweb.be/en/search/house-and-apartment/for-sale")

### Exctracting all the links in House and apartment search page (all pages)

hrefs = []  # List to store all hrefs

# Function to extract links from a single page
def get_links_from_page(page_number):
    driver.get(f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&priceType=SALE_PRICE&page={page_number}&orderBy=relevance")
   
    
    # Wait for the links to load on the page
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "card__title-link"))
    )
    
    # Find all the elements with class 'card__title-link' and get their href
    links = driver.find_elements(By.CLASS_NAME, "card__title-link")
    print("I am in page : ", page_number)
    # Extract the href attribute from each link
    return [link.get_attribute("href") for link in links]

# Using ThreadPoolExecutor to scrape multiple pages concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks for each page (e.g., pages 1 to 333)
    future_to_page = {executor.submit(get_links_from_page, page+1): page+1 for page in range(333)}
   
    # Process results as they come in
    for future in concurrent.futures.as_completed(future_to_page):
        page_number = future_to_page[future]
        try:
            page_links = future.result()  # Get the result (links from the page)
            hrefs.extend(page_links)  # Add links to the main hrefs list
        except Exception as exc:
            print(f"Page {page_number} generated an exception: {exc}")

# Print the number of links found
print(f"Total number of links: {len(hrefs)}")

### Saving  them links in link.txt
with open('links.txt', 'w') as file:
    file.writelines([item + '\n' for item in hrefs])



### Exctracting all the links without new project pages (new project pages contain multible links)


hrefs = []  # List to store all hrefs

# Function to extract links from a single page
# re Wrie get_links_from_page function 
def get_links_from_page(page_number):
    driver.get(f"https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&isNewlyBuilt=false&page={page_number}&orderBy=relevance")

    
    # Wait for the links to load on the page
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "card__title-link"))
    )
    
    # Find all the elements with class 'card__title-link' and get their href
    links = driver.find_elements(By.CLASS_NAME, "card__title-link")
    print("I am in page : ", page_number)
    # Extract the href attribute from each link
    return [link.get_attribute("href") for link in links]

# Using ThreadPoolExecutor to scrape multiple pages concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks for each page (e.g., pages 1 to 333)
    future_to_page = {executor.submit(get_links_from_page, page+1): page+1 for page in range(333)}
   
    # Process results as they come in
    for future in concurrent.futures.as_completed(future_to_page):
        page_number = future_to_page[future]
        try:
            page_links = future.result()  # Get the result (links from the page)
            hrefs.extend(page_links)  # Add links to the main hrefs list
        except Exception as exc:
            print(f"Page {page_number} generated an exception: {exc}")

# Print the number of links found

Links2 = pd.DataFrame(hrefs, columns=['Links'])
# Saving to a new file
with open('Houses _appartments.txt', 'w') as file:
    file.writelines([item + '\n' for item in hrefs])

### Extracting the links of properties from each new real estate project page 




# Print the collected hrefs
print("Collected hrefs:", hrefs)


with open('new_project.txt', 'w') as file:
    file.writelines([item + '\n' for item in hrefs])


    ### Apartments tab reading

hrefs = []  # List to store all hrefs

# Function to extract links from a single page
def get_links_from_page(page_number):
    driver.get(f"https://www.immoweb.be/en/search/apartment/for-sale?countries=BE&page={page_number}&orderBy=relevance")

    
    # Wait for the links to load on the page
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "card__title-link"))
    )
    
    # Find all the elements with class 'card__title-link' and get their href
    links = driver.find_elements(By.CLASS_NAME, "card__title-link")
    print("I am in page : ", page_number)
    # Extract the href attribute from each link
    return [link.get_attribute("href") for link in links]

# Using ThreadPoolExecutor to scrape multiple pages concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks for each page (e.g., pages 1 to 333)
    future_to_page = {executor.submit(get_links_from_page, page+1): page+1 for page in range(333)}
   
    # Process results as they come in
    for future in concurrent.futures.as_completed(future_to_page):
        page_number = future_to_page[future]
        try:
            page_links = future.result()  # Get the result (links from the page)
            hrefs.extend(page_links)  # Add links to the main hrefs list
        except Exception as exc:
            print(f"Page {page_number} generated an exception: {exc}")

# Print the number of links found
print(f"Total number of links: {len(hrefs)}")

with open('Apartments.txt', 'w') as file:
    file.writelines([item + '\n' for item in hrefs])
### Houses


hrefs = []  # List to store all hrefs

# Function to extract links from a single page
def get_links_from_page(page_number):
    driver.get(f"https://www.immoweb.be/en/search/house/for-sale?countries=BE&isALifeAnnuitySale=false&isNewlyBuilt=false&page={page_number}&orderBy=relevance")
    
    # Wait for the links to load on the page
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "card__title-link"))
    )
    
    # Find all the elements with class 'card__title-link' and get their href
    links = driver.find_elements(By.CLASS_NAME, "card__title-link")
    print("I am in page : ", page_number)
    # Extract the href attribute from each link
    return [link.get_attribute("href") for link in links]

# Using ThreadPoolExecutor to scrape multiple pages concurrently
with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    # Submit tasks for each page (e.g., pages 1 to 333)
    future_to_page = {executor.submit(get_links_from_page, page+1): page+1 for page in range(333)}
   
    # Process results as they come in
    for future in concurrent.futures.as_completed(future_to_page):
        page_number = future_to_page[future]
        try:
            page_links = future.result()  # Get the result (links from the page)
            hrefs.extend(page_links)  # Add links to the main hrefs list
        except Exception as exc:
            print(f"Page {page_number} generated an exception: {exc}")

# Print the number of links found
print(f"Total number of links: {len(hrefs)}")


with open('houses.txt', 'w') as file:
    file.writelines([item + '\n' for item in hrefs])



### Creating new file with all data we extract


# Open all the files and read their contents
with open("Data Files/Offices.txt", "r") as offices_file, \
     open("Data Files/Grages.txt", "r") as garages_file, \
     open("Data Files/new_project.txt", "r") as houses_file, \
     open("Data Files/Houses _appartments.txt", "r") as houses_file1, \
     open("Data Files/Apartments.txt", "r") as apartments_file, \
     open("Data Files/houses.txt", "r") as houses_file_2:  # Added Houses.txt

    offices_links = offices_file.read().splitlines()
    garages_links = garages_file.read().splitlines()
    houses_links = houses_file.read().splitlines()
    apartments_links = apartments_file.read().splitlines()
    houses_links_2 = houses_file_2.read().splitlines() 
    houses_links1 = houses_file1.read().splitlines()
     # Read Houses.txt

# Combine all the links into one list
all_links = offices_links + garages_links + houses_links + apartments_links + houses_links_2 +houses_links1

# Create a DataFrame from the combined list
links_df1 = pd.DataFrame(all_links, columns=["Links"])

links_df1 = links_df1[~links_df1['Links'].str.contains("new-real-estate-project-", na=False)]
links_df1 = links_df1[~links_df1['Links'].str.contains("new-real-estate-project-", na=False)]
links_df1=links_df1.drop_duplicates()
links_df1 = links_df1[~links_df1['Links'].str.contains("new-real-estate-project-", na=False)]
# Changing the type 
Links_expanded = links_df1['Links'].str.split('/', expand=True)
Links_expanded.columns  = ["p","f",'Domain', 'Language', 'Category', 'Project_Type', 'Property_Type', 'Location', 'Postal_Code', 'Real_Estate_ID']

# Combine the expanded columns with the original DataFrame (if needed)
Links = Links_expanded.drop(["p","f","Domain","Language","Category","Property_Type"],axis=1)
Links=pd.concat([Links, links_df1], axis=1)
 #Convert Real_Estate_ID to numeric (integer)
Links["Real_Estate_ID"] = pd.to_numeric(Links["Real_Estate_ID"], errors="coerce").astype("Int64")

# Convert Postal_Code to string, preserving any leading zeros
Links["Postal_Code"] = Links["Postal_Code"].astype(str)

# Optionally ensure all other text columns are of type string
Links["Project_Type"] = Links["Project_Type"].astype("string")
Links["Location"] = Links["Location"].astype("string")
Links["Links"] = Links["Links"].astype("string")
Links.info()
columns_to_save = ['Project_Type', 'Location', 'Postal_Code', 'Real_Estate_ID', 'Links']

# Save to CSV with specified columns
Links.to_csv('selected_columns.csv', columns=columns_to_save, index=False)

with open('Final_Links_Final.txt', 'w') as file:
    file.writelines([item + '\n' for item in Links.Links])