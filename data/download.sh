wget -r -nH --cut-dirs=10 ftp://sidads.colorado.edu/DATASETS/NOAA/G02135/north/monthly/data/ -P raw/csv/
wget -r -nH --cut-dirs=10 ftp://sidads.colorado.edu/DATASETS/NOAA/G02135/north/monthly/images/10_Oct/ -P raw/image/ -A "*conc_v2.1.png"
wget -r -nH --cut-dirs=10 ftp://sidads.colorado.edu/DATASETS/NOAA/G02135/north/monthly/images/10_Oct/ -P raw/image/ -A "*conc_hires_v2.1.png"
