from datetime import datetime
import requests
import json

import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

# -----------Todays date --------- #
date = datetime.now()
today = date.strftime("%m/%d/%Y")
time = date.strftime("%I:%M")

# --------------------- Nutrition -------------------------
# Constants
headers = {
    'x-app-id': os.getenv('NUTRITION_ID'),
    'x-app-key': os.getenv('NUTRITION_KEY')
}
body = {
    "query": "I ran 12 miles in 13 minutes"
}

nutri_url = "https://trackapi.nutritionix.com/v2/"
# nutri_nutrtion_endpoint = nutri_url + "search/instant/?query=hamburger"
nutty_nutty = nutri_url + "natural/exercise"


grab = requests.post(nutty_nutty, headers=headers, data=json.dumps(body))
json_grab = grab.json()

# Getting information from json
workout_type = json_grab["exercises"][0]["user_input"]
duration = json_grab["exercises"][0]["duration_min"]
calories = json_grab["exercises"][0]["nf_calories"]


# ---------------- Sheety / Spreadsheet -------------------#
post_link = "https://api.sheety.co/584f71e8d3042f1c0fc9d72d5fc40345/workout/activityLog"

headers_sheety = {
    "Authorization": os.getenv('SHEETY_BEARER')
}
# Add a row
activityLog = {
    "activityLog": {
        "date": today,
        "time": time,
        "exercise": workout_type,
        "duration": duration,
        "calories": calories
    }
}


sheety_post = requests.post(post_link, headers=headers_sheety, json=activityLog)
print(sheety_post.text)
