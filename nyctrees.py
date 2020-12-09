
#Samantha Michelle Garcia

#NYC Tree Census 2015

"""

1. use only tree species name, status (alive, dead, stump) column, and neighborhood columns
2. use only rows for trees with status = "Alive"
3. only use rows for trees in manhattan
4. re name columns in header
5. count number of rows = number of trees that are alive in manhattan

"""

import csv


def trees():
    
    num_rows = 0    #counter
    diameter_sum = 0    #sum all diameters / num_rows == average diameter

    in_trees = open("Trees.csv", "r")
    reader = csv.reader(in_trees)

    #create new file for records i want to keep
    out_trees = open("nyctreesCLEAN.csv", "w")
    writer = csv.writer(out_trees)
    
    header = ["Name", "Status", "Neighborhood", "Tree Diameter"] #creating header
    writer.writerow(header)
    
    try:
        for row in reader:
            if row[30] != "Manhattan":
              each_row = [] #do nothing
            elif row[7] != "Alive":
                each_row = [] #do nothing

            #if tree is in manhattan and is alive
            #keep these columns from dataset
            else:
                each_row = [row[10], row[7], row[35], row[4]]
                writer.writerow(each_row)   
                num_rows+= 1
                diameter_sum += int(row[4])
    
    except Exception as e:    
        print("didn't work!")
        print(e)
 
    diameter_avg = diameter_sum / num_rows
    print("There are " + str(num_rows) + " trees that are alive in Manhattan!") 
    print("The average diameter of a tree in Manhattan is " + str(diameter_avg) + " inches!")
    out_trees.close()

    print("New file succesfully created 'nyctreesCLEAN.csv'")
    
trees()