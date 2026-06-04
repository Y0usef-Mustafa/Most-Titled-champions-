import requests
import pandas as pd
from bs4 import BeautifulSoup
import time 


champions = []

print("Collecting Data ........")


for year in range(2000, 2025):
   
    url = f'https://www.formula1.com/en/results/{year}/team'
   
    try:
        html_page = requests.get(url).text
        soup = BeautifulSoup(html_page, 'html.parser')
        
        tables = soup.find_all('tbody')
        
        if tables:
            rows = tables[0].find_all('tr')
            if len(rows) > 0:
                col = rows[0].find_all('td')
                if len(col) != 0:
                    
                    winning_team = col[1].text.strip()
                    champions.append(winning_team)
                    print(f"Champion {year}:{winning_team}")
                    
        
        time.sleep(0.5)

    except Exception as err:
        print(f"Promblm happed in  {year}: {err}")


df_champions = pd.DataFrame(champions, columns=['Team'])

top_teams = df_champions['Team'].value_counts().reset_index()
top_teams.columns = ['Team', 'Total Championships']

print("\n--- History champions since 2000  with number of titels ---")
print(top_teams)
csv_path = r'F:\Data Topics\Data Engineering\Python project for Data Engineering\Web_scraping_Most_titled_teams_F1\all_time_champions.csv'
top_teams.to_csv(csv_path, index=False)
