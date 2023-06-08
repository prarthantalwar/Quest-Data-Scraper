# Quest Data Scraper

This project is a web scraper implemented in Python using the Selenium library to extract data from a specific website. It retrieves information about quests and saves it in an Excel file.

## Prerequisites

- Python 3.x
- ChromeDriver (compatible with your Chrome browser version)
- Selenium
- pandas

## Installation

1. Clone the repository:

git clone https://github.com/prarthantalwar/quest-data-scraper.git


2. Install the required packages:

pip install -r requirements.txt


Ensure that you have ChromeDriver installed and the path to the driver executable specified correctly in the code.

## Usage

1. Run the `quest_scraper.py` script:

python quest_scraper.py


The script will open a Chrome browser window, navigate to the target website, and start scraping the quest data.

2. Once the scraping is complete, the data will be saved in an Excel file named `Quest data.xlsx`.

## Configuration

You can modify the following variables in the `quest_scraper.py` script to customize the scraping process:

- `path_driver`: Path to the ChromeDriver executable.
- `url`: URL of the website to scrape. (Modify the data needed to scrape accordingly)

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

