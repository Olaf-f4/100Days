from bs4 import BeautifulSoup
import requests, time

website = requests.get("https://lp.jetbrains.com/python-developers-survey-2021/#PythonPackaging")
html = BeautifulSoup(website.text, "html.parser")

while True:
    time_obj = time.strftime('%Y-%m-%d')
    last_scan = ''
    if time_obj != last_scan:
        with open('website.html', 'w') as L:
            L.write(html.prettify())
    else:
        break

sub_section = html.div('div', class_='wt-container')
print(sub_section)

# deep_dive = sub_section.find('div ', class_='')
# print(html.prettify())


