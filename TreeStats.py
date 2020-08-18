#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Samantha Garcia
Assignment 2

1. use only tree species name, status (alive, dead, stump) column, and neighborhood columns
2. use only rows for trees with status = "Alive"
3. only use rows for trees in manhattan
4. re name columns in header
5. count number of rows = number of trees that are alive in manhattan
"""

import csv


def trees():
    
    num_rows = 0    #number of rows = number of trees
    diameter_sum = 0    #to add up all diameters (row[4]) and then divide by number of rows/trees to get avg diameter
    
    in_trees = open("Trees.csv", "r")
    out_trees = open("newtrees.csv", "w")
    reader = csv.reader(in_trees)
    writer = csv.writer(out_trees)
    
    header = ["Name", "Status", "Neighborhood", "Tree Diameter"] #creating header
    writer.writerow(header)
    
    try:
        for row in reader:
            if row[30] != "Manhattan":
              each_row = [] #It wouldn't just let me leave it blank, my idea was to exclude rows that were not in manhattan
            elif row[7] != "Alive":
                each_row = [] #do nothing
            else:
                each_row = [row[10], row[7], row[35], row[4]]
                writer.writerow(each_row)   
                num_rows+= 1
                diameter_sum += int(row[4])
    
    except Exception as e:    
        print("didn't work!")
        print(e)
 
    diameter_avg = diameter_sum / num_rows
    print("There are " , num_rows, " trees that are alive in Manhattan!") 
    print("The average diameter of a tree in Manhattan is ", diameter_avg, " inches!")
    out_trees.close()
    
trees()