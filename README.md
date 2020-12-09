# NYC-Tree-Census

#Data Source: https://data.cityofnewyork.us/Environment/2015-Street-Tree-Census-Tree-Data/pi5s-9p35

It was originally a huge file, my computer was able to download it, but when I tried to open it, a lot of the rows were removed,so this data set is probably not complete :(

A lot of the columns were not very useful to me, they just described the position of the tree, any damage it had, geographic coordinates, etc.
I decided to get rid of most of the columns that were not of interest, and I also narrowed the data down to only trees that were alive and in Manhattan, in hopes of making the file smaller and easier to process.


I used google sheets to verify my data. In my program I calculated the average diameter of a tree.
The method I used was to set a counter and add the diameter with each iteration, and then divide that total by the number of rows.
Google sheets was able to verify that the number of trees was correct, however it would not calculate the average tree diameter. I used Minitab to calculate the average (8.752 inches) and it confirmed the result from my python program.

Minitab also found the median to be 8.00 inches, which isn’t too far off from the mean, indicating that there weren’t any outliers.


* nyctrees.py           -- Python program that creates a new file, 'nyctreesCLEAN.csv' for records of trees that are alive and in Manhattan
* nyctreesCLEAN.csv     -- file which contains records of trees that are alive and in manhattan, from nyctrees.py
* nyctrees2.py          -- Python program that calculates summary statistics for trees in Manhattan, and creates a new file 'manhattantrees.csv'
* manhattantrees.csv    -- further cleaned dataset that contained records of trees that are alive and in Manhattan, from nyctrees2.py
* minitab-stats.png     -- screenshot of summary statistics calculated in Minitab

