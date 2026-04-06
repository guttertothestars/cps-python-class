INPUT_FILENAME = "playlist.csv"

file_ptr = open(INPUT_FILENAME)

for line in file_ptr:
    line = line.strip()
    print(line)
# ---------------------------------------------------------------------------
# now try the csv module
import csv

# start pointer at the top of the file
file_ptr.seek(0)

# this time use the reader to help us
reader = csv.DictReader(file_ptr)

# print each row and only select a few columns
for row in reader:
    print(row["Track Name"], "-", row["Artist Name(s)"], "-", row["Genres"])
# ---------------------------------------------------------------------------
# now try pandas module
import pandas

dataframe = pandas.read_csv(INPUT_FILENAME)
dataframe.columns  # see all of the columns
# ---------------------------------------------------------------------------
print("max danceability is", dataframe.Danceability.max())
# ---------------------------------------------------------------------------
print("min energy is", dataframe.Energy.min())
# ---------------------------------------------------------------------------
# sort by one of the columns.  just show a few columns.  first few rows.
column_name = "Danceability"
sorted_df = dataframe.sort_values(by=column_name, ascending=False)
sorted_df[["Track Name", "Artist Name(s)", column_name]].head(8)
# ---------------------------------------------------------------------------
# show last few rows (the tail)
sorted_df[["Track Name", "Artist Name(s)", column_name]].tail()
# ---------------------------------------------------------------------------
# get a count for columns with frequently recurring values
dataframe["Time Signature"].value_counts()
# ---------------------------------------------------------------------------
column_name = "Time Signature"
sorted_df = dataframe.sort_values(by=column_name, ascending=False)
sorted_df[["Track Name", "Artist Name(s)", column_name]].tail(3)
# ---------------------------------------------------------------------------
# now let's look at genres. create a subset of the dataframe to hold only 3 columns of our interest
genre_df = dataframe[["Track Name", "Artist Name(s)", "Genres"]]
genre_df
# ---------------------------------------------------------------------------
# Spotify stores NaN (not a number - a float data type) for some genres.
# essentially, it is blank.  And so let's drop any rows that have an empty genre
# axis=0 means to delete the ROW.  "any" means to delete the row if any field is blank
print("number of songs before the drop", len(genre_df))
genre_df = genre_df.dropna(axis=0, how="any")
print("number of songs before the drop", len(genre_df))
# ---------------------------------------------------------------------------
genre_df
# ---------------------------------------------------------------------------
# convert our subset dataframe to a list.
genre_strings = genre_df["Genres"].to_list()
print(genre_strings)
# ---------------------------------------------------------------------------
# create a rollup - a dictionary of our genres and their counts
genre_dictionary = dict()
# first loop through the genre str, which could contain more than one genre
for genre_str in genre_strings:
    # use the split method to chop up each genre separately
    genre_list = genre_str.split(",")
    # for each genre, see if already in our dictionary
    for g in genre_list:
        # look it up in the dictionary
        count = genre_dictionary.get(g)
        # if count is None, then that means the genre is NOT there.  We must add it.
        if count is None:
            genre_dictionary[g] = 1  # add it to the dictionary and set the count to 1
        else:
            genre_dictionary[g] = count + 1  # already found, add one to the counter

# too many genres, just count those with a count >= 2
# create a 'fav' genre dictionary as a copy
fav_genre_dictionary = dict(genre_dictionary)

"""
# cycle through each genre to decide which ones to keep
for k, v in genre_dictionary.items():
  if v == 1: # count is only 1, so 'pop' it off the dictionary
    fav_genre_dictionary.pop(k)
"""

# now print out our favorite genres
for key in fav_genre_dictionary.keys():
    print(key, "-", fav_genre_dictionary.get(key))
# ---------------------------------------------------------------------------
# use matplotlib to draw a pie chart of our favorite genres

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
_ = ax.pie(
    list(fav_genre_dictionary.values()), labels=list(fav_genre_dictionary.keys())
)
# ---------------------------------------------------------------------------
# use matplotlib to draw a histogram / bar chart
plt.hist(dataframe["Danceability"], bins=20, edgecolor="black")
plt.xlabel("Danceability")
plt.ylabel("Frequency")
plt.title("Distribution of Danceability")
plt.show()
# ---------------------------------------------------------------------------
# use matplotlib to draw a scatter plot
plt.scatter(dataframe["Danceability"], dataframe["Energy"], alpha=0.5)
plt.xlabel("Danceability")
plt.ylabel("Energy")
plt.title("Danceability vs. Energy")
plt.show()
