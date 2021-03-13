import csv
import os

#Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

#Assign a variable for the file to save to a path
file_to_save = os.path.join("analysis","elections_analysis.txt")

#Open the election results and read the file
with open(file_to_load) as election_data:

    #To do: read and analyze the data here
    file_reader = csv.reader(election_data)

    #read and print header row
    headers = next(file_reader)
    print(headers)
