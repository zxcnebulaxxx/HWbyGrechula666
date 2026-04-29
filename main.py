import csv
import re
import requests
from bs4 import BeautifulSoup
from datetime import datetime

URL = "https://hotmc.ru/minecraft-server-211679"

def get_online():
try:
headers = {
"User-Agent": "Mozilla/5.0"
}

    response = requests.get(URL, headers=headers, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    text = " ".join(soup.stripped_strings)

    match = re.search(r"Игроки:\s*(\d+)\s*из", text)

    if match:
        return int(match.group(1))

    return "not found"

except Exception as e:
    return f"error: {str(e)}"

def get_coin_price():
return 185

def save_to_csv():
now = datetime.now()

row = [
    now.strftime("%d.%m.%Y"),
    now.strftime("%H:%M"),
    get_online(),
    get_coin_price()
]

file_name = "data.csv"

try:
    with open(file_name, "x", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["date", "time", "online", "coin_price"])
except FileExistsError:
    pass

with open(file_name, "a", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(row)

print("Saved:", row)

if **name** == "**main**":
save_to_csv()
