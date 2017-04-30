wget ftp://sidads.colorado.edu/DATASETS/NOAA/G02186/masie_4km_allyears_extent_sqkm.csv -O raw/arctic_sea_ice.csv
wget -r ftp://sidads.colorado.edu/DATASETS/NOAA/G02186/png/4km/ -P raw/
cp -r raw/sidads.colorado.edu/DATASETS/NOAA/G02186/png/4km raw/png
rm -r raw/sidads.colorado.edu
