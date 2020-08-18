# NYC-Tree-Census

#Data Source: https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/pi5s-9p35

#cleaned dataset- 'newtrees.csv'
#python program to clean data and calculate statistics- 'TreeStats.py'

I chose to work with this one because I thought it was so cool that someone decided to do a tree census.
It was originally a huge file, my computer was able to download it, but when I tried to open it, a lot of the rows were removed,so this data set is not complete.
A lot of the columns were not very useful to me, they just described the position of the tree, any damage it had, geographic coordinates, etc.
I decided to get rid of most of the columns that were not of interest, and I also narrowed the data down to only trees that were alive and in Manhattan, in hopes of making the file smaller.
The total number of trees that my program found is most likely incorrect because many of the records had been excluded when I tried opening the file.
Additionally, the average diameter is inaccurate because of the missing records, and data dictionary says that the individual measurements round to the nearest whole inch, which, in my opinion, is a lot to round off.

I used google sheets to try to verify my data. In my program I calculated the average diameter of a tree.
The method I used was to set a counter and add the diameter with each iteration, and then divide that total by the number of rows.
Google sheets was able to verify that the number of trees was correct, however it would not calculate the average tree diameter. I used Minitab to calculate the average (8.752 inches) and it confirmed the result from my python program.

Minitab also found the median (8.00) which isn’t too far off from the mean, indicating that there weren’t any outliers.

#This is shown in the file 'minitab-stats.png'
