# F1 Constructors' World Champions Scraper 🏎️🏆

## Overview
This project is a web scraping script built with Python to extract data about the most titled Formula 1 Constructor teams of all time. It scrapes the Wikipedia page, processes the HTML table, and exports a clean, structured CSV file containing the constructors and their total number of world championships. 

This repository demonstrates foundational Data Engineering skills, specifically the Extraction and Transformation phases of gathering unstructured web data.

## Files in this Repository
* `Web_scraping_Most_titled_teams_F1.py`: The main Python script that performs the web scraping using BeautifulSoup and data manipulation using Pandas.
* `all_time_champions.csv`: The final, cleaned output dataset containing the extracted F1 data.

## Technologies Used
* **Python**
* **BeautifulSoup4** (HTML parsing and Web Scraping)
* **Pandas** (Data manipulation and CSV export)
* **Requests** (HTTP requests)

## How to Run
1. Ensure you have the required libraries installed in your environment:
   ```bash
   pip install beautifulsoup4 pandas requests
