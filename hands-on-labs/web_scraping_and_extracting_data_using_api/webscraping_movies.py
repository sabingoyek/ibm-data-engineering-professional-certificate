import requests
import sqlite3
import pandas as pd
from bs4 import BeautifulSoup
from sqlalchemy import types

url = 'https://web.archive.org/web/20230902185655/https://en.everybodywiki.com/100_Most_Highly-Ranked_Films'
db_name = 'Movie.db'
table_name = 'Top_50'
csv_path = 'top_50_films.csv'
df = pd.DataFrame(columns=["Average Rank", "Film", "Year"])
count = 0

html_page = requests.get(url).text
data = BeautifulSoup(html_page, 'html.parser')


tables = data.find_all('tbody')
rows = tables[0].find_all('tr')

data_dict = {"Average Rank": [], "Film": [], "Year": []}

for row in rows:
    if count < 50:
        col = row.find_all('td')
        if len(col) != 0:
            data_dict['Average Rank'].append(int(col[0].contents[0]))
            data_dict['Film'].append(str(col[1].contents[0]))
            data_dict['Year'].append(int(col[2].contents[0]))
            count += 1
    else:
        break

#print(data_dict)

df = pd.DataFrame.from_dict(data_dict)


# saving the dataframe as csv file
df.to_csv(csv_path)

# saving the data into a database
conn = sqlite3.connect(db_name)
df.to_sql(table_name, conn, if_exists='replace', index=False)
conn.close()
