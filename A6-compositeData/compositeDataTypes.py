""" Working with Composite Data Types """

""" Defining the dictionary """

import csv                  # imports the csv modual to read the csv file 
import copy                 # imports the copy modual to store the data in memory 
myVehicle = {               # define a dictionary that will serve as your composite type for reading the tabular data
    "vin" : "<empty>",
    "make" : "<empty>" ,
    "model" : "<empty>" ,
    "year" : 0,
    "range" : 0,
    "topSpeed" : 0,
    "zeroSixty" : 0.0,
    "mileage" : 0
}
for key, value in myVehicle.items():            # loop to iterate over the initial keys and values of the dictionary 
    print("{} : {}".format(key,value))           
    
myInventoryList = []                            # Define an empty list to hold the car inventory that you will read 


""" Copying the CSV file into memory """

with open('car_fleet.csv') as csvFile:              # Opens car_fleet.csv as csvFile 
    csvReader = csv.reader(csvFile, delimiter=',')  # function using the csv 
    lineCount = 0  
    for row in csvReader:                           # loop for rows in csvReader 
        if lineCount == 0:
            print(f'Column names are: {", ".join(row)}')  # prints the colmns, using ', ' as separator
            lineCount += 1  
        else:  
            # line below prints the table heading
            print(f'vin: {row[0]} make: {row[1]}, model: {row[2]}, year: {row[3]}, range: {row[4]}, topSpeed: {row[5]}, zeroSixty: {row[6]}, mileage: {row[7]}')  
            currentVehicle = copy.deepcopy(myVehicle)   # with out this line the rest of table will not print
            currentVehicle["vin"] = row[0]          #column 1 
            currentVehicle["make"] = row[1]         #colummn 2
            currentVehicle["model"] = row[2]        #column 3
            currentVehicle["year"] = row[3]         #col 4
            currentVehicle["range"] = row[4]        #col 5
            currentVehicle["topSpeed"] = row[5]     #col 6
            currentVehicle["zeroSixty"] = row[6]    #col 7
            currentVehicle["mileage"] = row[7]      #col 8
            myInventoryList.append(currentVehicle)  
            lineCount += 1  
    print(f'Processed {lineCount} lines.')
   
""" Printing the car inventory """
   
for myCarProperties in myInventoryList:         #loop myCarProperties in myInventoryList
    for key, value in myCarProperties.items():  #loop checks key and value in myCarProperties items
        print("{} : {}".format(key,value))      # print format is key and value
        print("-----")                          # prints '-----' to separate each myCarProperties
        