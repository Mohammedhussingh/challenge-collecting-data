# Challenge-Collecting-Data

## Description
This project aims to collect real estate data from various sources in Belgium to build a comprehensive dataset for predicting property prices. The collected dataset will contain detailed information about at least 10,000 properties and will be used for training a machine learning model to predict real estate prices.

The dataset includes information such as locality, property type, price, number of rooms, surface areas, features (like garden, swimming pool), and much more. This data will help in creating a robust and accurate model for real estate price predictions.

## Installation

### Prerequisites
To get started with this project, you'll need to have Python installed on your machine. Additionally, you'll need the following libraries:
- `requests` (for web scraping)
- `beautifulsoup4` (for HTML parsing)
- `pandas` (for data manipulation)
- `numpy` (for numerical operations)
- `csv` (for writing to CSV files)

You can install the necessary Python libraries using pip:

```bash
pip install requests beautifulsoup4 pandas numpy
```


## Usage
Scraping and Collecting Data
To scrape the website and collect property data, follow these steps:

Initialize the project: Ensure you have all the required libraries installed.

Run the main script: The script main.py is the main file to gather the data. Execute the script to begin the scraping process.

```bash
Code kopiÃ«ren
python collect_data.py
```


### Data Cleaning and Preprocessing:
 The collected data will be stored in a CSV file, ensuring it follows the required structure and contains no missing values.

### CSV Output: 
The final dataset will be saved as real_estate_data.csv in the root directory. The dataset will include the following columns:

- Locality
- Type of property (House/Apartment)
- Subtype of property (Bungalow, Chalet, Mansion, etc.)
- Price
- Type of sale
- Number of rooms
- Living area
- Fully equipped kitchen (0 = No, 1 = Yes)
- Furnished (0 = No, 1 = Yes)
- Open fire (0 = No, 1 = Yes)
- Terrace (0 = No, 1 = Yes)
- If yes: Terrace area
- Garden (0 = No, 1 = Yes)
- If yes: Garden area
- Surface of the land
- Surface area of the plot of land
- Number of facades
- Swimming pool (0 = No, 1 = Yes)
- State of the building (New, Renovated, etc.)

## Data Collection Strategy
- Scrape Emmoweb real estate websites to gather a variety of property listings.
- Ensure the dataset is free from duplicates and that missing values are handled by setting them as `None`.
- Avoid scraping data that violates any legal or ethical guidelines (e.g., privacy concerns).
  ![Screenshot from 2024-11-14 12-09-12](https://github.com/user-attachments/assets/eecb2fcf-123e-491b-8cf5-39fa47197b10)


## Contributors
- **Mohamad Hussain** 
- **Celina**
- **Mero** 


## Timeline
- **Day 1-2:** Scraping and gathering initial data from real estate websites.
- **Day 3:** Data cleaning and preprocessing, including handling missing values and duplicates, and making it complete.
- **Day 4:** Final dataset creation, writing to CSV, and preparation for machine learning use.




