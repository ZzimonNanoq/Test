from typing import Any, Union

import numpy as np
import pandas as pd
import matplotlib

#part 1.1 load contents of files movies & ratings
# combine contents of both files into single dataframe, you map drop timestamp column
#.2 show a summary statitics and a summary of possible missing values in the combined dataframe
#.3 calculate the average rating for each movie and show the 10 highest rated movies
#.4 add to your dataframe a column rating_count to record the number of rating for each movie.
# Visualize the ratings and the number of ratings and comment on any relationship that exist
# between rating and rating_count. Can you suggest a threshold for the number of ratings under
# which the rating can be considered as not significant?
#.5 Using the threshold found, transform rating column to binary 1 for like -1 for dislike
#.6 transform the column genres of the dataset into a binary form
#.7 convert the resulting dataframe to one wherein the rows are the movie titles and the columns
# are the user IDs
#.8 consider the movie Forrest Gump. what are your first 10 movie recommendations for a user who
# has liked that movie?
from pandas import DataFrame
from pandas.io.parsers import TextFileReader

movies = pd.read_csv("movies.csv"); print(movies.shape)
ratings = pd.read_csv("ratings.csv");# print(ratings.shape)
rating = ratings.drop('timestamp',axis=1); print(rating.shape)

totmov = [movies,rating]
resframe = pd.concat(totmov); print(resframe.shape)
print(resframe.loc[:]['title'])