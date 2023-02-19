""" Working with Composite Data Types """

""" Defining the dictionary """

import csv                                          # imports the csv module to read the csv file 
import copy                                         # imports the copy module to store the data in memory 
myVehicle = {                                       # define a dictionary that will serve as your composite type for reading the tabular data
    "vin" : "<empty>",                              # data is stored as key : value
    "make" : "<empty>" ,                            # each key:value is separated by comma
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
for key, value in myVehicle.items():                # loop to iterate over the initial keys and values of the dictionary 
    print("{} : {}".format(key,value))              # prints key and its value as formatted
    
myInventoryList = []                                # Define an empty list to hold the car inventory that you will read 


""" Copying the CSV file into memory """

with open('./A6-compositeData/car_fleet.csv') as csvFile:               # Opens car_fleet.csv as csvFile 
    csvReader = csv.reader(csvFile, delimiter=',')                      # function using the csv 
    lineCount = 0                                                       # defines lineCount as 0
    for row in csvReader:                                               # loop for rows in csvReader 
        if lineCount == 0:                                              # if lineCount is 0 then print line below
            print(f'Column names are: {", ".join(row)}')                # prints the columns, joins row with ', ' as a separator
            lineCount += 1                                              # lineCount is +1
        else:  
            # line below uses the dict. keys to print table heading and defines row numbers of dictionary for each table heading.
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)   # with out this line the rest of table will not print, it makes a deep copy of dictionary to memory and prints all of dictionary
            currentVehicle["vin"] = row[0]          # defines dictionary key "vin" for its value to be printed at row 0 
            currentVehicle["make"] = row[1]         # defines dictionary key "make" for its value to be printed at row 1 
            currentVehicle["model"] = row[2]        # defines dictionary key "model" for its value to be printed at row 2 
            currentVehicle["year"] = row[3]         # defines dictionary key "year" for its value to be printed at row 3 
            currentVehicle["range"] = row[4]        # defines dictionary key "range" for its value to be printed at row 4 
            currentVehicle["topSpeed"] = row[5]     # defines dictionary key "topSpeed" for its value to be printed at row 5 
            currentVehicle["zeroSixty"] = row[6]    # defines dictionary key "zeroSixty" for its value to be printed at row 6 
            currentVehicle["mileage"] = row[7]      # defines dictionary key "mileage" for its value to be printed at row 7 
            myInventoryList.append(currentVehicle)  # appends myInventoryList (list) with currentVehicle data (deepcopy of myVehicle)
            lineCount += 1                          # adds +1 to lineCount
    print(f'Processed {lineCount} lines.')          # prints the number of lines in lineCount
   
""" Printing the car inventory """
   
for myCarProperties in myInventoryList:         # for myCarProperties (items) in myInventoryList (list)
    for key, value in myCarProperties.items():  # for key and value in myCarProperties (list) items
        print("{} : {}".format(key,value))      # print key and value as formatted
        print("-----")                          # prints '-----' to separate each myCarProperties
        