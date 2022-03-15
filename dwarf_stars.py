import pandas as pd
from bs4 import BeautifulSoup as bs
import requests

dawrf_star_url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
page= requests.get(dawrf_star_url)
print(page)

soup= bs(page.text,"html.parser")

dwarf_star_table= soup.find_all("table")

temp_list=[]
table_rows= dwarf_star_table[7].find_all("tr")
for tr in table_rows:
    td= tr.find_all("td")
    row= [i.text.rstrip() for i in td]
    temp_list.append(row)

star_name=[]
radius=[]
mass=[]
distance=[]

for i in range(1,len(temp_list)):
    star_name.append(temp_list[i][0])
    radius.append(temp_list[i][8])
    mass.append(temp_list[i][7])
    distance.append(temp_list[i][5])

df= pd.DataFrame(list(zip(star_name,radius,mass,distance)),columns=['star_name','radius','mass','distance'])
print(df)

df.to_csv('dwarf_stars_list.csv')