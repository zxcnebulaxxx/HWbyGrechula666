import csv
from datetime import datetime

def get_online():
    # пока вручную
    return 5400

def get_coin_price():
    # пока вручную
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

    print("Данные сохранены:", row)

if __name__ == "__main__":
    save_to_csv()
