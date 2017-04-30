import os
import csv
import json

TARGET_DAYS = [1, 90, 180, 270]

entries_csv = []
entries_json = []
with open("raw/arctic_sea_ice.csv", "rt") as fin:
    next(fin) # ignore their header
    reader = csv.DictReader(fin)
    for row in reader:
        row = {k: v.strip() for k, v in row.items()}
        year = int(row["yyyyddd"][:4])
        day = int(row["yyyyddd"][4:])
        area = float(row[" (0) Northern_Hemisphere"])
        if day in TARGET_DAYS:
            entries_csv.append((year, day, area))
            entries_json.append({
                "year": year, 
                "day": day, 
                "area": area,
                "png": "data/processed/4km/" + str(year) + "/masie_all_r00_v01_{}_4km.png".format(row["yyyyddd"])
            })
        # assert os.path.exists("processed/4km/" + str(year) + "/masie_all_r00_v01_{}_4km.png".format(row["yyyyddd"])), row["yyyyddd"]

with open("processed/northern.csv", "wt") as fout:
    writer = csv.writer(fout)
    writer.writerow(["year", "day", "northern_hemisphere_area"])
    writer.writerows(entries_csv)

with open("processed/northern.json", "wt") as fout:
    json.dump(entries_json, fout, indent=2)
