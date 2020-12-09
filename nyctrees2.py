
#Samantha Michelle Garcia

#NYC Tree Census 2015 - Part 2

"""

-get rid of status column
-count how many trees are in each neighborhood
-rename columns
-sort the trees by increasing diameter, and then alphabetically by name and neighborhood
-count the number of trees
-get the biggest diameter
-get mean and median tree diameter and compare the two

"""

import pandas as pd

def trees():
    
    in_trees = "nyctreesCLEAN.csv" #cleaned dataset, only trees in manhattan

    df = pd.read_csv(in_trees, na_values = 0)
    df = df[["Name", "Neighborhood", "Tree Diameter"]]   #columns I want to keep

    out_trees = "manhattantrees.csv"  #new tree csv file

    num_trees = str(df.shape[0]) #number of rows = number of trees

    neighborhood_trees = df["Neighborhood"].value_counts()

    #number of trees in each neighborhood
    df = df.sort_values(["Tree Diameter", "Name", "Neighborhood"])
    df.to_csv(out_trees, sep = ",")  #writing to new tree csv file
    
    print("The number of trees that are alive in Manhattan is " + num_trees)

    print("\n\n")

    print("Neighborhood \t\t\t\t Number of Trees")
    print(neighborhood_trees)
    
    print("\n")

    maxDiameter = df["Tree Diameter"].max()
    print("The biggest tree diameter is " + str(maxDiameter))
    
    print("\n")

    median = df["Tree Diameter"].median()
    print("The median tree diameter is " + str(median))

    print("\n")

    mean = df["Tree Diameter"].mean()
    print("The average tree diameter is " + str(mean))
    
    print("\n")
    
    if (mean > median):
        print("The data is right skewed.")
    elif (mean < median):
        print("The data is left skewed.")
    elif (mean == median):
        print("The data has an even distribution")

    print("New file successfully created 'manhattantrees.csv'")


trees()














