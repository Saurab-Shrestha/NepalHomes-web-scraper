import requests
from bs4 import BeautifulSoup
import pandas as pd
from tqdm import tqdm
from selenium import webdriver

# set up the Selenium driver
options = webdriver.Firefox()

# specify the URL
URL = "https://www.nepalhomes.com/search?find_property_category=5d660cb27682d03f547a6c4a"

# create empty lists to store the data
land_area = []
road_access = []
facing = []
floor = []
parking = []
bedroom = []
bathroom = []
furnish_status = []
builtup_area = []
built_year = []
locations = []
title = []
prices = []

# create an empty set to store the hrefs
href_set = set()

# iterate over all pages
for page_number in tqdm(range(1, 426)):
    # construct the page URL
    if page_number == 1:
        page_url = URL
    else:
        page_url = URL + "&page=" + str(page_number) + "&sort=1"
        
    # get the page HTML
    page = requests.get(page_url)
    soup = BeautifulSoup(page.content, "html.parser")
    nepalhomes_url = "https://www.nepalhomes.com/"
    # extract the data for each property on the page


    for feature in soup.find_all('div', class_='property-listing-results-item'):

        for link in feature.find_all('a'):
            href = link.get('href')
            if href and href.startswith("/detail/") and href not in href_set:
                href_set.add(href)

                property_url = href
                full_url = nepalhomes_url + property_url
                property_page = requests.get(full_url)
                property_soup = BeautifulSoup(property_page.content, "html.parser")
                
                header = property_soup.select_one(".details--hero-header")
                title.append(header.select_one('.title').text.strip())
                prices.append(header.select_one('.price').text.strip())
                locations.append(header.select_one('.location').text.strip())
                list_overview = property_soup.find_all('div', {'class': 'excerpt'})
                
                for features in list_overview:
                    h3_text = features.select_one('h3').text.strip()
                    h5 = features.select_one('h5')
                    if h3_text == "LAND AREA":
                        land_area.append(h5.text.strip() if h5 else "NAN")
                    elif h3_text == "ROAD ACCESS":
                        road_access.append(h5.text.strip() if h5 else "NAN")
                    elif h3_text == "FACING":
                        facing.append(h5.text.strip() if h5 else "NAN")
                    elif h3_text == "FLOOR":
                        floor.append(h5.text.strip() if h5 else "NAN")
                    elif h3_text == "PARKING":
                        parking.append(h5.text.strip() if h5 else "NAN")
                    elif h3_text == "BEDROOM":
                        bedroom.append(h5.text.strip() if h5 else "NAN")
                    elif h3_text == "BATHROOM":
                        bathroom.append(h5.text.strip() if h5 else "NAN")
                    elif h3_text == "FURNISH STATUS":
                        furnish_status.append(h5.text.strip() if h5 else "NAN")

            # If any list is shorter than the others, add "NAN" values to make them equal length
            max_len = max(len(land_area), len(road_access), len(facing), len(floor), len(parking), len(bedroom), len(bathroom), len(furnish_status))
            for lst in [land_area, road_access, facing, floor, parking, bedroom, bathroom, furnish_status]:
                while len(lst) < max_len:
                    lst.append("NAN")


# create a dataframe from the extracted data
data ={
    'title': title,
    'price': prices,
    'location': locations,
    'land_area': land_area,
    'road_access': road_access,
    'facing': facing,
    'floor': floor,
    'bedroom': bedroom,
    'bathroom': bathroom,
    'parking': parking,
    'furnish_status': furnish_status
}

final_df = pd.DataFrame(data)
final_df.to_csv('property_data.csv', index=False)

href_list = list(href_set)
href_df = pd.DataFrame(href_list)
href_df.to_csv("property_link.csv",index=False)