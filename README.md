# Formula 1 Champions Historical Web Scraper

A Python-based web scraping project designed to extract, parse, and aggregate historical Formula 1 Constructor Champions data from the official Formula 1 website for the seasons 2000 through 2024.

## 🛠️ Project Steps Summary:
1. **Web Scraping & HTTP Requests:** Automated multi-page data collection by iterating through annual F1 team standings URLs using the `requests` library with built-in time delays to respect server pacing.
2. **HTML Parsing:** Processed the raw web layouts using `BeautifulSoup` to target specific structural elements (`<tbody>` and `<tr>`) containing the championship data.
3. **Data Extraction:** Cleaned and isolated text strings to extract the exact name of the top-ranked winning constructor for each individual season.
4. **Data Aggregation:** Leveraged `pandas` to analyze the collected records, performing frequency counts (`value_counts()`) to rank the teams by their total historical championships since 2000.
5. **Storage:** Exported the finalized structured insights into a clean, analytical CSV file (`all_time_champions.csv`).

## 📂 Final Project Files:
* `Web_scraping_Most_titled_teams_F1.py`: The main Python automation script containing the web scraping logic and parsing routines.
* `all_time_champions.csv`: The aggregated output dataset containing the structured leaderboard of F1 teams and their total title counts.

