# Unemployment Data Scrapper

## Overview

Unemployment Data Scraper is a Python-based project that automates the process of collecting and organizing unemployment data from the data.gov.ro website. 
The project uses web scraping and API calls to gather relevant information, which is then stored in a structured database for further analysis or reporting.

## Features
- **Web Scraping**: Extracts data from the data.gov.ro website.
- **API Integration**: Makes API calls to retrieve additional data points.
- **Database Creation**: Organizes the scraped and API data into a relational database.
- **Automation**: Can be scheduled to run periodically for up-to-date information.
  
## Installation
- Clone the repository.
- Install the dependencies and you are good to go. Make sure to create the database tables first.
  
## Usage
- **Scraping and API Calls**: The script scrapes unemployment data from data.gov.ro and enriches it with additional data from relevant APIs.
- **Data Storage**: All collected data is stored in the database you configured.
- **Custom Queries**: You can run custom SQL queries on the database for analysis.

## Technologies Used
- **Python**: Core language used for scripting.
- **Libraries**: requests, BeautifulSoup.
- **Database**: PostgreSQL.
