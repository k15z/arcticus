import os
import csv
import json
from PIL import Image
from glob import glob

entries = []
for csv_file in glob("raw/csv/*.csv"):
    with open(csv_file, "rt") as fin:
        reader = csv.DictReader(fin, delimiter=",")
        reader = map(lambda d: {k.strip(): v.strip() for k, v in d.items()}, reader)
        for entry in reader:
            year = int(entry["year"])
            month = int(entry["mo"])
            area = float(entry["area"])
            entries.append((year, month, area))

def is_relevant(row):
    year, month, area = row
    return year >= 1992 and year % 4 == 0 and month == 10
entries = sorted(filter(is_relevant, entries))
entries = [{"year": y, "month": m, "area": a} for y, m, a in entries]

max_area = max(map(lambda x: x["area"], entries))
min_area = max(map(lambda x: x["area"], entries))

for entry in entries:
    year = str(entry["year"])
    month = str(entry["month"])
    if len(month) == 1: month = "0" + month
    if os.path.exists("raw/image/N_{}{}_conc_highres_v2.1.png".format(year, month)):
        img = Image.open("raw/image/N_{}{}_conc_highres_v2.1.png".format(year, month))
    else:
        img = Image.open("raw/image/N_{}{}_conc_v2.1.png".format(year, month))
    img.save("processed/" + year + month + ".png")
    entry["png"] = "data/processed/" + year + month + ".png"
    entry["radius"] = 1000.0 * entry["area"] / max_area
json.dump(entries, open("processed/entries.json", "wt"), indent=2)
