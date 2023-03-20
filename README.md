# NepalHomes Web Scraper

This is a web scrapper build for **educational** purpose to scrap Home data from [Nepal Homes](https://www.nepalhomes.com/).

The scraper extracts data on properties listed under the category 'House for sale' and saves the information to a CSV file.

The scraper scrapers through multiple pages and extracs the following information for each property:
- Title
- Price
- Location
- Land area
- Road access
- Facing
- FLoor
- Bedroom
- Bathroom
- Parking
- Furnish status

## Installation
1. Clone the repository
```
git clone https://github.com/yourusername/nepalhomes-scraper.git 
```

2. Install the required packages by running the following command
```
pip install -r requirements.txt
```

3. Run the scrapper by executing the script
```
python scrapper.py
```
## Usage

The scraper will extract the data and save it to a CSV file named 'nepalhomes_data.csv' in the same directory as the script.

You can open the CSV file using any spreadsheet software or Python and use the data for analysis and visualization purposes.

Note: The scraper may take a few minutes to complete, depending on the number of pages to be scraped.

## Contributing

Contributions are always welcome! If you would like to contribute to this project, please open an issue to discuss the proposed changes or submit a pull request.
