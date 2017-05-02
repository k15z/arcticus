# arcticus
This is the code for CMS.631: Sketch 5. In this visualization, we use creative maps to show the sea
ice levels over the past decade. You can imagine this being embedded in an article on the New York 
Time about the rapid decrease in artic sea ice levels.

We start by asking users to map out their environment by listing some of the places they frequently
visit. Next, we show a map of the Arctic sea ice on the left labeled as a polar bear's environment 
and a map with a circle around the user's places as the user's environment. The user watches as the
environment shrinks over time, cutting of access to their food/school/whatever.

![screenshot](images/prototype.png)

## setup
Start by running `data/download.sh` to get the raw data from the NSIDC website. This can take up to
an hour since we have to recursively download all of the image files; you can also ask me to send a
copy directly to you. Next, run `data/preprocess.py` to produce the processed dataset.
