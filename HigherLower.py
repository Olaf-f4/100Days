import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/List_of_awards_and_nominations_received_by_Johnny_Depp"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")
table = soup.find(id="mw-content-text")

table_elements = table.find_all("table", class_="infobox")
#print(table_elements)
for table_element in table_elements:
    #print(table_element, end="\n"*2)
    yes_count = table_element.find("td", class_="yes table_yes2 notheme")
    print(yes_count, end="\n"*2)
    # print(yes_count.text.strip())


# results = soup.find(id)

print(table.prettify())

