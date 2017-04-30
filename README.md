# arctic-us
Two ideas: (1) use a map of the United States to show the area of Arctic sea ice. As the ice melts, 
we show states fading out to show the extent of the damage or (2) we show a circle of destruction 
around the users location which shows landmarks being destroyed over time. I prefer idea (2) so I'm
going to go ahead and start working on that.

## prototype
![Prototype 1](prototype1.png)

![Prototype 2](prototype2.png)

## setup
Start by running `data/download.sh` to get the raw data from the NSIDC website. This can take up to
an hour since we have to recursively download all of the image files; you can also ask me to send a
copy directly to you. Next, run `data/preprocess.py` to produce the processed dataset which holds a
subset of the data - you can change the subset that is extracted by modifying `TARGET_DAYS`.
