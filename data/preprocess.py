import csv

entries = []
with open("raw/arctic_sea_ice.csv", "rt") as fin:
    next(fin) # ignore their header
    reader = csv.DictReader(fin)
    for row in reader:
        row = {k: v.strip() for k, v in row.items()}
        year = row["yyyyddd"][:4]
        day = row["yyyyddd"][4:]
        area = float(row[" (0) Northern_Hemisphere"])
        entries.append((year, day, area))

with open("processed/northern.csv", "wt") as fout:
    writer = csv.writer(fout)
    writer.writerow(["year", "day", "northern_hemisphere_area"])
    writer.writerows(entries)
